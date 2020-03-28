import os
import yaml
import shutil
import logging
import logging.config

from settings import BASE_DIR
from slcore.environment import setup_target_dir, get_target_dir
from slcore.srcodec import SRCodeController
from slcore.qemuc import QEMUController
from slcore.compositor import unpack
from slcore.profile.firmwaref import get_firmware
from slcore.analyses.scheduler import run_static_analysis, run_diagnosis, \
    run_trace_analysis, run_dt_renderer, run_bootup
from slcore.database.dbf import get_database
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.common import load_dtb


class Project(object):
    def __init__(self, uuid=None, arch=None, endian=None, target_dir=None,
                 brand=None, target=None, subtarget=None, images=None, dtbs=None,
                 source=None, cross_compile=None, makeout=None):
        """
        Those arguments can be divided into 3 groups.
        1. basics: uuid/arch/endian/target_dir [required]
        2. brand related: brand, target, subtarget [optional]
        3. source related: source/cross_compile/makeout [optional]
        """
        self.target_dir = target_dir
        self.attrs = {
            'uuid': uuid,
            'arch': arch,
            'endian': endian,
            'target_dir': target_dir,
            'brand': brand,
            'target': target,
            'subtarget': subtarget,
            'source': source,
            'cross_compile': cross_compile,
            'makeout': makeout,
            'images': images,
            'dtbs': dtbs,
        }

    def exists(self):
        return os.path.exists(
            os.path.join(self.target_dir, 'project.yaml'))

    def rename(self, new_target_dir):
        os.system('mv {} {}'.format(self.target_dir, new_target_dir))
        self.attrs['target_dir'] = new_target_dir
        self.target_dir = new_target_dir

    def save(self):
        """
        save project.yaml
        """
        yaml.safe_dump(
            self.attrs,
            open(os.path.join(self.target_dir, 'project.yaml'), 'w'))

    def load(self):
        """
        load project.yaml
        """
        self.attrs = yaml.safe_load(
            open(os.path.join(self.target_dir, 'project.yaml')))
        self.target_dir = self.attrs['target_dir']


def __project_get_current():
    current = os.path.join(BASE_DIR, '.project')
    if os.path.exists(current):
        kwargs = yaml.safe_load(open(current))
        project = Project(**kwargs)
        return project
    else:
        return None


def __project_set_current(project):
    current = os.path.join(BASE_DIR, '.project')
    yaml.safe_dump(project.attrs, open(current, 'w'))


def __project_clear_current():
    current = os.path.join(BASE_DIR, '.project')
    os.remove(current)


def project_open(uuid):
    target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is not None:
        project_print('please close current project {}'.format(project.attrs['uuid']))
        return False

    project = Project(target_dir=target_dir)
    if project.exists():
        project.load()
    else:
        project_print('please create a project first')
        return False

    __project_set_current(project)
    return True


def project_config(uuid=None, arch=None, endian=None,
                   brand=None, target=None, subtarget=None,
                   source=None, cross_compile=None, makeout=None):
    project = __project_get_current()
    if project is None:
        project_print('please create/open a project {}'.format(project.attrs['uuid']))
        return False

    if uuid is not None:
        project.attrs['uuid'] = uuid
    if arch is not None:
        project.attrs['arch'] = arch
    if endian is not None:
        project.attrs['endian'] = endian
    if brand is not None:
        project.attrs['brand'] = brand
    if target is not None:
        project.attrs['target'] = target
    if subtarget is not None:
        project.attrs['subtarget'] = subtarget
    if source is not None:
        project.attrs['source'] = source
    if cross_compile is not None:
        project.attrs['cross_compile'] = cross_compile
    if makeout is not None:
        project.attrs['makeout'] = makeout
    __project_set_current(project)
    return True


def project_create(uuid, arch, endian,
                   brand=None, target=None, subtarget=None,
                   source=None, cross_compile=None, makeout=None,
                   mode='cmdline'):
    project = __project_get_current()
    if project is not None:
        project_print('please close current project {}'.format(project.attrs['uuid']))
        return False

    target_dir = setup_target_dir(uuid)
    if mode == 'cmdline':
        project = Project(
            uuid, arch, endian, target_dir=target_dir,
            brand=brand, target=target, subtarget=subtarget,
            source=source, cross_compile=cross_compile, makeout=makeout)
    else:
        raise NotImplementedError('cannot support wizard mode')

    project.save()
    __project_set_current(project)
    return True


def project_rename(uuid):
    new_target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    project.rename(new_target_dir)
    project.attrs['uuid'] = uuid
    __project_set_current(project)
    return True


def project_close():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    project.save()
    __project_clear_current()
    return True


def project_show():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    for k, v in project.attrs.items():
        if isinstance(v, list):
            for vv in v:
                project_print('{}: {}'.format(k, vv))
        else:
            project_print('{}: {}'.format(k, v))
    return True


def update_current_project(project):
    __project_set_current(project)


def get_current_project():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return None
    return project


def project_delete(uuid):
    target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is not None:
        if os.path.realpath(project.target_dir) == os.path.realpath(target_dir):
            __project_clear_current()
    os.system('rm -r {}'.format(target_dir))
    return True


def project_get_srcodec():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return None

    srcodec = SRCodeController()
    path_to_source_code = project.attrs['source'] # checked
    if path_to_source_code is None:
        return None
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))

    cross_compile = project.attrs['cross_compile'] # checked
    if cross_compile is None:
        return None
    srcodec.set_path_to_cross_compile(cross_compile)
    srcodec.set_endian(project.attrs['endian'])
    srcodec.set_arch(project.attrs['arch'])
    srcodec.set_path_to_makeout(project.attrs['makeout'])
    return srcodec


def project_get_qemuc():
    from settings import WORKING_DIR, QEMU_DIR_NAME
    return QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))


def project_setup_logging(default_level=logging.INFO):
    project = __project_get_current()
    if project is None:
        return True

    uuid = project.attrs['uuid']
    target_dir = project.attrs['target_dir']

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.yaml')
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        config['handlers']['file']['filename'] = os.path.join(target_dir, '{}.log'.format(uuid))
        config['root']['level'] = default_level
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    return True


def project_print(message):
    print('[+] {}'.format(message))


def project_run_static_analysis(args):
    # 1 standard_setup
    firmware = project_standard_warmup(args)
    # 2. analyze the source code
    run_static_analysis(firmware)
    # 3. take snapshots to save results
    return project_standard_wrapup(firmware)


def project_run_diagnosis(args):
    # 1 standard_setup
    firmware = project_standard_warmup(args)
    # 2. test the machine
    run_diagnosis(firmware)
    # 3. take snapshots to save results
    return project_standard_wrapup(firmware, archive=True)


def project_run_bootup(args):
    # 1 standard_setup
    firmware = project_standard_warmup(args)

    # 2 test the machine
    firmware.set_url(args.url)
    run_bootup(firmware)

    # 3. take snapshots to save results
    return project_standard_wrapup(firmware)


def project_run_atrace(args):
    # 1 standard_setup
    firmware = project_standard_warmup(args)
    # 2 run trace analysis
    run_trace_analysis(firmware)
    # 3. take snapshots to save results
    return project_standard_wrapup(firmware)


def project_run_generate(args):
    # 1 standard_setup
    firmware = project_standard_warmup(args)
    # 2 generate code from dtb
    run_dt_renderer(firmware)
    # 3. take snapshots to save results
    return project_standard_wrapup(firmware)


def project_standard_warmup(args, components=None, profile=None):
    project = get_current_project()
    if project is None:
        print('please open/create a new project')
        exit()

    target_dir = project.attrs['target_dir']
    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        path_to_profile = None
    if profile is not None:
        path_to_profile = profile

    firmware = project_migrate(path_to_profile=path_to_profile, components=components)
    firmware.set_arch(project.attrs['arch'])
    firmware.set_endian(project.attrs['endian'])
    firmware.set_brand(project.attrs['brand'])
    firmware.rerun = args.rerun
    firmware.path_to_summary = os.path.join(firmware.get_target_dir(), 'stats.yaml')

    firmware.srcodec = project_get_srcodec()
    firmware.qemuc = project_get_qemuc()
    if hasattr(args, 'nocompilation'):
        firmware.cancle_compilation = args.nocompilation

    firmware.max_iteration = 1
    firmware.trace_format = 'qemudebug'
    if hasattr(args, 'trace') and args.trace is not None:
        firmware.path_to_trace = args.trace
    else:
        firmware.path_to_trace = '{}/{}-{}-{}.trace'.format(
            firmware.get_target_dir(), '0', firmware.get_arch(), firmware.get_endian()
        )
    firmware.debug = args.debug

    if hasattr(args, 'firmware'):
        images = project.attrs['images']
        components = firmware.get_components()
        if components is not None:
            if args.firmware is not None and args.firmware != components.get_path_to_raw():
                firmware.components = unpack(args.firmware, target_dir=firmware.target_dir)
        elif args.firmware:
            firmware.components = unpack(args.firmware, target_dir=firmware.target_dir)
        elif images is not None and len(images):
            firmware.components = unpack(images[0], target_dir=firmware.target_dir)
        else:
            print('-f/--firmware missing')

    if hasattr(args, 'dtb'):
        dtbs = project.attrs['dtbs']
        components = firmware.get_components()
        if components is not None:
            if args.dtb is not None:
                firmware.set_dtb(args.dtb)
            elif components.has_device_tree():
                firmware.set_dtb(components.get_path_to_dtb())
        elif args.dtb:
            firmware.set_dtb(args.dtb)
        elif dtbs is not None and len(dtbs):
            firmware.set_dtb(dtbs[0])
        else:
            print('neither dtb was found in tested firmware nor -dtb was assigned')
    return firmware


def project_standard_wrapup(firmware, archive=False):
    firmware.snapshot()
    if archive and firmware.get_stage('user_mode'):
        return project_archive(firmware)
    return True


def project_migrate(path_to_profile=None, components=None):
    project = get_current_project()
    if project is None:
        print('please open/create a new project')
        return None

    firmware = get_firmware('simple')
    firmware.target_dir =  project.attrs['target_dir']

    # load profile from path_to_profile
    if path_to_profile:
        firmware.set_profile(path_to_profile=path_to_profile)
        # change save-to-path to avoid modifing our well-defined profile
        firmware.path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.yaml')
    else:
        firmware.set_profile(target_dir=firmware.get_target_dir(), first=True)

    # handle components
    if components is not None:
        # copy the firmware to working path
        firmware.set_working_path(
            os.path.join(firmware.get_target_dir(), components.get_raw_name()))
        if not os.path.exists(firmware.working_path):
            shutil.copy(
                os.path.join(os.getcwd(), components.get_path_to_raw()),
                os.path.join(firmware.working_path)
        )
        firmware.set_components(components)

    return firmware


def project_archive(firmware):
    """Should be called after firmware.snapshot()."""
    project = get_current_project()
    if project is None:
        print('please open/create a new project')
        return None

    target_dir = project.target_dir

    # move profile to examples/profiles/machine_name/profile.yaml
    target_profiles = os.path.join(BASE_DIR, 'examples/profiles/{}'.format(
            firmware.get_machine_name()))
    os.makedirs(target_profiles, exist_ok=True)
    os.system('cp {} {}'.format(
        os.path.join(target_dir, 'profile.yaml'),
        os.path.join(target_profiles, 'profile.yaml')
    ))

    # move dtb     to examples/profiles/machine_name/profile.dtb
    os.system('cp {} {}'.format(
        firmware.dtb,
        os.path.join(target_profiles, 'profile.dtb')
    ))
    # we've updated the path to dtb un firmware.snapshot()

    # move qemu c files to examples/machines/machine_name/profile.yaml
    target_machines = os.path.join(BASE_DIR, 'examples/machines/{}'.format(firmware.get_machine_name()))
    os.makedirs(target_machines, exist_ok=True)
    os.system('cp -r {}/* {}'.format(
        os.path.join(target_dir, 'qemu-4.0.0'),
        target_machines,
    ))

    # update support list
    if firmware.dtb is None:
        return False

    dts = load_dtb(firmware.dtb)
    compatible = find_compatible_in_fdt(dts)

    support = get_database('support')
    board = support.select('board', arch=firmware.get_arch(), board=firmware.get_board())
    if board is None:
        board = {'device_tree': True}
    target_profile = os.path.join('examples/profiles', firmware.get_machine_name(), 'profile.yaml')
    if 'profiles' not in board:
        board['profiles'] = {}
    if target_profile not in board['profiles']:
        board['profiles'][target_profile] = {
            'brand': project.attrs['brand'],
             'version': firmware.get_kernel_version(),
            'target': project.attrs['target'],
            'subtarget': project.attrs['subtarget']
        }

    if 'compatible' not in board:
        board['compatible'] = {}
    for cmptbl in compatible:
        if cmptbl not in board['compatible']:
            board['compatible'][cmptbl] = target_profile

    if 'targets' not in board:
        board['targets'] = {}
    if project.attrs['brand'] not in board['targets']:
        board['targets'][project.attrs['brand']] = []
    if project.attrs['target'] not in board['targets'][project.attrs['brand']]:
        board['targets'][project.attrs['brand']].append(project.attrs['target'])

    support = support.update(firmware.get_board(), board=board, arch=firmware.get_arch())
    return True

