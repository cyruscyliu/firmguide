/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/arm/arm.h"
#include "hw/intc/mv88f5181l_ic.h"

#define TYPE_MV88F5181L "mv88f5181l"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)

#define GPIO_DATA_OUT_REGISTER 0x00
#define GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER 0x04
#define GPIO_BLINK_ENABLE_REGISTER 0x08
#define GPIO_DATA_IN_POLARITY_REGISTER 0x0c
#define GPIO_DATA_IN_REGISTER 0x10
#define GPIO_INTERRUPT_CAUSE_REGISTER 0x14
#define GPIO_INTERRUPT_MASK_REGISTER 0x18
#define GPIO_INTERRUPT_LEVEL_MASK_REGISTER 0x1c
#define WINDOW0_CONTROL_REGISTER 0x00
#define WINDOW0_BASE_REGISTER 0x04
#define WINDOW0_REMAP_LOW_REGISTER 0x08
#define WINDOW0_REMAP_HIGH_REGISTER 0x0C
#define WINDOW1_CONTROL_REGISTER 0x10
#define WINDOW1_BASE_REGISTER 0x14
#define WINDOW1_REMAP_LOW_REGISTER 0x18
#define WINDOW1_REMAP_HIGH_REGISTER 0x1C
#define WINDOW2_CONTROL_REGISTER 0x20
#define WINDOW2_BASE_REGISTER 0x24
#define WINDOW2_REMAP_LOW_REGISTER 0x28
#define WINDOW2_REMAP_HIGH_REGISTER 0x2C
#define WINDOW3_CONTROL_REGISTER 0x30
#define WINDOW3_BASE_REGISTER 0x34
#define WINDOW4_CONTROL_REGISTER 0x40
#define WINDOW4_BASE_REGISTER 0x44
#define WINDOW5_CONTROL_REGISTER 0x50
#define WINDOW5_BASE_REGISTER 0x54
#define WINDOW6_CONTROL_REGISTER 0x60
#define WINDOW6_BASE_REGISTER 0x64
#define WINDOW7_CONTROL_REGISTER 0x70
#define WINDOW7_BASE_REGISTER 0x74
#define _88F5181_INTERNAL_REGISTERS_BASE_ADDRESS_REGISTER 0x80
#define CS0N_BASE_ADDRESS_REGISTER 0x100
#define CS0N_SIZE_REGISTER 0x104
#define CS1N_BASE_ADDRESS_REGISTER 0x108
#define CS1N_SIZE_REGISTER 0x10C
#define CS2N_BASE_ADDRESS_REGISTER 0x110
#define CS2N_SIZE_REGISTER 0x114
#define CS3N_BASE_ADDRESS_REGISTER 0x118
#define CS3N_SIZE_REGISTER 0x11C
#define DDR_SDRAM_CONFIGURATION_REGISTER 0x00
#define DDR_SDRAM_CONTROL_REGISTER 0x04
#define DDR_SDRAM_TIMING_LOW_REGISTER 0x08
#define DDR_SDRAM_TIMING_HIGH_REGISTER 0x0C
#define DDR2_SDRAM_TIMING_LOW_REGISTER 0x28
#define DDR2_SDRAM_TIMING_HIGH_REGISTER 0x7C
#define DDR_SDRAM_ADDRESS_CONTROL_REGISTER 0x10
#define DDR_SDRAM_OPEN_PAGES_CONTROL_REGISTER 0x14
#define DDR_SDRAM_OPERATION_REGISTER 0x18
#define DDR_SDRAM_OPERATION_CONTROL_REGISTER 0x2C
#define DDR_SDRAM_MODE_REGISTER 0x1C
#define EXTENDED_DDR_SDRAM_MODE_REGISTER 0x20
#define DDR_SDRAM_INITIALIZATION_CONTROL_REGISTER 0x80
#define DDR_SDRAM_ADDRESS_OR_CONTROL_PADS_CALIBRATION_REGISTER 0xC0
#define DDR_SDRAM_DATA_PADS_CALIBRATION_REGISTER 0xC4
#define DDR2_SDRAM_ODT_CONTROL_LOW_REGISTER 0x94
#define DDR2_SDRAM_ODT_CONTROL_HIGH_REGISTER 0x98
#define DDR2_SDRAM_ODT_CONTROL_REGISTER 0x9C
#define DDR_SDRAM_INTERFACE_MBUS_CONTROL_LOW_REGISTER 0x30
#define DDR_SDRAM_INTERFACE_MBUS_CONTROL_HIGH_REGISTER 0x34
#define DDR_SDRAM_INTERFACE_MBUS_TIMEOUT_REGISTER 0x38
#define DDR_SDRAM_MMASK_REGISTER 0xB0
#define MPP_CONTROL_0_REGISTER 0x00
#define MPP_CONTROL_1_REGISTER 0x04
#define MPP_CONTROL_2_REGISTER 0x50
#define DEVICE_MULTIPLEX_CONTROL_REGISTER 0x08
#define SAMPLE_AT_RESET_REGISTER 0x10
#define CSN0_BAR_SIZE 0x0c08
#define CSN1_BAR_SIZE 0x0d08
#define CSN2_BAR_SIZE 0x0c0c
#define CSN3_BAR_SIZE 0x0d0c
#define DEVCSN0_BAR_SIZE 0x0c10
#define DEVCSN1_BAR_SIZE 0x0d10
#define DEVCSN2_BAR_SIZE 0x0d18
#define BOOT_CSN_BAR_SIZE 0x0d14
#define P2P_MEM0_BAR_SIZE 0x0d1c
#define P2P_I_OR_O_BAR_SIZE 0x0d24
#define EXPANSION_ROM_BAR_SIZE 0x0d2c
#define BASE_ADDRESS_REGISTERS_ENABLE 0x0c3c
#define CSN0_BASE_ADDRESS_REMAP 0x0c48
#define CSN1_BASE_ADDRESS_REMAP 0x0d48
#define CSN2_BASE_ADDRESS_REMAP 0x0c4c
#define CSN3_BASE_ADDRESS_REMAP 0x0d4c
#define DEVCSN0_BASE_ADDRESS_REMAP 0x0c50
#define DEVCSN1_BASE_ADDRESS_REMAP 0x0d50
#define DEVCSN2_BASE_ADDRESS_REMAP 0x0d58
#define BOOTCSN_BASE_ADDRESS_REMAP 0x0d54
#define P2P_MEM0_BASE_ADDRESS_REMAP_LOW 0x0d5c
#define P2P_MEM0_BASE_ADDRESS_REMAP_HIGH 0x0d60
#define P2P_I_OR_O_BASE_ADDRESS_REMAP 0x0d6c
#define EXPANSION_ROM_BASE_ADDRESS_REMAP 0x0f38
#define DRAM_BAR_BANK_SELECT 0x0c1c
#define PCI_ADDRESS_DECODE_CONTROL 0x0d3c
#define PCI_DLL_CONTROL 0x1d20
#define PCI_OR_MPP_PADS_CALIBRATION 0x1d1c
#define PCI_COMMAND 0x0c00
#define PCI_MODE 0x0d00
#define PCI_RETRY 0x0c04
#define PCI_DISCARD_TIMER 0x0d04
#define MSI_TRIGGER_TIMER 0x0c38
#define PCI_ARBITER_CONTROL 0x1d00
#define PCI_P2P_CONFIGURATION 0x1d14
#define PCI_ACCESS_CONTROL_BASE_0_LOW 0x1e00
#define PCI_ACCESS_CONTROL_BASE_0_HIGH 0x1e04
#define PCI_ACCESS_CONTROL_SIZE_0 0x1e08
#define PCI_ACCESS_CONTROL_BASE_1_LOW 0x1e10
#define PCI_ACCESS_CONTROL_BASE_1_HIGH 0x1e14
#define PCI_ACCESS_CONTROL_SIZE_1 0x1e18
#define PCI_ACCESS_CONTROL_BASE_2_LOW 0x1e20
#define PCI_ACCESS_CONTROL_BASE_2_HIGH 0x1e24
#define PCI_ACCESS_CONTROL_SIZE_2 0x1e28
#define PCI_ACCESS_CONTROL_BASE_3_LOW 0x1e30
#define PCI_ACCESS_CONTROL_BASE_3_HIGH 0x1e34
#define PCI_ACCESS_CONTROL_SIZE_3 0x1e38
#define PCI_ACCESS_CONTROL_BASE_4_LOW 0x1e40
#define PCI_ACCESS_CONTROL_BASE_4_HIGH 0x1e44
#define PCI_ACCESS_CONTROL_SIZE_4 0x1e48
#define PCI_ACCESS_CONTROL_BASE_5_LOW 0x1e50
#define PCI_ACCESS_CONTROL_BASE_5_HIGH 0x1e54
#define PCI_ACCESS_CONTROL_SIZE_5 0x1e58
#define PCI_CONFIGURATION_ADDRESS 0x0c78
#define PCI_CONFIGURATION_DATA 0x0c7c
#define PCI_INTERRUPT_ACKNOWLEDGE 0x0c34
#define PCI_SERRN_MASK 0x0c28
#define PCI_INTERRUPT_CAUSE 0x1d58
#define PCI_INTERRUPT_MASK 0x1d5c
#define PCI_ERROR_ADDRESS_LOW 0x1d40
#define PCI_ERROR_ADDRESS_HIGH 0x1d44
#define PCI_ERROR_COMMAND 0x1d50
#define PCI_EXPRESS_DEVICE_AND_VENDOR_ID_REGISTER 0x0000
#define PCI_EXPRESS_COMMAND_AND_STATUS_REGISTER 0x0004
#define PCI_EXPRESS_CLASS_CODE_AND_REVISION_ID_REGISTER 0x0008
#define PCI_EXPRESS_BIST_HEADER_TYPE_AND_CACHE_LINE_SIZE_REGISTER 0x000c
#define PCI_EXPRESS_BAR0_INTERNAL_REGISTER 0x0010
#define PCI_EXPRESS_BAR0_INTERNAL_HIGH_REGISTER 0x0014
#define PCI_EXPRESS_BAR1_REGISTER 0x0018
#define PCI_EXPRESS_BAR1_HIGH_REGISTER 0x001c
#define PCI_EXPRESS_BAR2_REGISTER 0x0020
#define PCI_EXPRESS_BAR2_HIGH_REGISTER 0x0024
#define PCI_EXPRESS_SUBSYSTEM_DEVICE_AND_VENDOR_ID 0x002c
#define PCI_EXPRESS_EXPANSION_ROM_BAR_REGISTER 0x0030
#define PCI_EXPRESS_CAPABILITY_LIST_POINTER_REGISTER 0x0034
#define PCI_EXPRESS_INTERRUPT_PIN_AND_LINE_REGISTER 0x003c
#define PCI_EXPRESS_POWER_MANAGEMENT_CAPABILITY_HEADER_REGISTER 0x0040
#define PCI_EXPRESS_POWER_MANAGEMENT_CONTROL_AND_STATUS_REGISTER 0x0044
#define PCI_EXPRESS_MSI_MESSAGE_CONTROL_REGISTER 0x0050
#define PCI_EXPRESS_MSI_MESSAGE_ADDRESS_REGISTER 0x0054
#define PCI_EXPRESS_MSI_MESSAGE_ADDRESS_HIGH_REGISTER 0x0058
#define PCI_EXPRESS_MSI_MESSAGE_DATA_REGISTER 0x005c
#define PCI_EXPRESS_CAPABILITY_REGISTER 0x0060
#define PCI_EXPRESS_DEVICE_CAPABILITIES_REGISTER 0x0064
#define PCI_EXPRESS_DEVICE_CONTROL_STATUS_REGISTER 0x0068
#define PCI_EXPRESS_LINK_CAPABILITIES_REGISTER 0x006c
#define PCI_EXPRESS_LINK_CONTROL_STATUS_REGISTER 0x0070
#define PCI_EXPRESS_ADVANCED_ERROR_REPORT_HEADER_REGISTER 0x0100
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_STATUS_REGISTER 0x0104
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_MASK_REGISTER 0x0108
#define PCI_EXPRESS_UNCORRECTABLE_ERROR_SEVERITY_REGISTER 0x010c
#define PCI_EXPRESS_CORRECTABLE_ERROR_STATUS_REGISTER 0x0110
#define PCI_EXPRESS_CORRECTABLE_ERROR_MASK_REGISTER 0x0114
#define PCI_EXPRESS_ADVANCED_ERROR_CAPABILITY_AND_CONTROL_REGISTER 0x0118
#define PCI_EXPRESS_HEADER_LOG_FIRST_DWORD_REGISTER 0x011c
#define PCI_EXPRESS_HEADER_LOG_SECOND_DWORD_REGISTER 0x0120
#define PCI_EXPRESS_HEADER_LOG_THIRD_DWORD_REGISTER 0x0124
#define PCI_EXPRESS_HEADER_LOG_FOURTH_DWORD_REGISTER 0x0128
#define PCI_EXPRESS_BAR1_CONTROL_REGISTER 0x1804
#define PCI_EXPRESS_BAR2_CONTROL_REGISTER 0x1808
#define PCI_EXPRESS_EXPANSION_ROM_BAR_CONTROL_REGISTER 0x180c
#define PCI_EXPRESS_CONFIGURATION_ADDRESS_REGISTER 0x18f8
#define PCI_EXPRESS_CONFIGURATION_DATA_REGISTER 0x18fc
#define PCI_EXPRESS_INTERRUPT_CAUSE 0x1900
#define PCI_EXPRESS_INTERRUPT_MASK 0x1910
#define PCI_EXPRESS_WINDOW0_CONTROL_REGISTER 0x1820
#define PCI_EXPRESS_WINDOW0_BASE_REGISTER 0x1824
#define PCI_EXPRESS_WINDOW0_REMAP_REGISTER 0x182c
#define PCI_EXPRESS_WINDOW1_CONTROL_REGISTER 0x1830
#define PCI_EXPRESS_WINDOW1_BASE_REGISTER 0x1834
#define PCI_EXPRESS_WINDOW1_REMAP_REGISTER 0x183c
#define PCI_EXPRESS_WINDOW2_CONTROL_REGISTER 0x1840
#define PCI_EXPRESS_WINDOW2_BASE_REGISTER 0x1844
#define PCI_EXPRESS_WINDOW2_REMAP_REGISTER 0x184c
#define PCI_EXPRESS_WINDOW3_CONTROL_REGISTER 0x1850
#define PCI_EXPRESS_WINDOW3_BASE_REGISTER 0x1854
#define PCI_EXPRESS_WINDOW3_REMAP_REGISTER 0x185c
#define PCI_EXPRESS_WINDOW4_CONTROL_REGISTER 0x1860
#define PCI_EXPRESS_WINDOW4_BASE_REGISTER 0x1864
#define PCI_EXPRESS_WINDOW4_REMAP_REGISTER 0x186c
#define PCI_EXPRESS_WINDOW5_CONTROL_REGISTER 0x1880
#define PCI_EXPRESS_WINDOW5_BASE_REGISTER 0x1884
#define PCI_EXPRESS_WINDOW5_REMAP_REGISTER 0x188c
#define PCI_EXPRESS_DEFAULT_WINDOW_CONTROL_REGISTER 0x18b0
#define PCI_EXPRESS_EXPANSION_ROM_WINDOW_CONTROL_REGISTER 0x18c0
#define PCI_EXPRESS_EXPANSION_ROM_WINDOW_REMAP_REGISTER 0x18c4
#define PCI_EXPRESS_CONTROL_REGISTER 0x1a00
#define PCI_EXPRESS_STATUS_REGISTER 0x1a04
#define PCI_EXPRESS_COMPLETION_TIMEOUT_REGISTER 0x1a10
#define PCI_EXPRESS_FLOW_CONTROL_REGISTER 0x1a20
#define PCI_EXPRESS_ACKNOWLEDGE_TIMERS_1X_REGISTER 0x1a40
#define PCI_EXPRESS_DEBUG_CONTROL_REGISTER 0x1a60
#define PCI_EXPRESS_TL_CONTROL_REGISTER 0x1ab0
#define PORT0_USB_2_0_ID 0x00
#define PORT0_USB_2_0_HWGENERAL 0x04
#define PORT0_USB_2_0_HWHOST 0x08
#define PORT0_USB_2_0_HWDEVICE 0x0c
#define PORT0_USB_2_0_HWTXBUF 0x10
#define PORT0_USB_2_0_HWRXBUF 0x14
#define PORT0_USB_2_0_HWTTTXBUF 0x18
#define PORT0_USB_2_0_HWTTRXBUF 0x1c
#define PORT0_USB_2_0_CAPLENGTH 0x100
#define PORT0_USB_2_0_HCIVERSION 0x102
#define PORT0_USB_2_0_HCSPARAMS 0x104
#define PORT0_USB_2_0_HCCPARAMS 0x108
#define PORT0_USB_2_0_DCIVERSION 0x120
#define PORT0_USB_2_0_DCCPARAMS 0x124
#define PORT0_USB_2_0_USBCMD 0x140
#define PORT0_USB_2_0_USBSTS 0x144
#define PORT0_USB_2_0_USBINTR 0x148
#define PORT0_USB_2_0_FRINDEX 0x14c
#define PORT0_USB_2_0_PERIODICLISTBASE__OR__DEVICE_ADDR 0x154
#define PORT0_USB_2_0_ASYNCLISTADDR__OR__ENDPOINTLIST_ADDR 0x158
#define PORT0_USB_2_0_TTCTRL 0x15c
#define PORT0_USB_2_0_BURSTSIZE 0x160
#define PORT0_USB_2_0_TXFILLTUNING 0x164
#define PORT0_USB_2_0_TXTTFILLTUNING 0x168
#define PORT0_USB_2_0_CONFIGFLAG 0x180
#define PORT0_USB_2_0_PORTSC1 0x184
#define PORT0_USB_2_0_OTGSC 0x1a4
#define PORT0_USB_2_0_USBMODE 0x1a8
#define PORT0_USB_2_0_ENPDTSETUPSTAT 0x1ac
#define PORT0_USB_2_0_ENDPTPRIME 0x1b0
#define PORT0_USB_2_0_ENDPTFLUSH 0x1b4
#define PORT0_USB_2_0_ENDPTSTATUS 0x1b8
#define PORT0_USB_2_0_ENDPTCOMPLETE 0x1bc
#define PORT0_USB_2_0_ENDPTCTRL0 0x1c0
#define PORT0_USB_2_0_ENDPTCTRL1 0x1c4
#define PORT0_USB_2_0_ENDPTCTRL2 0x1c8
#define PORT0_USB_2_0_ENDPTCTRL3 0x1cc
#define PORT0_USB_2_0_BRIDGE_CONTROL_REGISTER 0x300
#define PORT0_USB_2_0_BRIDGE_INTERRUPT_CAUSE_REGISTER 0x310
#define PORT0_USB_2_0_BRIDGE_INTERRUPT_MASK_REGISTER 0x314
#define PORT0_USB_2_0_BRIDGE_ERROR_ADDRESS_REGISTER 0x31c
#define PORT0_USB_2_0_WINDOW0_CONTROL_REGISTER 0x320
#define PORT0_USB_2_0_WINDOW0_BASE_REGISTER 0x324
#define PORT0_USB_2_0_WINDOW1_CONTROL_REGISTER 0x330
#define PORT0_USB_2_0_WINDOW1_BASE_REGISTER 0x334
#define PORT0_USB_2_0_WINDOW2_CONTROL_REGISTER 0x340
#define PORT0_USB_2_0_WINDOW2_BASE_REGISTER 0x344
#define PORT0_USB_2_0_WINDOW3_CONTROL_REGISTER 0x350
#define PORT0_USB_2_0_WINDOW3_BASE_REGISTER 0x354
#define PORT0_USB_2_0_POWER_CONTROL_REGISTER 0x400
#define PHY_ADDRESS 0x000
#define SMI 0x004
#define ETHERNET_UNIT_DEFAULT_ADDRESS_EUDA 0x008
#define ETHERNET_UNIT_DEFAULT_ID_EUDID 0x00c
#define ETHERNET_UNIT_RESERVED_EU 0x014
#define ETHERNET_UNIT_INTERRUPT_CAUSE_EUIC 0x080
#define ETHERNET_UNIT_INTERRUPT_MASK_EUIM 0x084
#define ETHERNET_UNIT_ERROR_ADDRESS_EUEA 0x094
#define ETHERNET_UNIT_INTERNAL_ADDRESS_ERROR_EUIAE 0x098
#define ETHERNET_UNIT_PORT_PADS_CALIBRATION_EUPCR 0x0a0
#define ETHERNET_UNIT_CONTROL_EUC 0x0b0
#define BASE_ADDRESS_0_BA0 0x200
#define SIZE_S_0_SR0 0x204
#define BASE_ADDRESS_1_BA1 0x208
#define SIZE_S_1_SR1 0x20c
#define BASE_ADDRESS_2_BA2 0x210
#define SIZE_S_2_SR2 0x214
#define BASE_ADDRESS_3_BA3 0x218
#define SIZE_S_3_SR3 0x21c
#define BASE_ADDRESS_4_BA4 0x220
#define SIZE_S_4_SR4 0x224
#define BASE_ADDRESS_5_BA5 0x228
#define SIZE_S_5_SR5 0x22c
#define HIGH_ADDRESS_REMAP_HA_HARR0 0x280
#define HIGH_ADDRESS_REMAP_HA_HARR1 0x284
#define HIGH_ADDRESS_REMAP_HA_HARR2 0x288
#define HIGH_ADDRESS_REMAP_HA_HARR3 0x28c
#define BASE_ADDRESS_ENABLE_BARE 0x290
#define ETHERNET_PORT_ACCESS_PROTECT_EPAP 0x294
#define PORT_CONFIGURATION_GEC 0x400
#define PORT_CONFIGURATION_EXTEND_GECX 0x404
#define MII_SERIAL_PARAMETERS 0x408
#define GMII_SERIAL_PARAMETERS 0x40c
#define VLAN_ETHERTYPE_EVLANE 0x410
#define MAC_ADDRESS_LOW_MACAL 0x414
#define MAC_ADDRESS_HIGH_MACAH 0x418
#define SDMA_CONFIGURATION_SDC 0x41c
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_0_TO_PRIORITY_DSCP0 0x420
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_1_TO_PRIORITY_DSCP1 0x424
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_2_TO_PRIORITY_DSCP2 0x428
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_23_TO_PRIORITY_DSCP3 0x42c
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_24_TO_PRIORITY_DSCP4 0x430
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_25_TO_PRIORITY_DSCP5 0x434
#define IP_DIFFERENTIATED_SERVICES_CODEPOINT_6_TO_PRIORITY_DSCP6 0x438
#define PORT_SERIAL_CONTROL_PSC 0x43c
#define VLAN_PRIORITY_TAG_TO_PRIORITY_VPT2P 0x440
#define ETHERNET_PORT_STATUS_PS 0x444
#define TRANSMIT_QUEUE_COMMAND_TQC 0x448
#define MAXIMUM_TRANSMIT_UNIT_MTU 0x458
#define PORT_INTERRUPT_CAUSE_IC 0x460
#define PORT_INTERRUPT_CAUSE_EXTEND_ICE 0x464
#define PORT_INTERRUPT_MASK_PIM 0x468
#define PORT_EXTEND_INTERRUPT_MASK_PEIM 0x46c
#define PORT_RX_FIFO_URGENT_THRESHOLD_PRFUT 0x470
#define PORT_TX_FIFO_URGENT_THRESHOLD_PTFUT 0x474
#define PORT_RX_MINIMAL_FRAME_SIZE_PMFS 0x47c
#define PORT_RX_DISCARD_FRAME_COUNTER_GEDFC 0x484
#define PORT_OVERRUN_FRAME_COUNTER_POFC 0x488
#define PORT_INTERNAL_ADDRESS_ERROR_EUIAE 0x494
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q0 0x60c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q1 0x61c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q2 0x62c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q3 0x63c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q4 0x64c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q5 0x65c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q6 0x66c
#define ETHERNET_CURRENT_RECEIVE_DESCRIPTOR_POINTERS_CRDP_Q7 0x67c
#define RECEIVE_QUEUE_COMMAND_RQC 0x680
#define TRANSMIT_CURRENT_SERVED_DESCRIPTOR_POINTER 0x684
#define TRANSMIT_CURRENT_QUEUE_DESCRIPTOR_POINTER_TCQDP_Q0 0x6c0
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q0 0x700
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q0 0x704
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q0 0x708
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q1 0x710
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q1 0x714
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q1 0x718
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q2 0x720
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q2 0x724
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q2 0x728
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q3 0x730
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q3 0x734
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q3 0x738
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q4 0x740
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q4 0x744
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q4 0x748
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q5 0x750
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q5 0x754
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q5 0x758
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q6 0x760
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q6 0x764
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q6 0x768
#define TRANSMIT_QUEUE_TOKEN_BUCKET_COUNTER_TQXTBC_Q7 0x770
#define TRANSMIT_QUEUE_TOKEN_BUCKET_CONFIGURATION_TQXTBC_Q7 0x774
#define TRANSMIT_QUEUE_ARBITER_CONFIGURATION_TQXAC_Q7 0x778
#define MAC_MIB_COUNTERSNTERRUPT_CAUSE_REGISTER 0x1000
#define DESTINATION_ADDRESS_FILTER_SPECIAL_MULTICAST_TABLE_DFSMT 0x1400
#define DESTINATION_ADDRESS_FILTER_OTHER_MULTICAST_TABLE_DFUT 0x1500
#define DESTINATION_ADDRESS_FILTER_UNICAST_TABLE_DFUT 0x1600
#define DES_DATA_OUT_LOW_REGISTER 0x00000078
#define DES_DATA_OUT_HIGH_REGISTER 0x0000007c
#define DES_DATA_BUFFER_LOW_REGISTER 0x00000070
#define DES_DATA_BUFFER_HIGH_REGISTER 0x00000074
#define DES_INITIAL_VALUE_LOW_REGISTER 0x00000040
#define DES_INITIAL_VALUE_HIGH_REGISTER 0x00000044
#define DES_KEY0_LOW_REGISTER 0x00000048
#define DES_KEY0_HIGH_REGISTER 0x0000004c
#define DES_KEY1_LOW_REGISTER 0x00000050
#define DES_KEY1_HIGH_REGISTER 0x00000054
#define DES_KEY2_LOW_REGISTER 0x00000060
#define DES_KEY2_HIGH_REGISTER 0x00000064
#define DES_COMMAND_REGISTER 0x00000058
#define SHA_1_OR_MD5_DATA_IN_REGISTER 0x00000038
#define SHA_1_OR_MD5_BIT_COUNT_LOW_REGISTER 0x00000020
#define SHA_1_OR_MD5_BIT_COUNT_HIGH_REGISTER 0x00000024
#define SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_A_REGISTER 0x00000000
#define SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_B_REGISTER 0x00000004
#define SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_C_REGISTER 0x00000008
#define SHA_1_OR_MD5_INITIAL_VALUE_OR_DIGEST_D_REGISTER 0x0000000c
#define SHA_1_INITIAL_VALUE_OR_DIGEST_E_REGISTER 0x00000010
#define SHA_1_OR_MD5_AUTHENTICATION_COMMAND_REGISTER 0x00000018
#define AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER 0x000000a0
#define AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER 0x000000a4
#define AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER 0x000000a8
#define AES_ENCRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER 0x000000ac
#define AES_ENCRYPTION_KEY_COLUMN_3_REGISTER 0x00000090
#define AES_ENCRYPTION_KEY_COLUMN_2_REGISTER 0x00000094
#define AES_ENCRYPTION_KEY_COLUMN_1_REGISTER 0x00000098
#define AES_ENCRYPTION_KEY_COLUMN_0_REGISTER 0x0000009c
#define AES_ENCRYPTION_KEY_COLUMN_7_REGISTER 0x00000080
#define AES_ENCRYPTION_KEY_COLUMN_6_REGISTER 0x00000084
#define AES_ENCRYPTION_KEY_COLUMN_5_REGISTER 0x00000088
#define AES_ENCRYPTION_KEY_COLUMN_4_REGISTER 0x0000008c
#define AES_ENCRYPTION_COMMAND_REGISTER 0x000000b0
#define AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_3_REGISTER 0x000000e0
#define AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_2_REGISTER 0x000000e4
#define AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_1_REGISTER 0x000000e8
#define AES_DECRYPTION_DATA_IN_OR_OUT_COLUMN_0_REGISTER 0x000000ec
#define AES_DECRYPTION_KEY_COLUMN_3_REGISTER 0x000000d0
#define AES_DECRYPTION_KEY_COLUMN_2_REGISTER 0x000000d4
#define AES_DECRYPTION_KEY_COLUMN_1_REGISTER 0x000000d8
#define AES_DECRYPTION_KEY_COLUMN_0_REGISTER 0x000000dc
#define AES_DECRYPTION_KEY_COLUMN_7_REGISTER 0x000000c0
#define AES_DECRYPTION_KEY_COLUMN_6_REGISTER 0x000000c4
#define AES_DECRYPTION_KEY_COLUMN_5_REGISTER 0x000000c8
#define AES_DECRYPTION_KEY_COLUMN_4_REGISTER 0x000000cc
#define AES_DECRYPTION_COMMAND_REGISTER 0x000000f0
#define SECURITY_ACCELERATOR_COMMAND_REGISTER 0x00000100
#define SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_0_REGISTER 0x00000104
#define SECURITY_ACCELERATOR_DESCRIPTOR_POINTER_SESSION_1_REGISTER 0x00000114
#define SECURITY_ACCELERATOR_CONFIGURATION_REGISTER 0x00000108
#define SECURITY_ACCELERATOR_STATUS_REGISTER 0x0000010c
#define CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_CAUSE_REGISTER 0x00000120
#define CRYPTOGRAPHIC_ENGINES_AND_SECURITY_ACCELERATOR_INTERRUPT_MASK_REGISTER 0x00000124

#define MV88F5181L_GPIO_MMIO_SIZE 0x100
#define MV88F5181L_GPIO_MMIO_BASE 0xf1010100
#define MV88F5181L_CPU_ADDRESS_MAP_MMIO_SIZE 0x100
#define MV88F5181L_CPU_ADDRESS_MAP_MMIO_BASE 0xf1020000
#define MV88F5181L_DDR_SDRAM_CONTROLLER_MMIO_SIZE 0x200
#define MV88F5181L_DDR_SDRAM_CONTROLLER_MMIO_BASE 0xf1001400
#define MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_SIZE 0x100
#define MV88F5181L_PINS_MULTIPLEXING_INTERFACE_MMIO_BASE 0xf1010000
#define MV88F5181L_PCI_INTERFACE_MMIO_SIZE 0x2000
#define MV88F5181L_PCI_INTERFACE_MMIO_BASE 0xf1030000
#define MV88F5181L_PCIE_INTERFACE_MMIO_SIZE 0x2000
#define MV88F5181L_PCIE_INTERFACE_MMIO_BASE 0xf1040000
#define MV88F5181L_USB_2_0_CONTROLLER_MMIO_SIZE 0x500
#define MV88F5181L_USB_2_0_CONTROLLER_MMIO_BASE 0xf1050000
#define MV88F5181L_GIGABIT_ETHERNET_CONTROLLER_MMIO_SIZE 0x2000
#define MV88F5181L_GIGABIT_ETHERNET_CONTROLLER_MMIO_BASE 0xf1072000
#define MV88F5181L_CESA_MMIO_SIZE 0x200
#define MV88F5181L_CESA_MMIO_BASE 0xf109DD00

#define MV88F5181L_UART_MMIO_SIZE 0x200
#define MV88F5181L_UART_MMIO_BASE 0xf1012000

typedef struct MV88F5181LState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion mv88f5181l_gpio_mmio;
    uint32_t gpio_data_out_register;
    uint32_t gpio_data_out_enable_control_register;
    uint32_t gpio_blink_enable_register;
    uint32_t gpio_data_in_polarity_register;
    uint32_t gpio_data_in_register;
    uint32_t gpio_interrupt_cause_register;
    uint32_t gpio_interrupt_mask_register;
    uint32_t gpio_interrupt_level_mask_register;
    MemoryRegion mv88f5181l_cpu_address_map_mmio;
    uint32_t window0_control_register;
    uint32_t window0_base_register;
    uint32_t window0_remap_low_register;
    uint32_t window0_remap_high_register;
    uint32_t window1_control_register;
    uint32_t window1_base_register;
    uint32_t window1_remap_low_register;
    uint32_t window1_remap_high_register;
    uint32_t window2_control_register;
    uint32_t window2_base_register;
    uint32_t window2_remap_low_register;
    uint32_t window2_remap_high_register;
    uint32_t window3_control_register;
    uint32_t window3_base_register;
    uint32_t window4_control_register;
    uint32_t window4_base_register;
    uint32_t window5_control_register;
    uint32_t window5_base_register;
    uint32_t window6_control_register;
    uint32_t window6_base_register;
    uint32_t window7_control_register;
    uint32_t window7_base_register;
    uint32_t _88f5181_internal_registers_base_address_register;
    MemoryRegion mv88f5181l_ddr_sdram_controller_mmio;
    uint32_t cs0n_base_address_register;
    uint32_t cs0n_size_register;
    uint32_t cs1n_base_address_register;
    uint32_t cs1n_size_register;
    uint32_t cs2n_base_address_register;
    uint32_t cs2n_size_register;
    uint32_t cs3n_base_address_register;
    uint32_t cs3n_size_register;
    uint32_t ddr_sdram_configuration_register;
    uint32_t ddr_sdram_control_register;
    uint32_t ddr_sdram_timing_low_register;
    uint32_t ddr_sdram_timing_high_register;
    uint32_t ddr2_sdram_timing_low_register;
    uint32_t ddr2_sdram_timing_high_register;
    uint32_t ddr_sdram_address_control_register;
    uint32_t ddr_sdram_open_pages_control_register;
    uint32_t ddr_sdram_operation_register;
    uint32_t ddr_sdram_operation_control_register;
    uint32_t ddr_sdram_mode_register;
    uint32_t extended_ddr_sdram_mode_register;
    uint32_t ddr_sdram_initialization_control_register;
    uint32_t ddr_sdram_address_or_control_pads_calibration_register;
    uint32_t ddr_sdram_data_pads_calibration_register;
    uint32_t ddr2_sdram_odt_control_low_register;
    uint32_t ddr2_sdram_odt_control_high_register;
    uint32_t ddr2_sdram_odt_control_register;
    uint32_t ddr_sdram_interface_mbus_control_low_register;
    uint32_t ddr_sdram_interface_mbus_control_high_register;
    uint32_t ddr_sdram_interface_mbus_timeout_register;
    uint32_t ddr_sdram_mmask_register;
    MemoryRegion mv88f5181l_pins_multiplexing_interface_mmio;
    uint32_t mpp_control_0_register;
    uint32_t mpp_control_1_register;
    uint32_t mpp_control_2_register;
    uint32_t device_multiplex_control_register;
    uint32_t sample_at_reset_register;
    MemoryRegion mv88f5181l_pci_interface_mmio;
    uint32_t csn0_bar_size;
    uint32_t csn1_bar_size;
    uint32_t csn2_bar_size;
    uint32_t csn3_bar_size;
    uint32_t devcsn0_bar_size;
    uint32_t devcsn1_bar_size;
    uint32_t devcsn2_bar_size;
    uint32_t boot_csn_bar_size;
    uint32_t p2p_mem0_bar_size;
    uint32_t p2p_i_or_o_bar_size;
    uint32_t expansion_rom_bar_size;
    uint32_t base_address_registers_enable;
    uint32_t csn0_base_address_remap;
    uint32_t csn1_base_address_remap;
    uint32_t csn2_base_address_remap;
    uint32_t csn3_base_address_remap;
    uint32_t devcsn0_base_address_remap;
    uint32_t devcsn1_base_address_remap;
    uint32_t devcsn2_base_address_remap;
    uint32_t bootcsn_base_address_remap;
    uint32_t p2p_mem0_base_address_remap_low;
    uint32_t p2p_mem0_base_address_remap_high;
    uint32_t p2p_i_or_o_base_address_remap;
    uint32_t expansion_rom_base_address_remap;
    uint32_t dram_bar_bank_select;
    uint32_t pci_address_decode_control;
    uint32_t pci_dll_control;
    uint32_t pci_or_mpp_pads_calibration;
    uint32_t pci_command;
    uint32_t pci_mode;
    uint32_t pci_retry;
    uint32_t pci_discard_timer;
    uint32_t msi_trigger_timer;
    uint32_t pci_arbiter_control;
    uint32_t pci_p2p_configuration;
    uint32_t pci_access_control_base_0_low;
    uint32_t pci_access_control_base_0_high;
    uint32_t pci_access_control_size_0;
    uint32_t pci_access_control_base_1_low;
    uint32_t pci_access_control_base_1_high;
    uint32_t pci_access_control_size_1;
    uint32_t pci_access_control_base_2_low;
    uint32_t pci_access_control_base_2_high;
    uint32_t pci_access_control_size_2;
    uint32_t pci_access_control_base_3_low;
    uint32_t pci_access_control_base_3_high;
    uint32_t pci_access_control_size_3;
    uint32_t pci_access_control_base_4_low;
    uint32_t pci_access_control_base_4_high;
    uint32_t pci_access_control_size_4;
    uint32_t pci_access_control_base_5_low;
    uint32_t pci_access_control_base_5_high;
    uint32_t pci_access_control_size_5;
    uint32_t pci_configuration_address;
    uint32_t pci_configuration_data;
    uint32_t pci_interrupt_acknowledge;
    uint32_t pci_serrn_mask;
    uint32_t pci_interrupt_cause;
    uint32_t pci_interrupt_mask;
    uint32_t pci_error_address_low;
    uint32_t pci_error_address_high;
    uint32_t pci_error_command;
    MemoryRegion mv88f5181l_pcie_interface_mmio;
    uint32_t pci_express_device_and_vendor_id_register;
    uint32_t pci_express_command_and_status_register;
    uint32_t pci_express_class_code_and_revision_id_register;
    uint32_t pci_express_bist_header_type_and_cache_line_size_register;
    uint32_t pci_express_bar0_internal_register;
    uint32_t pci_express_bar0_internal_high_register;
    uint32_t pci_express_bar1_register;
    uint32_t pci_express_bar1_high_register;
    uint32_t pci_express_bar2_register;
    uint32_t pci_express_bar2_high_register;
    uint32_t pci_express_subsystem_device_and_vendor_id;
    uint32_t pci_express_expansion_rom_bar_register;
    uint32_t pci_express_capability_list_pointer_register;
    uint32_t pci_express_interrupt_pin_and_line_register;
    uint32_t pci_express_power_management_capability_header_register;
    uint32_t pci_express_power_management_control_and_status_register;
    uint32_t pci_express_msi_message_control_register;
    uint32_t pci_express_msi_message_address_register;
    uint32_t pci_express_msi_message_address_high_register;
    uint32_t pci_express_msi_message_data_register;
    uint32_t pci_express_capability_register;
    uint32_t pci_express_device_capabilities_register;
    uint32_t pci_express_device_control_status_register;
    uint32_t pci_express_link_capabilities_register;
    uint32_t pci_express_link_control_status_register;
    uint32_t pci_express_advanced_error_report_header_register;
    uint32_t pci_express_uncorrectable_error_status_register;
    uint32_t pci_express_uncorrectable_error_mask_register;
    uint32_t pci_express_uncorrectable_error_severity_register;
    uint32_t pci_express_correctable_error_status_register;
    uint32_t pci_express_correctable_error_mask_register;
    uint32_t pci_express_advanced_error_capability_and_control_register;
    uint32_t pci_express_header_log_first_dword_register;
    uint32_t pci_express_header_log_second_dword_register;
    uint32_t pci_express_header_log_third_dword_register;
    uint32_t pci_express_header_log_fourth_dword_register;
    uint32_t pci_express_bar1_control_register;
    uint32_t pci_express_bar2_control_register;
    uint32_t pci_express_expansion_rom_bar_control_register;
    uint32_t pci_express_configuration_address_register;
    uint32_t pci_express_configuration_data_register;
    uint32_t pci_express_interrupt_cause;
    uint32_t pci_express_interrupt_mask;
    uint32_t pci_express_window0_control_register;
    uint32_t pci_express_window0_base_register;
    uint32_t pci_express_window0_remap_register;
    uint32_t pci_express_window1_control_register;
    uint32_t pci_express_window1_base_register;
    uint32_t pci_express_window1_remap_register;
    uint32_t pci_express_window2_control_register;
    uint32_t pci_express_window2_base_register;
    uint32_t pci_express_window2_remap_register;
    uint32_t pci_express_window3_control_register;
    uint32_t pci_express_window3_base_register;
    uint32_t pci_express_window3_remap_register;
    uint32_t pci_express_window4_control_register;
    uint32_t pci_express_window4_base_register;
    uint32_t pci_express_window4_remap_register;
    uint32_t pci_express_window5_control_register;
    uint32_t pci_express_window5_base_register;
    uint32_t pci_express_window5_remap_register;
    uint32_t pci_express_default_window_control_register;
    uint32_t pci_express_expansion_rom_window_control_register;
    uint32_t pci_express_expansion_rom_window_remap_register;
    uint32_t pci_express_control_register;
    uint32_t pci_express_status_register;
    uint32_t pci_express_completion_timeout_register;
    uint32_t pci_express_flow_control_register;
    uint32_t pci_express_acknowledge_timers_1x_register;
    uint32_t pci_express_debug_control_register;
    uint32_t pci_express_tl_control_register;
    MemoryRegion mv88f5181l_usb_2_0_controller_mmio;
    uint32_t port0_usb_2_0_id;
    uint32_t port0_usb_2_0_hwgeneral;
    uint32_t port0_usb_2_0_hwhost;
    uint32_t port0_usb_2_0_hwdevice;
    uint32_t port0_usb_2_0_hwtxbuf;
    uint32_t port0_usb_2_0_hwrxbuf;
    uint32_t port0_usb_2_0_hwtttxbuf;
    uint32_t port0_usb_2_0_hwttrxbuf;
    uint32_t port0_usb_2_0_caplength;
    uint32_t port0_usb_2_0_hciversion;
    uint32_t port0_usb_2_0_hcsparams;
    uint32_t port0_usb_2_0_hccparams;
    uint32_t port0_usb_2_0_dciversion;
    uint32_t port0_usb_2_0_dccparams;
    uint32_t port0_usb_2_0_usbcmd;
    uint32_t port0_usb_2_0_usbsts;
    uint32_t port0_usb_2_0_usbintr;
    uint32_t port0_usb_2_0_frindex;
    uint32_t port0_usb_2_0_periodiclistbase__or__device_addr;
    uint32_t port0_usb_2_0_asynclistaddr__or__endpointlist_addr;
    uint32_t port0_usb_2_0_ttctrl;
    uint32_t port0_usb_2_0_burstsize;
    uint32_t port0_usb_2_0_txfilltuning;
    uint32_t port0_usb_2_0_txttfilltuning;
    uint32_t port0_usb_2_0_configflag;
    uint32_t port0_usb_2_0_portsc1;
    uint32_t port0_usb_2_0_otgsc;
    uint32_t port0_usb_2_0_usbmode;
    uint32_t port0_usb_2_0_enpdtsetupstat;
    uint32_t port0_usb_2_0_endptprime;
    uint32_t port0_usb_2_0_endptflush;
    uint32_t port0_usb_2_0_endptstatus;
    uint32_t port0_usb_2_0_endptcomplete;
    uint32_t port0_usb_2_0_endptctrl0;
    uint32_t port0_usb_2_0_endptctrl1;
    uint32_t port0_usb_2_0_endptctrl2;
    uint32_t port0_usb_2_0_endptctrl3;
    uint32_t port0_usb_2_0_bridge_control_register;
    uint32_t port0_usb_2_0_bridge_interrupt_cause_register;
    uint32_t port0_usb_2_0_bridge_interrupt_mask_register;
    uint32_t port0_usb_2_0_bridge_error_address_register;
    uint32_t port0_usb_2_0_window0_control_register;
    uint32_t port0_usb_2_0_window0_base_register;
    uint32_t port0_usb_2_0_window1_control_register;
    uint32_t port0_usb_2_0_window1_base_register;
    uint32_t port0_usb_2_0_window2_control_register;
    uint32_t port0_usb_2_0_window2_base_register;
    uint32_t port0_usb_2_0_window3_control_register;
    uint32_t port0_usb_2_0_window3_base_register;
    uint32_t port0_usb_2_0_power_control_register;
    MemoryRegion mv88f5181l_gigabit_ethernet_controller_mmio;
    uint32_t phy_address;
    uint32_t smi;
    uint32_t ethernet_unit_default_address_euda;
    uint32_t ethernet_unit_default_id_eudid;
    uint32_t ethernet_unit_reserved_eu;
    uint32_t ethernet_unit_interrupt_cause_euic;
    uint32_t ethernet_unit_interrupt_mask_euim;
    uint32_t ethernet_unit_error_address_euea;
    uint32_t ethernet_unit_internal_address_error_euiae;
    uint32_t ethernet_unit_port_pads_calibration_eupcr;
    uint32_t ethernet_unit_control_euc;
    uint32_t base_address_0_ba0;
    uint32_t size_s_0_sr0;
    uint32_t base_address_1_ba1;
    uint32_t size_s_1_sr1;
    uint32_t base_address_2_ba2;
    uint32_t size_s_2_sr2;
    uint32_t base_address_3_ba3;
    uint32_t size_s_3_sr3;
    uint32_t base_address_4_ba4;
    uint32_t size_s_4_sr4;
    uint32_t base_address_5_ba5;
    uint32_t size_s_5_sr5;
    uint32_t high_address_remap_ha_harr0;
    uint32_t high_address_remap_ha_harr1;
    uint32_t high_address_remap_ha_harr2;
    uint32_t high_address_remap_ha_harr3;
    uint32_t base_address_enable_bare;
    uint32_t ethernet_port_access_protect_epap;
    uint32_t port_configuration_gec;
    uint32_t port_configuration_extend_gecx;
    uint32_t mii_serial_parameters;
    uint32_t gmii_serial_parameters;
    uint32_t vlan_ethertype_evlane;
    uint32_t mac_address_low_macal;
    uint32_t mac_address_high_macah;
    uint32_t sdma_configuration_sdc;
    uint32_t ip_differentiated_services_codepoint_0_to_priority_dscp0;
    uint32_t ip_differentiated_services_codepoint_1_to_priority_dscp1;
    uint32_t ip_differentiated_services_codepoint_2_to_priority_dscp2;
    uint32_t ip_differentiated_services_codepoint_23_to_priority_dscp3;
    uint32_t ip_differentiated_services_codepoint_24_to_priority_dscp4;
    uint32_t ip_differentiated_services_codepoint_25_to_priority_dscp5;
    uint32_t ip_differentiated_services_codepoint_6_to_priority_dscp6;
    uint32_t port_serial_control_psc;
    uint32_t vlan_priority_tag_to_priority_vpt2p;
    uint32_t ethernet_port_status_ps;
    uint32_t transmit_queue_command_tqc;
    uint32_t maximum_transmit_unit_mtu;
    uint32_t port_interrupt_cause_ic;
    uint32_t port_interrupt_cause_extend_ice;
    uint32_t port_interrupt_mask_pim;
    uint32_t port_extend_interrupt_mask_peim;
    uint32_t port_rx_fifo_urgent_threshold_prfut;
    uint32_t port_tx_fifo_urgent_threshold_ptfut;
    uint32_t port_rx_minimal_frame_size_pmfs;
    uint32_t port_rx_discard_frame_counter_gedfc;
    uint32_t port_overrun_frame_counter_pofc;
    uint32_t port_internal_address_error_euiae;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q0;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q1;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q2;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q3;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q4;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q5;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q6;
    uint32_t ethernet_current_receive_descriptor_pointers_crdp_q7;
    uint32_t receive_queue_command_rqc;
    uint32_t transmit_current_served_descriptor_pointer;
    uint32_t transmit_current_queue_descriptor_pointer_tcqdp_q0;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q0;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q0;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q0;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q1;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q1;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q1;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q2;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q2;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q2;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q3;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q3;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q3;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q4;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q4;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q4;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q5;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q5;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q5;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q6;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q6;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q6;
    uint32_t transmit_queue_token_bucket_counter_tqxtbc_q7;
    uint32_t transmit_queue_token_bucket_configuration_tqxtbc_q7;
    uint32_t transmit_queue_arbiter_configuration_tqxac_q7;
    uint32_t mac_mib_countersnterrupt_cause_register;
    uint32_t destination_address_filter_special_multicast_table_dfsmt;
    uint32_t destination_address_filter_other_multicast_table_dfut;
    uint32_t destination_address_filter_unicast_table_dfut;
    MemoryRegion mv88f5181l_cesa_mmio;
    uint32_t des_data_out_low_register;
    uint32_t des_data_out_high_register;
    uint32_t des_data_buffer_low_register;
    uint32_t des_data_buffer_high_register;
    uint32_t des_initial_value_low_register;
    uint32_t des_initial_value_high_register;
    uint32_t des_key0_low_register;
    uint32_t des_key0_high_register;
    uint32_t des_key1_low_register;
    uint32_t des_key1_high_register;
    uint32_t des_key2_low_register;
    uint32_t des_key2_high_register;
    uint32_t des_command_register;
    uint32_t sha_1_or_md5_data_in_register;
    uint32_t sha_1_or_md5_bit_count_low_register;
    uint32_t sha_1_or_md5_bit_count_high_register;
    uint32_t sha_1_or_md5_initial_value_or_digest_a_register;
    uint32_t sha_1_or_md5_initial_value_or_digest_b_register;
    uint32_t sha_1_or_md5_initial_value_or_digest_c_register;
    uint32_t sha_1_or_md5_initial_value_or_digest_d_register;
    uint32_t sha_1_initial_value_or_digest_e_register;
    uint32_t sha_1_or_md5_authentication_command_register;
    uint32_t aes_encryption_data_in_or_out_column_3_register;
    uint32_t aes_encryption_data_in_or_out_column_2_register;
    uint32_t aes_encryption_data_in_or_out_column_1_register;
    uint32_t aes_encryption_data_in_or_out_column_0_register;
    uint32_t aes_encryption_key_column_3_register;
    uint32_t aes_encryption_key_column_2_register;
    uint32_t aes_encryption_key_column_1_register;
    uint32_t aes_encryption_key_column_0_register;
    uint32_t aes_encryption_key_column_7_register;
    uint32_t aes_encryption_key_column_6_register;
    uint32_t aes_encryption_key_column_5_register;
    uint32_t aes_encryption_key_column_4_register;
    uint32_t aes_encryption_command_register;
    uint32_t aes_decryption_data_in_or_out_column_3_register;
    uint32_t aes_decryption_data_in_or_out_column_2_register;
    uint32_t aes_decryption_data_in_or_out_column_1_register;
    uint32_t aes_decryption_data_in_or_out_column_0_register;
    uint32_t aes_decryption_key_column_3_register;
    uint32_t aes_decryption_key_column_2_register;
    uint32_t aes_decryption_key_column_1_register;
    uint32_t aes_decryption_key_column_0_register;
    uint32_t aes_decryption_key_column_7_register;
    uint32_t aes_decryption_key_column_6_register;
    uint32_t aes_decryption_key_column_5_register;
    uint32_t aes_decryption_key_column_4_register;
    uint32_t aes_decryption_command_register;
    uint32_t security_accelerator_command_register;
    uint32_t security_accelerator_descriptor_pointer_session_0_register;
    uint32_t security_accelerator_descriptor_pointer_session_1_register;
    uint32_t security_accelerator_configuration_register;
    uint32_t security_accelerator_status_register;
    uint32_t cryptographic_engines_and_security_accelerator_interrupt_cause_register;
    uint32_t cryptographic_engines_and_security_accelerator_interrupt_mask_register;
    
    MV88F5181LICState ic;
    MV88F5181LTIMERState timer;
} MV88F5181LState;

#endif /* MV88F5181L_H */