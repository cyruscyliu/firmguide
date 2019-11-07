import subprocess

import qmp


def trace_collection(firmware):
    running_command = firmware.get_running_command()
    # nochain is too too slow
    trace_flags = '-d in_asm,cpu -D log/{}.trace'.format(firmware.uuid)
    qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
    full_command = ' '.join([running_command, trace_flags, qmp_flags])
    try:
        subprocess.run(full_command, timeout=60, shell=True)
    except subprocess.TimeoutExpired:
        qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
        qemu.connect()
        qemu.cmd('quit')
        qemu.close()
