import subprocess

import qmp


def trace_collection(firmware):
    running_command = firmware.get_running_command()
    trace_flags = '-d in_asm,cpu,nochain -D log/{}.trace'.format(firmware.uuid)
    qmp_flags = '-qmp tcp:localhost:4444,server,nowait'
    full_command = ' '.join([running_command, trace_flags, qmp_flags])
    try:
        subprocess.run(full_command, timeout=20, shell=True)
    except subprocess.TimeoutExpired:
        qemu = qmp.QEMUMonitorProtocol(('localhost', 4444))
        qemu.connect()
        qemu.cmd('quit')
        qemu.close()
