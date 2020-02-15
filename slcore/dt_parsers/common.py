import fdt
import os

def compile_dts(path_to_dts):
    path_to_dtb = path_to_dts + '.dtb'
    os.system('dtc -I dts -O dtb -f {} -o {} >/dev/null 2>&1'.format(path_to_dts, path_to_dtb))
    return path_to_dtb


def compile_dts_in_dtc(dir_to_dt_collection):
    path_to_dtbs = []
    for root, dirs, files in os.walk(dir_to_dt_collection):
        if len(dirs):
            continue
        for f in files:
            if not f.endswith('dts'):
                continue
            ff = os.path.join(root, f)
            path_to_dtb = compile_dts(ff)
            path_to_dtbs.append(path_to_dtbs)
    return path_to_dtbs


def compile_dts_in_dtcg(dir_to_dt_collection):
    for root, dirs, files in os.walk(dir_to_dt_collection):
        if len(dirs):
            continue
        for f in files:
            if not f.endswith('dts'):
                continue
            ff = os.path.join(root, f)
            path_to_dtb = compile_dts(ff)
            yield path_to_dtb


def load_dtb(path_to_dtb):
    with open(path_to_dtb, 'rb') as f:
        dtb = f.read()
    dts = fdt.parse_dtb(dtb)
    return dts

