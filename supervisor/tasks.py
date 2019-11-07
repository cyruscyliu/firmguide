from analyses.cpu import get_cpu_model_info
from analyses.extraction import extract_kernel_and_dtb
from analyses.flash import get_flash_info
from analyses.ic import get_ic_info
from analyses.metadata import get_metadata
from analyses.ram import get_ram_info
from analyses.srcode import get_source_code
from analyses.timer import get_timer_info
from analyses.trace.collection import trace_collection
from analyses.trace.policies import policy_checking
from analyses.uart import get_uart_info


def analysis(firmware):
    # let's start
    extract_kernel_and_dtb(firmware)
    get_metadata(firmware)
    get_source_code(firmware)
    get_cpu_model_info(firmware)
    get_ram_info(firmware)
    get_ic_info(firmware)
    get_timer_info(firmware)
    get_uart_info(firmware)
    get_flash_info(firmware)


def dynamic_analysis(firmware):
    trace_collection(firmware)
    policy_checking(firmware)
