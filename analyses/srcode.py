"""
Handle all about source code.
"""
import os
import yaml
import logging

from manager import finished, finish
from pyquery import PyQuery as pq

logger = logging.getLogger()
TASK_DESCRIPTION = 'let\'s get its source code'


def find_urls_in_openwrt_homepage(homepage):
    html = pq(url=homepage)
    a = html('a')
    image_builder = None
    dot_config = None
    for item in a.items():
        href = item.attr('href')
        if image_builder is None and href.find('ImageBuilder') != -1:
            image_builder = os.path.join(homepage, href)
        if dot_config is None and (href.find('config.diff') != -1):
            dot_config = os.path.join(homepage, href)
    return image_builder, dot_config


def find_url_for_kernel(version):
    # version: 2.6.30
    v1, v2, _ = version.split('.')
    if v1 == '3' and v2 > '0':
        v2 = 'x'
    if v1 > '3':
        v2 = 'x'
    root = 'https://mirrors.edge.kernel.org/pub/linux/kernel/'
    l1 = 'v{}.{}'.format(v1, v2)
    l2 = 'linux-{}.tar.gz'.format(version)
    return os.path.join(root, l1, l2)


def find_url_for_openwrt(revision):
    # 15.05
    if revision == '15.05':
        return "https://github.com/openwrt/chaos_calmer/archive/v15.05.tar.gz"
    else:
        raise NotImplementedError()


def cache_package(url, adjust):
    package_name = os.path.basename(url)
    cached_directory = os.path.join(os.getcwd(), 'cache', adjust)
    if not os.path.exists(cached_directory):
        os.makedirs(cached_directory)
    cached_path = os.path.join(cached_directory, package_name)
    os.system('wget -nc {} -O {} >/dev/null 2>&1'.format(url, cached_path))
    return cached_path


def get_source_code(firmware):
    logger.info(TASK_DESCRIPTION)
    if finished(firmware, 'get_source_code', 'by_default'):
        return
    brand = firmware.get_brand()
    revision = firmware.get_revision()  # 1
    kernel_version = firmware.get_kernel_version()  # 5
    kernel = find_url_for_kernel(kernel_version)  # 3
    kernel = cache_package(kernel, 'linux')  # 3
    target = firmware.get_target()  # 6
    subtarget = firmware.get_subtarget()  # 7
    if brand == 'openwrt':
        if firmware.homepage is None:
            with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
                openwrt_release_info = yaml.safe_load(f)
            try:
                url = openwrt_release_info[revision]['url']
                homepage = os.path.join(url, target, subtarget)
                logger.info(
                    '\033[32mdownload page found for OpenWrt project {}\033[0m'.format(
                        homepage))
            except NotImplementedError:
                logger.info('no available url for this version {}'.format(firmware.get('revision')))
                return
        else:
            homepage = firmware.homepage
        image_builder, dot_config = find_urls_in_openwrt_homepage(homepage)  # 2, 4
        # image_builder = cache_package(image_builder, os.path.join('openwrt', revision, target, subtarget))
        image_builder = find_url_for_openwrt(revision)
        image_builder = cache_package(image_builder, os.path.join('openwrt', revision))
        dot_config = cache_package(dot_config, os.path.join('openwrt', revision, target, subtarget))
    else:
        raise NotImplementedError()
    source_code = os.path.join(firmware.working_dir, 'source_code', 'linux-{}'.format(kernel_version))  # 8
    firmware.set_path_to_source_code(source_code)
    working_dir = os.path.join(firmware.working_dir, 'source_code')
    cmd = 'bash extract_dot_config.sh "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}" "{}"'.format(
        revision, image_builder, kernel, dot_config, kernel_version, target, subtarget, source_code, working_dir
    )
    logger.info('{} [BASH]'.format(cmd))
    pwd = os.getcwd()
    os.chdir(os.path.join(pwd, 'openwrt', 'extract_dot_config'))
    os.system('{} >/dev/null 2>&1'.format(cmd))
    os.chdir(pwd)
    finish(firmware, 'get_source_code', 'by_default')