/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "target/arm/cpu-qom.h"
#include "exec/address-spaces.h"
#include "hw/intc/mv88f5181l_ic.h"
#include "hw/arm/mv88f5181l_bridge.h"
#include "hw/timer/mv88f5181l_timer.h"
#include "hw/char/serial.h"
#include "sysemu/blockdev.h"
#include "hw/block/flash.h"
#include "hw/arm/arm.h"
#include "qemu/units.h"
#include "target/arm/cpu.h"
#include "hw/boards.h"

#define TYPE_WRT350N_V2 "wrt350n_v2"
#define WRT350N_V2(obj) \
    OBJECT_CHECK(WRT350NV2State, (obj), TYPE_WRT350N_V2)

typedef struct WRT350NV2State {
    ARMCPU *cpu;
    MemoryRegion ram;
    MV88F5181LICState ic;
    MV88F5181LBRIDGEState bridge;
    MV88F5181LTIMERState timer;
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
} WRT350NV2State;

static void mv88f5181l_gpio_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_gpio_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00:
        res = s->gpio_data_out_register;
        break;
    case 0x04:
        res = s->gpio_data_out_enable_control_register;
        break;
    case 0x08:
        res = s->gpio_blink_enable_register;
        break;
    case 0x0c:
        res = s->gpio_data_in_polarity_register;
        break;
    case 0x10:
        res = s->gpio_data_in_register;
        break;
    case 0x14:
        res = s->gpio_interrupt_cause_register;
        break;
    case 0x18:
        res = s->gpio_interrupt_mask_register;
        break;
    case 0x1c:
        res = s->gpio_interrupt_level_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00:
        s->gpio_data_out_register = val;
        break;
    case 0x04:
        s->gpio_data_out_enable_control_register = val;
        break;
    case 0x08:
        s->gpio_blink_enable_register = val;
        break;
    case 0x0c:
        s->gpio_data_in_polarity_register = val;
        break;
    case 0x10:
        s->gpio_data_in_register = val;
        break;
    case 0x14:
        s->gpio_interrupt_cause_register = val;
        break;
    case 0x18:
        s->gpio_interrupt_mask_register = val;
        break;
    case 0x1c:
        s->gpio_interrupt_level_mask_register = val;
        break;
    }
    mv88f5181l_gpio_update(s);
}

static const MemoryRegionOps mv88f5181l_gpio_ops = {
    .read = mv88f5181l_gpio_read,
    .write = mv88f5181l_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_cpu_address_map_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_cpu_address_map_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00:
        res = s->window0_control_register;
        break;
    case 0x04:
        res = s->window0_base_register;
        break;
    case 0x08:
        res = s->window0_remap_low_register;
        break;
    case 0x0C:
        res = s->window0_remap_high_register;
        break;
    case 0x10:
        res = s->window1_control_register;
        break;
    case 0x14:
        res = s->window1_base_register;
        break;
    case 0x18:
        res = s->window1_remap_low_register;
        break;
    case 0x1C:
        res = s->window1_remap_high_register;
        break;
    case 0x20:
        res = s->window2_control_register;
        break;
    case 0x24:
        res = s->window2_base_register;
        break;
    case 0x28:
        res = s->window2_remap_low_register;
        break;
    case 0x2C:
        res = s->window2_remap_high_register;
        break;
    case 0x30:
        res = s->window3_control_register;
        break;
    case 0x34:
        res = s->window3_base_register;
        break;
    case 0x40:
        res = s->window4_control_register;
        break;
    case 0x44:
        res = s->window4_base_register;
        break;
    case 0x50:
        res = s->window5_control_register;
        break;
    case 0x54:
        res = s->window5_base_register;
        break;
    case 0x60:
        res = s->window6_control_register;
        break;
    case 0x64:
        res = s->window6_base_register;
        break;
    case 0x70:
        res = s->window7_control_register;
        break;
    case 0x74:
        res = s->window7_base_register;
        break;
    case 0x80:
        res = s->_88f5181_internal_registers_base_address_register;
        break;
    }
    return res;
}

static void mv88f5181l_cpu_address_map_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00:
        s->window0_control_register = val;
        break;
    case 0x04:
        s->window0_base_register = val;
        break;
    case 0x08:
        s->window0_remap_low_register = val;
        break;
    case 0x0C:
        s->window0_remap_high_register = val;
        break;
    case 0x10:
        s->window1_control_register = val;
        break;
    case 0x14:
        s->window1_base_register = val;
        break;
    case 0x18:
        s->window1_remap_low_register = val;
        break;
    case 0x1C:
        s->window1_remap_high_register = val;
        break;
    case 0x20:
        s->window2_control_register = val;
        break;
    case 0x24:
        s->window2_base_register = val;
        break;
    case 0x28:
        s->window2_remap_low_register = val;
        break;
    case 0x2C:
        s->window2_remap_high_register = val;
        break;
    case 0x30:
        s->window3_control_register = val;
        break;
    case 0x34:
        s->window3_base_register = val;
        break;
    case 0x40:
        s->window4_control_register = val;
        break;
    case 0x44:
        s->window4_base_register = val;
        break;
    case 0x50:
        s->window5_control_register = val;
        break;
    case 0x54:
        s->window5_base_register = val;
        break;
    case 0x60:
        s->window6_control_register = val;
        break;
    case 0x64:
        s->window6_base_register = val;
        break;
    case 0x70:
        s->window7_control_register = val;
        break;
    case 0x74:
        s->window7_base_register = val;
        break;
    case 0x80:
        s->_88f5181_internal_registers_base_address_register = val;
        break;
    }
    mv88f5181l_cpu_address_map_update(s);
}

static const MemoryRegionOps mv88f5181l_cpu_address_map_ops = {
    .read = mv88f5181l_cpu_address_map_read,
    .write = mv88f5181l_cpu_address_map_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_ddr_sdram_controller_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_ddr_sdram_controller_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x100:
        res = s->cs0n_base_address_register;
        break;
    case 0x104:
        res = s->cs0n_size_register;
        break;
    case 0x108:
        res = s->cs1n_base_address_register;
        break;
    case 0x10C:
        res = s->cs1n_size_register;
        break;
    case 0x110:
        res = s->cs2n_base_address_register;
        break;
    case 0x114:
        res = s->cs2n_size_register;
        break;
    case 0x118:
        res = s->cs3n_base_address_register;
        break;
    case 0x11C:
        res = s->cs3n_size_register;
        break;
    case 0x00:
        res = s->ddr_sdram_configuration_register;
        break;
    case 0x04:
        res = s->ddr_sdram_control_register;
        break;
    case 0x08:
        res = s->ddr_sdram_timing_low_register;
        break;
    case 0x0C:
        res = s->ddr_sdram_timing_high_register;
        break;
    case 0x28:
        res = s->ddr2_sdram_timing_low_register;
        break;
    case 0x7C:
        res = s->ddr2_sdram_timing_high_register;
        break;
    case 0x10:
        res = s->ddr_sdram_address_control_register;
        break;
    case 0x14:
        res = s->ddr_sdram_open_pages_control_register;
        break;
    case 0x18:
        res = s->ddr_sdram_operation_register;
        break;
    case 0x2C:
        res = s->ddr_sdram_operation_control_register;
        break;
    case 0x1C:
        res = s->ddr_sdram_mode_register;
        break;
    case 0x20:
        res = s->extended_ddr_sdram_mode_register;
        break;
    case 0x80:
        res = s->ddr_sdram_initialization_control_register;
        break;
    case 0xC0:
        res = s->ddr_sdram_address_or_control_pads_calibration_register;
        break;
    case 0xC4:
        res = s->ddr_sdram_data_pads_calibration_register;
        break;
    case 0x94:
        res = s->ddr2_sdram_odt_control_low_register;
        break;
    case 0x98:
        res = s->ddr2_sdram_odt_control_high_register;
        break;
    case 0x9C:
        res = s->ddr2_sdram_odt_control_register;
        break;
    case 0x30:
        res = s->ddr_sdram_interface_mbus_control_low_register;
        break;
    case 0x34:
        res = s->ddr_sdram_interface_mbus_control_high_register;
        break;
    case 0x38:
        res = s->ddr_sdram_interface_mbus_timeout_register;
        break;
    case 0xB0:
        res = s->ddr_sdram_mmask_register;
        break;
    }
    return res;
}

static void mv88f5181l_ddr_sdram_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x100:
        s->cs0n_base_address_register = val;
        break;
    case 0x104:
        s->cs0n_size_register = val;
        break;
    case 0x108:
        s->cs1n_base_address_register = val;
        break;
    case 0x10C:
        s->cs1n_size_register = val;
        break;
    case 0x110:
        s->cs2n_base_address_register = val;
        break;
    case 0x114:
        s->cs2n_size_register = val;
        break;
    case 0x118:
        s->cs3n_base_address_register = val;
        break;
    case 0x11C:
        s->cs3n_size_register = val;
        break;
    case 0x00:
        s->ddr_sdram_configuration_register = val;
        break;
    case 0x04:
        s->ddr_sdram_control_register = val;
        break;
    case 0x08:
        s->ddr_sdram_timing_low_register = val;
        break;
    case 0x0C:
        s->ddr_sdram_timing_high_register = val;
        break;
    case 0x28:
        s->ddr2_sdram_timing_low_register = val;
        break;
    case 0x7C:
        s->ddr2_sdram_timing_high_register = val;
        break;
    case 0x10:
        s->ddr_sdram_address_control_register = val;
        break;
    case 0x14:
        s->ddr_sdram_open_pages_control_register = val;
        break;
    case 0x18:
        s->ddr_sdram_operation_register = val;
        break;
    case 0x2C:
        s->ddr_sdram_operation_control_register = val;
        break;
    case 0x1C:
        s->ddr_sdram_mode_register = val;
        break;
    case 0x20:
        s->extended_ddr_sdram_mode_register = val;
        break;
    case 0x80:
        s->ddr_sdram_initialization_control_register = val;
        break;
    case 0xC0:
        s->ddr_sdram_address_or_control_pads_calibration_register = val;
        break;
    case 0xC4:
        s->ddr_sdram_data_pads_calibration_register = val;
        break;
    case 0x94:
        s->ddr2_sdram_odt_control_low_register = val;
        break;
    case 0x98:
        s->ddr2_sdram_odt_control_high_register = val;
        break;
    case 0x9C:
        s->ddr2_sdram_odt_control_register = val;
        break;
    case 0x30:
        s->ddr_sdram_interface_mbus_control_low_register = val;
        break;
    case 0x34:
        s->ddr_sdram_interface_mbus_control_high_register = val;
        break;
    case 0x38:
        s->ddr_sdram_interface_mbus_timeout_register = val;
        break;
    case 0xB0:
        s->ddr_sdram_mmask_register = val;
        break;
    }
    mv88f5181l_ddr_sdram_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_ddr_sdram_controller_ops = {
    .read = mv88f5181l_ddr_sdram_controller_read,
    .write = mv88f5181l_ddr_sdram_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pins_multiplexing_interface_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_pins_multiplexing_interface_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00:
        res = s->mpp_control_0_register;
        break;
    case 0x04:
        res = s->mpp_control_1_register;
        break;
    case 0x50:
        res = s->mpp_control_2_register;
        break;
    case 0x08:
        res = s->device_multiplex_control_register;
        break;
    case 0x10:
        res = s->sample_at_reset_register;
        break;
    }
    return res;
}

static void mv88f5181l_pins_multiplexing_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00:
        s->mpp_control_0_register = val;
        break;
    case 0x04:
        s->mpp_control_1_register = val;
        break;
    case 0x50:
        s->mpp_control_2_register = val;
        break;
    case 0x08:
        s->device_multiplex_control_register = val;
        break;
    case 0x10:
        s->sample_at_reset_register = val;
        break;
    }
    mv88f5181l_pins_multiplexing_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pins_multiplexing_interface_ops = {
    .read = mv88f5181l_pins_multiplexing_interface_read,
    .write = mv88f5181l_pins_multiplexing_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pci_interface_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_pci_interface_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0c08:
        res = s->csn0_bar_size;
        break;
    case 0x0d08:
        res = s->csn1_bar_size;
        break;
    case 0x0c0c:
        res = s->csn2_bar_size;
        break;
    case 0x0d0c:
        res = s->csn3_bar_size;
        break;
    case 0x0c10:
        res = s->devcsn0_bar_size;
        break;
    case 0x0d10:
        res = s->devcsn1_bar_size;
        break;
    case 0x0d18:
        res = s->devcsn2_bar_size;
        break;
    case 0x0d14:
        res = s->boot_csn_bar_size;
        break;
    case 0x0d1c:
        res = s->p2p_mem0_bar_size;
        break;
    case 0x0d24:
        res = s->p2p_i_or_o_bar_size;
        break;
    case 0x0d2c:
        res = s->expansion_rom_bar_size;
        break;
    case 0x0c3c:
        res = s->base_address_registers_enable;
        break;
    case 0x0c48:
        res = s->csn0_base_address_remap;
        break;
    case 0x0d48:
        res = s->csn1_base_address_remap;
        break;
    case 0x0c4c:
        res = s->csn2_base_address_remap;
        break;
    case 0x0d4c:
        res = s->csn3_base_address_remap;
        break;
    case 0x0c50:
        res = s->devcsn0_base_address_remap;
        break;
    case 0x0d50:
        res = s->devcsn1_base_address_remap;
        break;
    case 0x0d58:
        res = s->devcsn2_base_address_remap;
        break;
    case 0x0d54:
        res = s->bootcsn_base_address_remap;
        break;
    case 0x0d5c:
        res = s->p2p_mem0_base_address_remap_low;
        break;
    case 0x0d60:
        res = s->p2p_mem0_base_address_remap_high;
        break;
    case 0x0d6c:
        res = s->p2p_i_or_o_base_address_remap;
        break;
    case 0x0f38:
        res = s->expansion_rom_base_address_remap;
        break;
    case 0x0c1c:
        res = s->dram_bar_bank_select;
        break;
    case 0x0d3c:
        res = s->pci_address_decode_control;
        break;
    case 0x1d20:
        res = s->pci_dll_control;
        break;
    case 0x1d1c:
        res = s->pci_or_mpp_pads_calibration;
        break;
    case 0x0c00:
        res = s->pci_command;
        break;
    case 0x0d00:
        res = s->pci_mode;
        break;
    case 0x0c04:
        res = s->pci_retry;
        break;
    case 0x0d04:
        res = s->pci_discard_timer;
        break;
    case 0x0c38:
        res = s->msi_trigger_timer;
        break;
    case 0x1d00:
        res = s->pci_arbiter_control;
        break;
    case 0x1d14:
        res = s->pci_p2p_configuration;
        break;
    case 0x1e00:
        res = s->pci_access_control_base_0_low;
        break;
    case 0x1e04:
        res = s->pci_access_control_base_0_high;
        break;
    case 0x1e08:
        res = s->pci_access_control_size_0;
        break;
    case 0x1e10:
        res = s->pci_access_control_base_1_low;
        break;
    case 0x1e14:
        res = s->pci_access_control_base_1_high;
        break;
    case 0x1e18:
        res = s->pci_access_control_size_1;
        break;
    case 0x1e20:
        res = s->pci_access_control_base_2_low;
        break;
    case 0x1e24:
        res = s->pci_access_control_base_2_high;
        break;
    case 0x1e28:
        res = s->pci_access_control_size_2;
        break;
    case 0x1e30:
        res = s->pci_access_control_base_3_low;
        break;
    case 0x1e34:
        res = s->pci_access_control_base_3_high;
        break;
    case 0x1e38:
        res = s->pci_access_control_size_3;
        break;
    case 0x1e40:
        res = s->pci_access_control_base_4_low;
        break;
    case 0x1e44:
        res = s->pci_access_control_base_4_high;
        break;
    case 0x1e48:
        res = s->pci_access_control_size_4;
        break;
    case 0x1e50:
        res = s->pci_access_control_base_5_low;
        break;
    case 0x1e54:
        res = s->pci_access_control_base_5_high;
        break;
    case 0x1e58:
        res = s->pci_access_control_size_5;
        break;
    case 0x0c78:
        res = s->pci_configuration_address;
        break;
    case 0x0c7c:
        res = s->pci_configuration_data;
        break;
    case 0x0c34:
        res = s->pci_interrupt_acknowledge;
        break;
    case 0x0c28:
        res = s->pci_serrn_mask;
        break;
    case 0x1d58:
        res = s->pci_interrupt_cause;
        break;
    case 0x1d5c:
        res = s->pci_interrupt_mask;
        break;
    case 0x1d40:
        res = s->pci_error_address_low;
        break;
    case 0x1d44:
        res = s->pci_error_address_high;
        break;
    case 0x1d50:
        res = s->pci_error_command;
        break;
    }
    return res;
}

static void mv88f5181l_pci_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0c08:
        s->csn0_bar_size = val;
        break;
    case 0x0d08:
        s->csn1_bar_size = val;
        break;
    case 0x0c0c:
        s->csn2_bar_size = val;
        break;
    case 0x0d0c:
        s->csn3_bar_size = val;
        break;
    case 0x0c10:
        s->devcsn0_bar_size = val;
        break;
    case 0x0d10:
        s->devcsn1_bar_size = val;
        break;
    case 0x0d18:
        s->devcsn2_bar_size = val;
        break;
    case 0x0d14:
        s->boot_csn_bar_size = val;
        break;
    case 0x0d1c:
        s->p2p_mem0_bar_size = val;
        break;
    case 0x0d24:
        s->p2p_i_or_o_bar_size = val;
        break;
    case 0x0d2c:
        s->expansion_rom_bar_size = val;
        break;
    case 0x0c3c:
        s->base_address_registers_enable = val;
        break;
    case 0x0c48:
        s->csn0_base_address_remap = val;
        break;
    case 0x0d48:
        s->csn1_base_address_remap = val;
        break;
    case 0x0c4c:
        s->csn2_base_address_remap = val;
        break;
    case 0x0d4c:
        s->csn3_base_address_remap = val;
        break;
    case 0x0c50:
        s->devcsn0_base_address_remap = val;
        break;
    case 0x0d50:
        s->devcsn1_base_address_remap = val;
        break;
    case 0x0d58:
        s->devcsn2_base_address_remap = val;
        break;
    case 0x0d54:
        s->bootcsn_base_address_remap = val;
        break;
    case 0x0d5c:
        s->p2p_mem0_base_address_remap_low = val;
        break;
    case 0x0d60:
        s->p2p_mem0_base_address_remap_high = val;
        break;
    case 0x0d6c:
        s->p2p_i_or_o_base_address_remap = val;
        break;
    case 0x0f38:
        s->expansion_rom_base_address_remap = val;
        break;
    case 0x0c1c:
        s->dram_bar_bank_select = val;
        break;
    case 0x0d3c:
        s->pci_address_decode_control = val;
        break;
    case 0x1d20:
        s->pci_dll_control = val;
        break;
    case 0x1d1c:
        s->pci_or_mpp_pads_calibration = val;
        break;
    case 0x0c00:
        s->pci_command = val;
        break;
    case 0x0d00:
        s->pci_mode = val;
        break;
    case 0x0c04:
        s->pci_retry = val;
        break;
    case 0x0d04:
        s->pci_discard_timer = val;
        break;
    case 0x0c38:
        s->msi_trigger_timer = val;
        break;
    case 0x1d00:
        s->pci_arbiter_control = val;
        break;
    case 0x1d14:
        s->pci_p2p_configuration = val;
        break;
    case 0x1e00:
        s->pci_access_control_base_0_low = val;
        break;
    case 0x1e04:
        s->pci_access_control_base_0_high = val;
        break;
    case 0x1e08:
        s->pci_access_control_size_0 = val;
        break;
    case 0x1e10:
        s->pci_access_control_base_1_low = val;
        break;
    case 0x1e14:
        s->pci_access_control_base_1_high = val;
        break;
    case 0x1e18:
        s->pci_access_control_size_1 = val;
        break;
    case 0x1e20:
        s->pci_access_control_base_2_low = val;
        break;
    case 0x1e24:
        s->pci_access_control_base_2_high = val;
        break;
    case 0x1e28:
        s->pci_access_control_size_2 = val;
        break;
    case 0x1e30:
        s->pci_access_control_base_3_low = val;
        break;
    case 0x1e34:
        s->pci_access_control_base_3_high = val;
        break;
    case 0x1e38:
        s->pci_access_control_size_3 = val;
        break;
    case 0x1e40:
        s->pci_access_control_base_4_low = val;
        break;
    case 0x1e44:
        s->pci_access_control_base_4_high = val;
        break;
    case 0x1e48:
        s->pci_access_control_size_4 = val;
        break;
    case 0x1e50:
        s->pci_access_control_base_5_low = val;
        break;
    case 0x1e54:
        s->pci_access_control_base_5_high = val;
        break;
    case 0x1e58:
        s->pci_access_control_size_5 = val;
        break;
    case 0x0c78:
        s->pci_configuration_address = val;
        break;
    case 0x0c7c:
        s->pci_configuration_data = val;
        break;
    case 0x0c34:
        s->pci_interrupt_acknowledge = val;
        break;
    case 0x0c28:
        s->pci_serrn_mask = val;
        break;
    case 0x1d58:
        s->pci_interrupt_cause = val;
        break;
    case 0x1d5c:
        s->pci_interrupt_mask = val;
        break;
    case 0x1d40:
        s->pci_error_address_low = val;
        break;
    case 0x1d44:
        s->pci_error_address_high = val;
        break;
    case 0x1d50:
        s->pci_error_command = val;
        break;
    }
    mv88f5181l_pci_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pci_interface_ops = {
    .read = mv88f5181l_pci_interface_read,
    .write = mv88f5181l_pci_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_pcie_interface_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_pcie_interface_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x0000:
        res = s->pci_express_device_and_vendor_id_register;
        break;
    case 0x0004:
        res = s->pci_express_command_and_status_register;
        break;
    case 0x0008:
        res = s->pci_express_class_code_and_revision_id_register;
        break;
    case 0x000c:
        res = s->pci_express_bist_header_type_and_cache_line_size_register;
        break;
    case 0x0010:
        res = s->pci_express_bar0_internal_register;
        break;
    case 0x0014:
        res = s->pci_express_bar0_internal_high_register;
        break;
    case 0x0018:
        res = s->pci_express_bar1_register;
        break;
    case 0x001c:
        res = s->pci_express_bar1_high_register;
        break;
    case 0x0020:
        res = s->pci_express_bar2_register;
        break;
    case 0x0024:
        res = s->pci_express_bar2_high_register;
        break;
    case 0x002c:
        res = s->pci_express_subsystem_device_and_vendor_id;
        break;
    case 0x0030:
        res = s->pci_express_expansion_rom_bar_register;
        break;
    case 0x0034:
        res = s->pci_express_capability_list_pointer_register;
        break;
    case 0x003c:
        res = s->pci_express_interrupt_pin_and_line_register;
        break;
    case 0x0040:
        res = s->pci_express_power_management_capability_header_register;
        break;
    case 0x0044:
        res = s->pci_express_power_management_control_and_status_register;
        break;
    case 0x0050:
        res = s->pci_express_msi_message_control_register;
        break;
    case 0x0054:
        res = s->pci_express_msi_message_address_register;
        break;
    case 0x0058:
        res = s->pci_express_msi_message_address_high_register;
        break;
    case 0x005c:
        res = s->pci_express_msi_message_data_register;
        break;
    case 0x0060:
        res = s->pci_express_capability_register;
        break;
    case 0x0064:
        res = s->pci_express_device_capabilities_register;
        break;
    case 0x0068:
        res = s->pci_express_device_control_status_register;
        break;
    case 0x006c:
        res = s->pci_express_link_capabilities_register;
        break;
    case 0x0070:
        res = s->pci_express_link_control_status_register;
        break;
    case 0x0100:
        res = s->pci_express_advanced_error_report_header_register;
        break;
    case 0x0104:
        res = s->pci_express_uncorrectable_error_status_register;
        break;
    case 0x0108:
        res = s->pci_express_uncorrectable_error_mask_register;
        break;
    case 0x010c:
        res = s->pci_express_uncorrectable_error_severity_register;
        break;
    case 0x0110:
        res = s->pci_express_correctable_error_status_register;
        break;
    case 0x0114:
        res = s->pci_express_correctable_error_mask_register;
        break;
    case 0x0118:
        res = s->pci_express_advanced_error_capability_and_control_register;
        break;
    case 0x011c:
        res = s->pci_express_header_log_first_dword_register;
        break;
    case 0x0120:
        res = s->pci_express_header_log_second_dword_register;
        break;
    case 0x0124:
        res = s->pci_express_header_log_third_dword_register;
        break;
    case 0x0128:
        res = s->pci_express_header_log_fourth_dword_register;
        break;
    case 0x1804:
        res = s->pci_express_bar1_control_register;
        break;
    case 0x1808:
        res = s->pci_express_bar2_control_register;
        break;
    case 0x180c:
        res = s->pci_express_expansion_rom_bar_control_register;
        break;
    case 0x18f8:
        res = s->pci_express_configuration_address_register;
        break;
    case 0x18fc:
        res = s->pci_express_configuration_data_register;
        break;
    case 0x1900:
        res = s->pci_express_interrupt_cause;
        break;
    case 0x1910:
        res = s->pci_express_interrupt_mask;
        break;
    case 0x1820:
        res = s->pci_express_window0_control_register;
        break;
    case 0x1824:
        res = s->pci_express_window0_base_register;
        break;
    case 0x182c:
        res = s->pci_express_window0_remap_register;
        break;
    case 0x1830:
        res = s->pci_express_window1_control_register;
        break;
    case 0x1834:
        res = s->pci_express_window1_base_register;
        break;
    case 0x183c:
        res = s->pci_express_window1_remap_register;
        break;
    case 0x1840:
        res = s->pci_express_window2_control_register;
        break;
    case 0x1844:
        res = s->pci_express_window2_base_register;
        break;
    case 0x184c:
        res = s->pci_express_window2_remap_register;
        break;
    case 0x1850:
        res = s->pci_express_window3_control_register;
        break;
    case 0x1854:
        res = s->pci_express_window3_base_register;
        break;
    case 0x185c:
        res = s->pci_express_window3_remap_register;
        break;
    case 0x1860:
        res = s->pci_express_window4_control_register;
        break;
    case 0x1864:
        res = s->pci_express_window4_base_register;
        break;
    case 0x186c:
        res = s->pci_express_window4_remap_register;
        break;
    case 0x1880:
        res = s->pci_express_window5_control_register;
        break;
    case 0x1884:
        res = s->pci_express_window5_base_register;
        break;
    case 0x188c:
        res = s->pci_express_window5_remap_register;
        break;
    case 0x18b0:
        res = s->pci_express_default_window_control_register;
        break;
    case 0x18c0:
        res = s->pci_express_expansion_rom_window_control_register;
        break;
    case 0x18c4:
        res = s->pci_express_expansion_rom_window_remap_register;
        break;
    case 0x1a00:
        res = s->pci_express_control_register;
        break;
    case 0x1a04:
        res = s->pci_express_status_register;
        break;
    case 0x1a10:
        res = s->pci_express_completion_timeout_register;
        break;
    case 0x1a20:
        res = s->pci_express_flow_control_register;
        break;
    case 0x1a40:
        res = s->pci_express_acknowledge_timers_1x_register;
        break;
    case 0x1a60:
        res = s->pci_express_debug_control_register;
        break;
    case 0x1ab0:
        res = s->pci_express_tl_control_register;
        break;
    }
    return res;
}

static void mv88f5181l_pcie_interface_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x0000:
        s->pci_express_device_and_vendor_id_register = val;
        break;
    case 0x0004:
        s->pci_express_command_and_status_register = val;
        break;
    case 0x0008:
        s->pci_express_class_code_and_revision_id_register = val;
        break;
    case 0x000c:
        s->pci_express_bist_header_type_and_cache_line_size_register = val;
        break;
    case 0x0010:
        s->pci_express_bar0_internal_register = val;
        break;
    case 0x0014:
        s->pci_express_bar0_internal_high_register = val;
        break;
    case 0x0018:
        s->pci_express_bar1_register = val;
        break;
    case 0x001c:
        s->pci_express_bar1_high_register = val;
        break;
    case 0x0020:
        s->pci_express_bar2_register = val;
        break;
    case 0x0024:
        s->pci_express_bar2_high_register = val;
        break;
    case 0x002c:
        s->pci_express_subsystem_device_and_vendor_id = val;
        break;
    case 0x0030:
        s->pci_express_expansion_rom_bar_register = val;
        break;
    case 0x0034:
        s->pci_express_capability_list_pointer_register = val;
        break;
    case 0x003c:
        s->pci_express_interrupt_pin_and_line_register = val;
        break;
    case 0x0040:
        s->pci_express_power_management_capability_header_register = val;
        break;
    case 0x0044:
        s->pci_express_power_management_control_and_status_register = val;
        break;
    case 0x0050:
        s->pci_express_msi_message_control_register = val;
        break;
    case 0x0054:
        s->pci_express_msi_message_address_register = val;
        break;
    case 0x0058:
        s->pci_express_msi_message_address_high_register = val;
        break;
    case 0x005c:
        s->pci_express_msi_message_data_register = val;
        break;
    case 0x0060:
        s->pci_express_capability_register = val;
        break;
    case 0x0064:
        s->pci_express_device_capabilities_register = val;
        break;
    case 0x0068:
        s->pci_express_device_control_status_register = val;
        break;
    case 0x006c:
        s->pci_express_link_capabilities_register = val;
        break;
    case 0x0070:
        s->pci_express_link_control_status_register = val;
        break;
    case 0x0100:
        s->pci_express_advanced_error_report_header_register = val;
        break;
    case 0x0104:
        s->pci_express_uncorrectable_error_status_register = val;
        break;
    case 0x0108:
        s->pci_express_uncorrectable_error_mask_register = val;
        break;
    case 0x010c:
        s->pci_express_uncorrectable_error_severity_register = val;
        break;
    case 0x0110:
        s->pci_express_correctable_error_status_register = val;
        break;
    case 0x0114:
        s->pci_express_correctable_error_mask_register = val;
        break;
    case 0x0118:
        s->pci_express_advanced_error_capability_and_control_register = val;
        break;
    case 0x011c:
        s->pci_express_header_log_first_dword_register = val;
        break;
    case 0x0120:
        s->pci_express_header_log_second_dword_register = val;
        break;
    case 0x0124:
        s->pci_express_header_log_third_dword_register = val;
        break;
    case 0x0128:
        s->pci_express_header_log_fourth_dword_register = val;
        break;
    case 0x1804:
        s->pci_express_bar1_control_register = val;
        break;
    case 0x1808:
        s->pci_express_bar2_control_register = val;
        break;
    case 0x180c:
        s->pci_express_expansion_rom_bar_control_register = val;
        break;
    case 0x18f8:
        s->pci_express_configuration_address_register = val;
        break;
    case 0x18fc:
        s->pci_express_configuration_data_register = val;
        break;
    case 0x1900:
        s->pci_express_interrupt_cause = val;
        break;
    case 0x1910:
        s->pci_express_interrupt_mask = val;
        break;
    case 0x1820:
        s->pci_express_window0_control_register = val;
        break;
    case 0x1824:
        s->pci_express_window0_base_register = val;
        break;
    case 0x182c:
        s->pci_express_window0_remap_register = val;
        break;
    case 0x1830:
        s->pci_express_window1_control_register = val;
        break;
    case 0x1834:
        s->pci_express_window1_base_register = val;
        break;
    case 0x183c:
        s->pci_express_window1_remap_register = val;
        break;
    case 0x1840:
        s->pci_express_window2_control_register = val;
        break;
    case 0x1844:
        s->pci_express_window2_base_register = val;
        break;
    case 0x184c:
        s->pci_express_window2_remap_register = val;
        break;
    case 0x1850:
        s->pci_express_window3_control_register = val;
        break;
    case 0x1854:
        s->pci_express_window3_base_register = val;
        break;
    case 0x185c:
        s->pci_express_window3_remap_register = val;
        break;
    case 0x1860:
        s->pci_express_window4_control_register = val;
        break;
    case 0x1864:
        s->pci_express_window4_base_register = val;
        break;
    case 0x186c:
        s->pci_express_window4_remap_register = val;
        break;
    case 0x1880:
        s->pci_express_window5_control_register = val;
        break;
    case 0x1884:
        s->pci_express_window5_base_register = val;
        break;
    case 0x188c:
        s->pci_express_window5_remap_register = val;
        break;
    case 0x18b0:
        s->pci_express_default_window_control_register = val;
        break;
    case 0x18c0:
        s->pci_express_expansion_rom_window_control_register = val;
        break;
    case 0x18c4:
        s->pci_express_expansion_rom_window_remap_register = val;
        break;
    case 0x1a00:
        s->pci_express_control_register = val;
        break;
    case 0x1a04:
        s->pci_express_status_register = val;
        break;
    case 0x1a10:
        s->pci_express_completion_timeout_register = val;
        break;
    case 0x1a20:
        s->pci_express_flow_control_register = val;
        break;
    case 0x1a40:
        s->pci_express_acknowledge_timers_1x_register = val;
        break;
    case 0x1a60:
        s->pci_express_debug_control_register = val;
        break;
    case 0x1ab0:
        s->pci_express_tl_control_register = val;
        break;
    }
    mv88f5181l_pcie_interface_update(s);
}

static const MemoryRegionOps mv88f5181l_pcie_interface_ops = {
    .read = mv88f5181l_pcie_interface_read,
    .write = mv88f5181l_pcie_interface_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_usb_2_0_controller_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_usb_2_0_controller_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00:
        res = s->port0_usb_2_0_id;
        break;
    case 0x04:
        res = s->port0_usb_2_0_hwgeneral;
        break;
    case 0x08:
        res = s->port0_usb_2_0_hwhost;
        break;
    case 0x0c:
        res = s->port0_usb_2_0_hwdevice;
        break;
    case 0x10:
        res = s->port0_usb_2_0_hwtxbuf;
        break;
    case 0x14:
        res = s->port0_usb_2_0_hwrxbuf;
        break;
    case 0x18:
        res = s->port0_usb_2_0_hwtttxbuf;
        break;
    case 0x1c:
        res = s->port0_usb_2_0_hwttrxbuf;
        break;
    case 0x100:
        res = s->port0_usb_2_0_caplength;
        break;
    case 0x102:
        res = s->port0_usb_2_0_hciversion;
        break;
    case 0x104:
        res = s->port0_usb_2_0_hcsparams;
        break;
    case 0x108:
        res = s->port0_usb_2_0_hccparams;
        break;
    case 0x120:
        res = s->port0_usb_2_0_dciversion;
        break;
    case 0x124:
        res = s->port0_usb_2_0_dccparams;
        break;
    case 0x140:
        res = s->port0_usb_2_0_usbcmd;
        break;
    case 0x144:
        res = s->port0_usb_2_0_usbsts;
        break;
    case 0x148:
        res = s->port0_usb_2_0_usbintr;
        break;
    case 0x14c:
        res = s->port0_usb_2_0_frindex;
        break;
    case 0x154:
        res = s->port0_usb_2_0_periodiclistbase__or__device_addr;
        break;
    case 0x158:
        res = s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr;
        break;
    case 0x15c:
        res = s->port0_usb_2_0_ttctrl;
        break;
    case 0x160:
        res = s->port0_usb_2_0_burstsize;
        break;
    case 0x164:
        res = s->port0_usb_2_0_txfilltuning;
        break;
    case 0x168:
        res = s->port0_usb_2_0_txttfilltuning;
        break;
    case 0x180:
        res = s->port0_usb_2_0_configflag;
        break;
    case 0x184:
        res = s->port0_usb_2_0_portsc1;
        break;
    case 0x1a4:
        res = s->port0_usb_2_0_otgsc;
        break;
    case 0x1a8:
        res = s->port0_usb_2_0_usbmode;
        break;
    case 0x1ac:
        res = s->port0_usb_2_0_enpdtsetupstat;
        break;
    case 0x1b0:
        res = s->port0_usb_2_0_endptprime;
        break;
    case 0x1b4:
        res = s->port0_usb_2_0_endptflush;
        break;
    case 0x1b8:
        res = s->port0_usb_2_0_endptstatus;
        break;
    case 0x1bc:
        res = s->port0_usb_2_0_endptcomplete;
        break;
    case 0x1c0:
        res = s->port0_usb_2_0_endptctrl0;
        break;
    case 0x1c4:
        res = s->port0_usb_2_0_endptctrl1;
        break;
    case 0x1c8:
        res = s->port0_usb_2_0_endptctrl2;
        break;
    case 0x1cc:
        res = s->port0_usb_2_0_endptctrl3;
        break;
    case 0x300:
        res = s->port0_usb_2_0_bridge_control_register;
        break;
    case 0x310:
        res = s->port0_usb_2_0_bridge_interrupt_cause_register;
        break;
    case 0x314:
        res = s->port0_usb_2_0_bridge_interrupt_mask_register;
        break;
    case 0x31c:
        res = s->port0_usb_2_0_bridge_error_address_register;
        break;
    case 0x320:
        res = s->port0_usb_2_0_window0_control_register;
        break;
    case 0x324:
        res = s->port0_usb_2_0_window0_base_register;
        break;
    case 0x330:
        res = s->port0_usb_2_0_window1_control_register;
        break;
    case 0x334:
        res = s->port0_usb_2_0_window1_base_register;
        break;
    case 0x340:
        res = s->port0_usb_2_0_window2_control_register;
        break;
    case 0x344:
        res = s->port0_usb_2_0_window2_base_register;
        break;
    case 0x350:
        res = s->port0_usb_2_0_window3_control_register;
        break;
    case 0x354:
        res = s->port0_usb_2_0_window3_base_register;
        break;
    case 0x400:
        res = s->port0_usb_2_0_power_control_register;
        break;
    }
    return res;
}

static void mv88f5181l_usb_2_0_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00:
        s->port0_usb_2_0_id = val;
        break;
    case 0x04:
        s->port0_usb_2_0_hwgeneral = val;
        break;
    case 0x08:
        s->port0_usb_2_0_hwhost = val;
        break;
    case 0x0c:
        s->port0_usb_2_0_hwdevice = val;
        break;
    case 0x10:
        s->port0_usb_2_0_hwtxbuf = val;
        break;
    case 0x14:
        s->port0_usb_2_0_hwrxbuf = val;
        break;
    case 0x18:
        s->port0_usb_2_0_hwtttxbuf = val;
        break;
    case 0x1c:
        s->port0_usb_2_0_hwttrxbuf = val;
        break;
    case 0x100:
        s->port0_usb_2_0_caplength = val;
        break;
    case 0x102:
        s->port0_usb_2_0_hciversion = val;
        break;
    case 0x104:
        s->port0_usb_2_0_hcsparams = val;
        break;
    case 0x108:
        s->port0_usb_2_0_hccparams = val;
        break;
    case 0x120:
        s->port0_usb_2_0_dciversion = val;
        break;
    case 0x124:
        s->port0_usb_2_0_dccparams = val;
        break;
    case 0x140:
        s->port0_usb_2_0_usbcmd = val;
        break;
    case 0x144:
        s->port0_usb_2_0_usbsts = val;
        break;
    case 0x148:
        s->port0_usb_2_0_usbintr = val;
        break;
    case 0x14c:
        s->port0_usb_2_0_frindex = val;
        break;
    case 0x154:
        s->port0_usb_2_0_periodiclistbase__or__device_addr = val;
        break;
    case 0x158:
        s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr = val;
        break;
    case 0x15c:
        s->port0_usb_2_0_ttctrl = val;
        break;
    case 0x160:
        s->port0_usb_2_0_burstsize = val;
        break;
    case 0x164:
        s->port0_usb_2_0_txfilltuning = val;
        break;
    case 0x168:
        s->port0_usb_2_0_txttfilltuning = val;
        break;
    case 0x180:
        s->port0_usb_2_0_configflag = val;
        break;
    case 0x184:
        s->port0_usb_2_0_portsc1 = val;
        break;
    case 0x1a4:
        s->port0_usb_2_0_otgsc = val;
        break;
    case 0x1a8:
        s->port0_usb_2_0_usbmode = val;
        break;
    case 0x1ac:
        s->port0_usb_2_0_enpdtsetupstat = val;
        break;
    case 0x1b0:
        s->port0_usb_2_0_endptprime = val;
        break;
    case 0x1b4:
        s->port0_usb_2_0_endptflush = val;
        break;
    case 0x1b8:
        s->port0_usb_2_0_endptstatus = val;
        break;
    case 0x1bc:
        s->port0_usb_2_0_endptcomplete = val;
        break;
    case 0x1c0:
        s->port0_usb_2_0_endptctrl0 = val;
        break;
    case 0x1c4:
        s->port0_usb_2_0_endptctrl1 = val;
        break;
    case 0x1c8:
        s->port0_usb_2_0_endptctrl2 = val;
        break;
    case 0x1cc:
        s->port0_usb_2_0_endptctrl3 = val;
        break;
    case 0x300:
        s->port0_usb_2_0_bridge_control_register = val;
        break;
    case 0x310:
        s->port0_usb_2_0_bridge_interrupt_cause_register = val;
        break;
    case 0x314:
        s->port0_usb_2_0_bridge_interrupt_mask_register = val;
        break;
    case 0x31c:
        s->port0_usb_2_0_bridge_error_address_register = val;
        break;
    case 0x320:
        s->port0_usb_2_0_window0_control_register = val;
        break;
    case 0x324:
        s->port0_usb_2_0_window0_base_register = val;
        break;
    case 0x330:
        s->port0_usb_2_0_window1_control_register = val;
        break;
    case 0x334:
        s->port0_usb_2_0_window1_base_register = val;
        break;
    case 0x340:
        s->port0_usb_2_0_window2_control_register = val;
        break;
    case 0x344:
        s->port0_usb_2_0_window2_base_register = val;
        break;
    case 0x350:
        s->port0_usb_2_0_window3_control_register = val;
        break;
    case 0x354:
        s->port0_usb_2_0_window3_base_register = val;
        break;
    case 0x400:
        s->port0_usb_2_0_power_control_register = val;
        break;
    }
    mv88f5181l_usb_2_0_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_usb_2_0_controller_ops = {
    .read = mv88f5181l_usb_2_0_controller_read,
    .write = mv88f5181l_usb_2_0_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_gigabit_ethernet_controller_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_gigabit_ethernet_controller_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x000:
        res = s->phy_address;
        break;
    case 0x004:
        res = s->smi;
        break;
    case 0x008:
        res = s->ethernet_unit_default_address_euda;
        break;
    case 0x00c:
        res = s->ethernet_unit_default_id_eudid;
        break;
    case 0x014:
        res = s->ethernet_unit_reserved_eu;
        break;
    case 0x080:
        res = s->ethernet_unit_interrupt_cause_euic;
        break;
    case 0x084:
        res = s->ethernet_unit_interrupt_mask_euim;
        break;
    case 0x094:
        res = s->ethernet_unit_error_address_euea;
        break;
    case 0x098:
        res = s->ethernet_unit_internal_address_error_euiae;
        break;
    case 0x0a0:
        res = s->ethernet_unit_port_pads_calibration_eupcr;
        break;
    case 0x0b0:
        res = s->ethernet_unit_control_euc;
        break;
    case 0x200:
        res = s->base_address_0_ba0;
        break;
    case 0x204:
        res = s->size_s_0_sr0;
        break;
    case 0x208:
        res = s->base_address_1_ba1;
        break;
    case 0x20c:
        res = s->size_s_1_sr1;
        break;
    case 0x210:
        res = s->base_address_2_ba2;
        break;
    case 0x214:
        res = s->size_s_2_sr2;
        break;
    case 0x218:
        res = s->base_address_3_ba3;
        break;
    case 0x21c:
        res = s->size_s_3_sr3;
        break;
    case 0x220:
        res = s->base_address_4_ba4;
        break;
    case 0x224:
        res = s->size_s_4_sr4;
        break;
    case 0x228:
        res = s->base_address_5_ba5;
        break;
    case 0x22c:
        res = s->size_s_5_sr5;
        break;
    case 0x280:
        res = s->high_address_remap_ha_harr0;
        break;
    case 0x284:
        res = s->high_address_remap_ha_harr1;
        break;
    case 0x288:
        res = s->high_address_remap_ha_harr2;
        break;
    case 0x28c:
        res = s->high_address_remap_ha_harr3;
        break;
    case 0x290:
        res = s->base_address_enable_bare;
        break;
    case 0x294:
        res = s->ethernet_port_access_protect_epap;
        break;
    case 0x400:
        res = s->port_configuration_gec;
        break;
    case 0x404:
        res = s->port_configuration_extend_gecx;
        break;
    case 0x408:
        res = s->mii_serial_parameters;
        break;
    case 0x40c:
        res = s->gmii_serial_parameters;
        break;
    case 0x410:
        res = s->vlan_ethertype_evlane;
        break;
    case 0x414:
        res = s->mac_address_low_macal;
        break;
    case 0x418:
        res = s->mac_address_high_macah;
        break;
    case 0x41c:
        res = s->sdma_configuration_sdc;
        break;
    case 0x420:
        res = s->ip_differentiated_services_codepoint_0_to_priority_dscp0;
        break;
    case 0x424:
        res = s->ip_differentiated_services_codepoint_1_to_priority_dscp1;
        break;
    case 0x428:
        res = s->ip_differentiated_services_codepoint_2_to_priority_dscp2;
        break;
    case 0x42c:
        res = s->ip_differentiated_services_codepoint_23_to_priority_dscp3;
        break;
    case 0x430:
        res = s->ip_differentiated_services_codepoint_24_to_priority_dscp4;
        break;
    case 0x434:
        res = s->ip_differentiated_services_codepoint_25_to_priority_dscp5;
        break;
    case 0x438:
        res = s->ip_differentiated_services_codepoint_6_to_priority_dscp6;
        break;
    case 0x43c:
        res = s->port_serial_control_psc;
        break;
    case 0x440:
        res = s->vlan_priority_tag_to_priority_vpt2p;
        break;
    case 0x444:
        res = s->ethernet_port_status_ps;
        break;
    case 0x448:
        res = s->transmit_queue_command_tqc;
        break;
    case 0x458:
        res = s->maximum_transmit_unit_mtu;
        break;
    case 0x460:
        res = s->port_interrupt_cause_ic;
        break;
    case 0x464:
        res = s->port_interrupt_cause_extend_ice;
        break;
    case 0x468:
        res = s->port_interrupt_mask_pim;
        break;
    case 0x46c:
        res = s->port_extend_interrupt_mask_peim;
        break;
    case 0x470:
        res = s->port_rx_fifo_urgent_threshold_prfut;
        break;
    case 0x474:
        res = s->port_tx_fifo_urgent_threshold_ptfut;
        break;
    case 0x47c:
        res = s->port_rx_minimal_frame_size_pmfs;
        break;
    case 0x484:
        res = s->port_rx_discard_frame_counter_gedfc;
        break;
    case 0x488:
        res = s->port_overrun_frame_counter_pofc;
        break;
    case 0x494:
        res = s->port_internal_address_error_euiae;
        break;
    case 0x60c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q0;
        break;
    case 0x61c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q1;
        break;
    case 0x62c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q2;
        break;
    case 0x63c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q3;
        break;
    case 0x64c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q4;
        break;
    case 0x65c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q5;
        break;
    case 0x66c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q6;
        break;
    case 0x67c:
        res = s->ethernet_current_receive_descriptor_pointers_crdp_q7;
        break;
    case 0x680:
        res = s->receive_queue_command_rqc;
        break;
    case 0x684:
        res = s->transmit_current_served_descriptor_pointer;
        break;
    case 0x6c0:
        res = s->transmit_current_queue_descriptor_pointer_tcqdp_q0;
        break;
    case 0x700:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q0;
        break;
    case 0x704:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q0;
        break;
    case 0x708:
        res = s->transmit_queue_arbiter_configuration_tqxac_q0;
        break;
    case 0x710:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q1;
        break;
    case 0x714:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q1;
        break;
    case 0x718:
        res = s->transmit_queue_arbiter_configuration_tqxac_q1;
        break;
    case 0x720:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q2;
        break;
    case 0x724:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q2;
        break;
    case 0x728:
        res = s->transmit_queue_arbiter_configuration_tqxac_q2;
        break;
    case 0x730:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q3;
        break;
    case 0x734:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q3;
        break;
    case 0x738:
        res = s->transmit_queue_arbiter_configuration_tqxac_q3;
        break;
    case 0x740:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q4;
        break;
    case 0x744:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q4;
        break;
    case 0x748:
        res = s->transmit_queue_arbiter_configuration_tqxac_q4;
        break;
    case 0x750:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q5;
        break;
    case 0x754:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q5;
        break;
    case 0x758:
        res = s->transmit_queue_arbiter_configuration_tqxac_q5;
        break;
    case 0x760:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q6;
        break;
    case 0x764:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q6;
        break;
    case 0x768:
        res = s->transmit_queue_arbiter_configuration_tqxac_q6;
        break;
    case 0x770:
        res = s->transmit_queue_token_bucket_counter_tqxtbc_q7;
        break;
    case 0x774:
        res = s->transmit_queue_token_bucket_configuration_tqxtbc_q7;
        break;
    case 0x778:
        res = s->transmit_queue_arbiter_configuration_tqxac_q7;
        break;
    case 0x1000:
        res = s->mac_mib_countersnterrupt_cause_register;
        break;
    case 0x1400:
        res = s->destination_address_filter_special_multicast_table_dfsmt;
        break;
    case 0x1500:
        res = s->destination_address_filter_other_multicast_table_dfut;
        break;
    case 0x1600:
        res = s->destination_address_filter_unicast_table_dfut;
        break;
    }
    return res;
}

static void mv88f5181l_gigabit_ethernet_controller_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x000:
        s->phy_address = val;
        break;
    case 0x004:
        s->smi = val;
        break;
    case 0x008:
        s->ethernet_unit_default_address_euda = val;
        break;
    case 0x00c:
        s->ethernet_unit_default_id_eudid = val;
        break;
    case 0x014:
        s->ethernet_unit_reserved_eu = val;
        break;
    case 0x080:
        s->ethernet_unit_interrupt_cause_euic = val;
        break;
    case 0x084:
        s->ethernet_unit_interrupt_mask_euim = val;
        break;
    case 0x094:
        s->ethernet_unit_error_address_euea = val;
        break;
    case 0x098:
        s->ethernet_unit_internal_address_error_euiae = val;
        break;
    case 0x0a0:
        s->ethernet_unit_port_pads_calibration_eupcr = val;
        break;
    case 0x0b0:
        s->ethernet_unit_control_euc = val;
        break;
    case 0x200:
        s->base_address_0_ba0 = val;
        break;
    case 0x204:
        s->size_s_0_sr0 = val;
        break;
    case 0x208:
        s->base_address_1_ba1 = val;
        break;
    case 0x20c:
        s->size_s_1_sr1 = val;
        break;
    case 0x210:
        s->base_address_2_ba2 = val;
        break;
    case 0x214:
        s->size_s_2_sr2 = val;
        break;
    case 0x218:
        s->base_address_3_ba3 = val;
        break;
    case 0x21c:
        s->size_s_3_sr3 = val;
        break;
    case 0x220:
        s->base_address_4_ba4 = val;
        break;
    case 0x224:
        s->size_s_4_sr4 = val;
        break;
    case 0x228:
        s->base_address_5_ba5 = val;
        break;
    case 0x22c:
        s->size_s_5_sr5 = val;
        break;
    case 0x280:
        s->high_address_remap_ha_harr0 = val;
        break;
    case 0x284:
        s->high_address_remap_ha_harr1 = val;
        break;
    case 0x288:
        s->high_address_remap_ha_harr2 = val;
        break;
    case 0x28c:
        s->high_address_remap_ha_harr3 = val;
        break;
    case 0x290:
        s->base_address_enable_bare = val;
        break;
    case 0x294:
        s->ethernet_port_access_protect_epap = val;
        break;
    case 0x400:
        s->port_configuration_gec = val;
        break;
    case 0x404:
        s->port_configuration_extend_gecx = val;
        break;
    case 0x408:
        s->mii_serial_parameters = val;
        break;
    case 0x40c:
        s->gmii_serial_parameters = val;
        break;
    case 0x410:
        s->vlan_ethertype_evlane = val;
        break;
    case 0x414:
        s->mac_address_low_macal = val;
        break;
    case 0x418:
        s->mac_address_high_macah = val;
        break;
    case 0x41c:
        s->sdma_configuration_sdc = val;
        break;
    case 0x420:
        s->ip_differentiated_services_codepoint_0_to_priority_dscp0 = val;
        break;
    case 0x424:
        s->ip_differentiated_services_codepoint_1_to_priority_dscp1 = val;
        break;
    case 0x428:
        s->ip_differentiated_services_codepoint_2_to_priority_dscp2 = val;
        break;
    case 0x42c:
        s->ip_differentiated_services_codepoint_23_to_priority_dscp3 = val;
        break;
    case 0x430:
        s->ip_differentiated_services_codepoint_24_to_priority_dscp4 = val;
        break;
    case 0x434:
        s->ip_differentiated_services_codepoint_25_to_priority_dscp5 = val;
        break;
    case 0x438:
        s->ip_differentiated_services_codepoint_6_to_priority_dscp6 = val;
        break;
    case 0x43c:
        s->port_serial_control_psc = val;
        break;
    case 0x440:
        s->vlan_priority_tag_to_priority_vpt2p = val;
        break;
    case 0x444:
        s->ethernet_port_status_ps = val;
        break;
    case 0x448:
        s->transmit_queue_command_tqc = val;
        break;
    case 0x458:
        s->maximum_transmit_unit_mtu = val;
        break;
    case 0x460:
        s->port_interrupt_cause_ic = val;
        break;
    case 0x464:
        s->port_interrupt_cause_extend_ice = val;
        break;
    case 0x468:
        s->port_interrupt_mask_pim = val;
        break;
    case 0x46c:
        s->port_extend_interrupt_mask_peim = val;
        break;
    case 0x470:
        s->port_rx_fifo_urgent_threshold_prfut = val;
        break;
    case 0x474:
        s->port_tx_fifo_urgent_threshold_ptfut = val;
        break;
    case 0x47c:
        s->port_rx_minimal_frame_size_pmfs = val;
        break;
    case 0x484:
        s->port_rx_discard_frame_counter_gedfc = val;
        break;
    case 0x488:
        s->port_overrun_frame_counter_pofc = val;
        break;
    case 0x494:
        s->port_internal_address_error_euiae = val;
        break;
    case 0x60c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q0 = val;
        break;
    case 0x61c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q1 = val;
        break;
    case 0x62c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q2 = val;
        break;
    case 0x63c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q3 = val;
        break;
    case 0x64c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q4 = val;
        break;
    case 0x65c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q5 = val;
        break;
    case 0x66c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q6 = val;
        break;
    case 0x67c:
        s->ethernet_current_receive_descriptor_pointers_crdp_q7 = val;
        break;
    case 0x680:
        s->receive_queue_command_rqc = val;
        break;
    case 0x684:
        s->transmit_current_served_descriptor_pointer = val;
        break;
    case 0x6c0:
        s->transmit_current_queue_descriptor_pointer_tcqdp_q0 = val;
        break;
    case 0x700:
        s->transmit_queue_token_bucket_counter_tqxtbc_q0 = val;
        break;
    case 0x704:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q0 = val;
        break;
    case 0x708:
        s->transmit_queue_arbiter_configuration_tqxac_q0 = val;
        break;
    case 0x710:
        s->transmit_queue_token_bucket_counter_tqxtbc_q1 = val;
        break;
    case 0x714:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q1 = val;
        break;
    case 0x718:
        s->transmit_queue_arbiter_configuration_tqxac_q1 = val;
        break;
    case 0x720:
        s->transmit_queue_token_bucket_counter_tqxtbc_q2 = val;
        break;
    case 0x724:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q2 = val;
        break;
    case 0x728:
        s->transmit_queue_arbiter_configuration_tqxac_q2 = val;
        break;
    case 0x730:
        s->transmit_queue_token_bucket_counter_tqxtbc_q3 = val;
        break;
    case 0x734:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q3 = val;
        break;
    case 0x738:
        s->transmit_queue_arbiter_configuration_tqxac_q3 = val;
        break;
    case 0x740:
        s->transmit_queue_token_bucket_counter_tqxtbc_q4 = val;
        break;
    case 0x744:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q4 = val;
        break;
    case 0x748:
        s->transmit_queue_arbiter_configuration_tqxac_q4 = val;
        break;
    case 0x750:
        s->transmit_queue_token_bucket_counter_tqxtbc_q5 = val;
        break;
    case 0x754:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q5 = val;
        break;
    case 0x758:
        s->transmit_queue_arbiter_configuration_tqxac_q5 = val;
        break;
    case 0x760:
        s->transmit_queue_token_bucket_counter_tqxtbc_q6 = val;
        break;
    case 0x764:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q6 = val;
        break;
    case 0x768:
        s->transmit_queue_arbiter_configuration_tqxac_q6 = val;
        break;
    case 0x770:
        s->transmit_queue_token_bucket_counter_tqxtbc_q7 = val;
        break;
    case 0x774:
        s->transmit_queue_token_bucket_configuration_tqxtbc_q7 = val;
        break;
    case 0x778:
        s->transmit_queue_arbiter_configuration_tqxac_q7 = val;
        break;
    case 0x1000:
        s->mac_mib_countersnterrupt_cause_register = val;
        break;
    case 0x1400:
        s->destination_address_filter_special_multicast_table_dfsmt = val;
        break;
    case 0x1500:
        s->destination_address_filter_other_multicast_table_dfut = val;
        break;
    case 0x1600:
        s->destination_address_filter_unicast_table_dfut = val;
        break;
    }
    mv88f5181l_gigabit_ethernet_controller_update(s);
}

static const MemoryRegionOps mv88f5181l_gigabit_ethernet_controller_ops = {
    .read = mv88f5181l_gigabit_ethernet_controller_read,
    .write = mv88f5181l_gigabit_ethernet_controller_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_cesa_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_cesa_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00000078:
        res = s->des_data_out_low_register;
        break;
    case 0x0000007c:
        res = s->des_data_out_high_register;
        break;
    case 0x00000070:
        res = s->des_data_buffer_low_register;
        break;
    case 0x00000074:
        res = s->des_data_buffer_high_register;
        break;
    case 0x00000040:
        res = s->des_initial_value_low_register;
        break;
    case 0x00000044:
        res = s->des_initial_value_high_register;
        break;
    case 0x00000048:
        res = s->des_key0_low_register;
        break;
    case 0x0000004c:
        res = s->des_key0_high_register;
        break;
    case 0x00000050:
        res = s->des_key1_low_register;
        break;
    case 0x00000054:
        res = s->des_key1_high_register;
        break;
    case 0x00000060:
        res = s->des_key2_low_register;
        break;
    case 0x00000064:
        res = s->des_key2_high_register;
        break;
    case 0x00000058:
        res = s->des_command_register;
        break;
    case 0x00000038:
        res = s->sha_1_or_md5_data_in_register;
        break;
    case 0x00000020:
        res = s->sha_1_or_md5_bit_count_low_register;
        break;
    case 0x00000024:
        res = s->sha_1_or_md5_bit_count_high_register;
        break;
    case 0x00000000:
        res = s->sha_1_or_md5_initial_value_or_digest_a_register;
        break;
    case 0x00000004:
        res = s->sha_1_or_md5_initial_value_or_digest_b_register;
        break;
    case 0x00000008:
        res = s->sha_1_or_md5_initial_value_or_digest_c_register;
        break;
    case 0x0000000c:
        res = s->sha_1_or_md5_initial_value_or_digest_d_register;
        break;
    case 0x00000010:
        res = s->sha_1_initial_value_or_digest_e_register;
        break;
    case 0x00000018:
        res = s->sha_1_or_md5_authentication_command_register;
        break;
    case 0x000000a0:
        res = s->aes_encryption_data_in_or_out_column_3_register;
        break;
    case 0x000000a4:
        res = s->aes_encryption_data_in_or_out_column_2_register;
        break;
    case 0x000000a8:
        res = s->aes_encryption_data_in_or_out_column_1_register;
        break;
    case 0x000000ac:
        res = s->aes_encryption_data_in_or_out_column_0_register;
        break;
    case 0x00000090:
        res = s->aes_encryption_key_column_3_register;
        break;
    case 0x00000094:
        res = s->aes_encryption_key_column_2_register;
        break;
    case 0x00000098:
        res = s->aes_encryption_key_column_1_register;
        break;
    case 0x0000009c:
        res = s->aes_encryption_key_column_0_register;
        break;
    case 0x00000080:
        res = s->aes_encryption_key_column_7_register;
        break;
    case 0x00000084:
        res = s->aes_encryption_key_column_6_register;
        break;
    case 0x00000088:
        res = s->aes_encryption_key_column_5_register;
        break;
    case 0x0000008c:
        res = s->aes_encryption_key_column_4_register;
        break;
    case 0x000000b0:
        res = s->aes_encryption_command_register;
        break;
    case 0x000000e0:
        res = s->aes_decryption_data_in_or_out_column_3_register;
        break;
    case 0x000000e4:
        res = s->aes_decryption_data_in_or_out_column_2_register;
        break;
    case 0x000000e8:
        res = s->aes_decryption_data_in_or_out_column_1_register;
        break;
    case 0x000000ec:
        res = s->aes_decryption_data_in_or_out_column_0_register;
        break;
    case 0x000000d0:
        res = s->aes_decryption_key_column_3_register;
        break;
    case 0x000000d4:
        res = s->aes_decryption_key_column_2_register;
        break;
    case 0x000000d8:
        res = s->aes_decryption_key_column_1_register;
        break;
    case 0x000000dc:
        res = s->aes_decryption_key_column_0_register;
        break;
    case 0x000000c0:
        res = s->aes_decryption_key_column_7_register;
        break;
    case 0x000000c4:
        res = s->aes_decryption_key_column_6_register;
        break;
    case 0x000000c8:
        res = s->aes_decryption_key_column_5_register;
        break;
    case 0x000000cc:
        res = s->aes_decryption_key_column_4_register;
        break;
    case 0x000000f0:
        res = s->aes_decryption_command_register;
        break;
    case 0x00000100:
        res = s->security_accelerator_command_register;
        break;
    case 0x00000104:
        res = s->security_accelerator_descriptor_pointer_session_0_register;
        break;
    case 0x00000114:
        res = s->security_accelerator_descriptor_pointer_session_1_register;
        break;
    case 0x00000108:
        res = s->security_accelerator_configuration_register;
        break;
    case 0x0000010c:
        res = s->security_accelerator_status_register;
        break;
    case 0x00000120:
        res = s->cryptographic_engines_and_security_accelerator_interrupt_cause_register;
        break;
    case 0x00000124:
        res = s->cryptographic_engines_and_security_accelerator_interrupt_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_cesa_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00000078:
        s->des_data_out_low_register = val;
        break;
    case 0x0000007c:
        s->des_data_out_high_register = val;
        break;
    case 0x00000070:
        s->des_data_buffer_low_register = val;
        break;
    case 0x00000074:
        s->des_data_buffer_high_register = val;
        break;
    case 0x00000040:
        s->des_initial_value_low_register = val;
        break;
    case 0x00000044:
        s->des_initial_value_high_register = val;
        break;
    case 0x00000048:
        s->des_key0_low_register = val;
        break;
    case 0x0000004c:
        s->des_key0_high_register = val;
        break;
    case 0x00000050:
        s->des_key1_low_register = val;
        break;
    case 0x00000054:
        s->des_key1_high_register = val;
        break;
    case 0x00000060:
        s->des_key2_low_register = val;
        break;
    case 0x00000064:
        s->des_key2_high_register = val;
        break;
    case 0x00000058:
        s->des_command_register = val;
        break;
    case 0x00000038:
        s->sha_1_or_md5_data_in_register = val;
        break;
    case 0x00000020:
        s->sha_1_or_md5_bit_count_low_register = val;
        break;
    case 0x00000024:
        s->sha_1_or_md5_bit_count_high_register = val;
        break;
    case 0x00000000:
        s->sha_1_or_md5_initial_value_or_digest_a_register = val;
        break;
    case 0x00000004:
        s->sha_1_or_md5_initial_value_or_digest_b_register = val;
        break;
    case 0x00000008:
        s->sha_1_or_md5_initial_value_or_digest_c_register = val;
        break;
    case 0x0000000c:
        s->sha_1_or_md5_initial_value_or_digest_d_register = val;
        break;
    case 0x00000010:
        s->sha_1_initial_value_or_digest_e_register = val;
        break;
    case 0x00000018:
        s->sha_1_or_md5_authentication_command_register = val;
        break;
    case 0x000000a0:
        s->aes_encryption_data_in_or_out_column_3_register = val;
        break;
    case 0x000000a4:
        s->aes_encryption_data_in_or_out_column_2_register = val;
        break;
    case 0x000000a8:
        s->aes_encryption_data_in_or_out_column_1_register = val;
        break;
    case 0x000000ac:
        s->aes_encryption_data_in_or_out_column_0_register = val;
        break;
    case 0x00000090:
        s->aes_encryption_key_column_3_register = val;
        break;
    case 0x00000094:
        s->aes_encryption_key_column_2_register = val;
        break;
    case 0x00000098:
        s->aes_encryption_key_column_1_register = val;
        break;
    case 0x0000009c:
        s->aes_encryption_key_column_0_register = val;
        break;
    case 0x00000080:
        s->aes_encryption_key_column_7_register = val;
        break;
    case 0x00000084:
        s->aes_encryption_key_column_6_register = val;
        break;
    case 0x00000088:
        s->aes_encryption_key_column_5_register = val;
        break;
    case 0x0000008c:
        s->aes_encryption_key_column_4_register = val;
        break;
    case 0x000000b0:
        s->aes_encryption_command_register = val;
        break;
    case 0x000000e0:
        s->aes_decryption_data_in_or_out_column_3_register = val;
        break;
    case 0x000000e4:
        s->aes_decryption_data_in_or_out_column_2_register = val;
        break;
    case 0x000000e8:
        s->aes_decryption_data_in_or_out_column_1_register = val;
        break;
    case 0x000000ec:
        s->aes_decryption_data_in_or_out_column_0_register = val;
        break;
    case 0x000000d0:
        s->aes_decryption_key_column_3_register = val;
        break;
    case 0x000000d4:
        s->aes_decryption_key_column_2_register = val;
        break;
    case 0x000000d8:
        s->aes_decryption_key_column_1_register = val;
        break;
    case 0x000000dc:
        s->aes_decryption_key_column_0_register = val;
        break;
    case 0x000000c0:
        s->aes_decryption_key_column_7_register = val;
        break;
    case 0x000000c4:
        s->aes_decryption_key_column_6_register = val;
        break;
    case 0x000000c8:
        s->aes_decryption_key_column_5_register = val;
        break;
    case 0x000000cc:
        s->aes_decryption_key_column_4_register = val;
        break;
    case 0x000000f0:
        s->aes_decryption_command_register = val;
        break;
    case 0x00000100:
        s->security_accelerator_command_register = val;
        break;
    case 0x00000104:
        s->security_accelerator_descriptor_pointer_session_0_register = val;
        break;
    case 0x00000114:
        s->security_accelerator_descriptor_pointer_session_1_register = val;
        break;
    case 0x00000108:
        s->security_accelerator_configuration_register = val;
        break;
    case 0x0000010c:
        s->security_accelerator_status_register = val;
        break;
    case 0x00000120:
        s->cryptographic_engines_and_security_accelerator_interrupt_cause_register = val;
        break;
    case 0x00000124:
        s->cryptographic_engines_and_security_accelerator_interrupt_mask_register = val;
        break;
    }
    mv88f5181l_cesa_update(s);
}

static const MemoryRegionOps mv88f5181l_cesa_ops = {
    .read = mv88f5181l_cesa_read,
    .write = mv88f5181l_cesa_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void wrt350n_v2_reset(void *opaque)
{
    WRT350NV2State *s = opaque;

    s->gpio_data_out_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_out_enable_control_register = 0xFFFF << 0 | 0x0 << 26;
    s->gpio_blink_enable_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_polarity_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_data_in_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_cause_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_mask_register = 0x0 << 0 | 0x0 << 26;
    s->gpio_interrupt_level_mask_register = 0x0 << 0 | 0x0 << 26;
    s->window0_control_register = 0x1FFF5941;
    s->window0_base_register = 0x80000000;
    s->window0_remap_low_register = 0x80000000;
    s->window0_remap_high_register = 0x0;
    s->window1_control_register = 0x1FFF5931;
    s->window1_base_register = 0xA0000000;
    s->window1_remap_low_register = 0xA0000000;
    s->window1_remap_high_register = 0x0;
    s->window2_control_register = 0x00005141;
    s->window2_base_register = 0xC0000000;
    s->window2_remap_low_register = 0xC0000000;
    s->window2_remap_high_register = 0x0;
    s->window3_control_register = 0x00005131;
    s->window3_base_register = 0xC8000000;
    s->window4_control_register = 0x00000091;
    s->window4_base_register = 0xC8010000;
    s->window5_control_register = 0x0;
    s->window5_base_register = 0x0;
    s->window6_control_register = 0x07FF1B11;
    s->window6_base_register = 0xF0000000;
    s->window7_control_register = 0x07FF0F11;
    s->window7_base_register = 0xF8000000;
    s->_88f5181_internal_registers_base_address_register = 0xD0000000;
    s->cs0n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x0 << 24;
    s->cs0n_size_register = 0x1 << 0 | 0x0 << 1 |  0xFF << 16 | 0x0F << 24;
    s->cs1n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x10 << 24;
    s->cs1n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->cs2n_base_address_register = 0x0 << 0 | 0xFF << 16 | 0x20 << 24;
    s->cs2n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->cs3n_base_address_register = 0x0 << 0 | 0x0 << 16 | 0x30 << 24;
    s->cs3n_size_register = 0x1 << 0 | 0x0 << 1 | 0xFF << 16 | 0x0F << 24;
    s->ddr_sdram_configuration_register = 0x400 << 0 | 0x2 << 14 | 0x1 << 18 | 0x2 << 20 | 0x1 << 24 | 0x1 << 25 /* 0 14 17 18 19 20 22 24 25 26 */;
    s->ddr_sdram_control_register = 0x1 << 6 | 0x1 << 12 | 0x1 << 18 | 0x3 << 24 /* 0 6 7 12 13 14 18 19 24 28 */;
    s->ddr_sdram_timing_low_register = 0x0 << 0 | 0x2 << 4 | 0x2 << 8 | 0x2 << 12 | 0x1 << 16 | 0x8 << 20 | 0x1 << 24 | 0x1 << 28;
    s->ddr_sdram_timing_high_register = 0xD << 0 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8 | 0x0 << 10 | 0x0 << 12;
    s->ddr2_sdram_timing_low_register = 0x5 << 0 | 0x0 << 4 | 0x3 << 8 | 0x3 << 12 | 0x6 << 16 | 0x0 << 20;
    s->ddr2_sdram_timing_high_register = 0x0 << 0 | 0x3 << 4 | 0x3 << 8 | 0x6 << 12 | 0x0 << 16;
    s->ddr_sdram_address_control_register = 0x0 << 0 | 0x1 << 4 | 0x0 << 6;
    s->ddr_sdram_open_pages_control_register = 0x0 << 0 | 0x0 << 1;
    s->ddr_sdram_operation_register = 0x0 << 0 | 0x0 << 4;
    s->ddr_sdram_operation_control_register = 0x0 << 0 | 0x0 << 2;
    s->ddr_sdram_mode_register = 0x2 << 0 | 0x0 << 3 | 0x3 << 4 | 0x0 << 7 | 0x0 << 8 | 0x0 << 12 | 0x0 << 13 | 0x0 << 14;
    s->extended_ddr_sdram_mode_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 7 | 0x0 << 13 | 0x0 << 14;
    s->ddr_sdram_initialization_control_register = 0x0 << 0 | 0x0 << 1;
    s->ddr_sdram_address_or_control_pads_calibration_register = 0x0 << 0 | 0x0 << 6 | 0x0 << 12 | 0x0 << 14 | 0x1 << 16 | 0x0 << 17 | 0x0 << 23 | 0x0 << 29 | 0x0 << 31;
    s->ddr_sdram_data_pads_calibration_register = 0x144 << 0;
    s->ddr2_sdram_odt_control_low_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 12 | 0x0 << 16 | 0x0 << 20 | 0x0 << 24 | 0x0 << 28;
    s->ddr2_sdram_odt_control_high_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 4 | 0x0 << 6 | 0x0 << 8;
    s->ddr2_sdram_odt_control_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 10 | 0x0 << 12;
    s->ddr_sdram_interface_mbus_control_low_register = 0x0 << 0 | 0x1 << 4 | 0x2 << 8 | 0x3 << 12 | 0x4 << 16 | 0x5 << 20 | 0x6 << 24 | 0x7 << 28;
    s->ddr_sdram_interface_mbus_control_high_register = 0x8 << 0 | 0x9 << 4 | 0xA << 8 | 0xB << 12 | 0xC << 16 | 0xD << 20 | 0xE << 24 | 0xF << 28;
    s->ddr_sdram_interface_mbus_timeout_register = 0xFF << 0 | 0x0 << 8 | 0x1 << 16 | 0x0 << 17;
    s->ddr_sdram_mmask_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 4 | 0xF << 5 | 0x0 << 9;
    s->mpp_control_0_register = 0x0;
    s->mpp_control_1_register = 0x0;
    s->mpp_control_2_register = 0x0;
    s->device_multiplex_control_register = 0x0;
    s->sample_at_reset_register = 0x0;
    s->csn0_bar_size = 0x0 << 0 | 0x0FFFF << 12;
    s->csn1_bar_size = 0x0FFFF000 << 0;
    s->csn2_bar_size = 0x0FFFF000 << 0;
    s->csn3_bar_size = 0x0FFFF000 << 0;
    s->devcsn0_bar_size = 0x07FFF000 << 0;
    s->devcsn1_bar_size = 0x07FFF000 << 0;
    s->devcsn2_bar_size = 0x07FFF000 << 0;
    s->boot_csn_bar_size = 0x07FFF000 << 0;
    s->p2p_mem0_bar_size = 0x1FFFF000 << 0;
    s->p2p_i_or_o_bar_size = 0xF000 << 0;
    s->expansion_rom_bar_size = 0x0 << 0;
    s->base_address_registers_enable = 0x1 << 4 | 0x1 << 5 | 0x1 << 7 | 0x1 << 10 | 0x1 << 11 | 0x1 << 12 | 0x1 << 13 /* 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 */;
    s->csn0_base_address_remap = 0x0 /* 0 12 */;
    s->csn1_base_address_remap = 0x10000000 << 0;
    s->csn2_base_address_remap = 0x20000000 << 0;
    s->csn3_base_address_remap = 0x30000000 << 0;
    s->devcsn0_base_address_remap = 0xE0000000 << 0;
    s->devcsn1_base_address_remap = 0xE8000000 << 0;
    s->devcsn2_base_address_remap = 0xF0000000 << 0;
    s->bootcsn_base_address_remap = 0xF8000000 << 0;
    s->p2p_mem0_base_address_remap_low = 0x80000000 << 0;
    s->p2p_mem0_base_address_remap_high = 0x0 << 0;
    s->p2p_i_or_o_base_address_remap = 0xC0000000 << 0;
    s->expansion_rom_base_address_remap = 0xE0000000 << 0;
    s->dram_bar_bank_select = 0x0 << 0 | 0x1 << 2 | 0x2 << 4 | 0x3 << 6 | 0x0 << 8;
    s->pci_address_decode_control = 0x1 << 3 /* 0 1 3 4 8 25 */;
    s->pci_dll_control = 0x1 << 1 | 0x1 << 20 /* 0 1 3 5 9 13 15 16 17 20 22 31 */;
    s->pci_or_mpp_pads_calibration = 0xF << 0 | 0xF << 4 | 0xF << 8 | 0xF << 12 | 0x1 << 16 | 0x1 << 17 | 0x0 << 18 | 0x0 << 22 | 0x0 << 31;
    s->pci_command = 0x1 << 0 | 0x1 << 4 |  0x1 << 5 | 0x1 << 6 | 0x1 << 8 | 0x1 << 9 | 0x1 << 13 | 0x1 << 14 | 0x1 << 16 | 0x1 << 17 | 0x1 << 24 /* 0 1 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 24 26 28 29 */;
    s->pci_mode = 0x1 << 31 /* 0 2 3 4 6 8 9 31 */;
    s->pci_retry = 0x0 /* 0 16 24 */;
    s->pci_discard_timer = 0x0 /* 0 16 */;
    s->msi_trigger_timer = 0xFFFF << 0 | 0x0 << 16;
    s->pci_arbiter_control = 0x6 << 3 /* 0 1 2 3 7 14 21 31 */;
    s->pci_p2p_configuration = 0xFF << 0 | 0x0 << 16 | 0x0 << 24 | 0x0 << 29;
    s->pci_access_control_base_0_low = 0x0 /* 0 1 4 5 6 8 10 12 */;
    s->pci_access_control_base_0_high = 0x0 << 0;
    s->pci_access_control_size_0 = 0x0 /* 0 4 5 8 19 11 12 */;
    s->pci_access_control_base_1_low = 0x0 << 0;
    s->pci_access_control_base_1_high = 0x0 << 0;
    s->pci_access_control_size_1 = 0x0 << 0;
    s->pci_access_control_base_2_low = 0x0 << 0;
    s->pci_access_control_base_2_high = 0x0 << 0;
    s->pci_access_control_size_2 = 0x0 << 0;
    s->pci_access_control_base_3_low = 0x0 << 0;
    s->pci_access_control_base_3_high = 0x0 << 0;
    s->pci_access_control_size_3 = 0x0 << 0;
    s->pci_access_control_base_4_low = 0x0 << 0;
    s->pci_access_control_base_4_high = 0x0 << 0;
    s->pci_access_control_size_4 = 0x0 << 0;
    s->pci_access_control_base_5_low = 0x0 << 0;
    s->pci_access_control_base_5_high = 0x0 << 0;
    s->pci_access_control_size_5 = 0x0 << 0;
    s->pci_configuration_address = 0x0 /* 0 2 8 11 16 24 31 */;
    s->pci_configuration_data = 0x0 << 0;
    s->pci_interrupt_acknowledge = 0x0 << 0;
    s->pci_serrn_mask = 0x0 /* 0 1 2 3 5 6 7 8 9 10 11 12 17 18 20 21 22 */;
    s->pci_interrupt_cause = 0x0 /* 0 24 25 26 27 */;
    s->pci_interrupt_mask = 0x0 /* 0 27 */;
    s->pci_error_address_low = 0x0 << 0;
    s->pci_error_address_high = 0x0 << 0;
    s->pci_error_command = 0x0 /* 0 4 5 */;
    s->pci_express_device_and_vendor_id_register = 0x11AB << 0 | 0x5181 << 16;
    s->pci_express_command_and_status_register = 0x1 << 20 /* 0 1 2 3 6 7 8 9 10 11 19 20 21 24 25 27 29 30 31 */;
    s->pci_express_class_code_and_revision_id_register = 0x3 << 0 | 0x80 << 16 | 0x05 << 24;
    s->pci_express_bist_header_type_and_cache_line_size_register = 0x0 /* 0 8 16 24 28 30 31 */;
    s->pci_express_bar0_internal_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xD00 << 20;
    s->pci_express_bar0_internal_high_register = 0x0 << 0;
    s->pci_express_bar1_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0x0 << 16;
    s->pci_express_bar1_high_register = 0x0 << 0;
    s->pci_express_bar2_register = 0x0 << 0 | 0x2 << 1 | 0x1 << 3 | 0x0 << 4 | 0xF000 << 16;
    s->pci_express_bar2_high_register = 0x0 << 0;
    s->pci_express_subsystem_device_and_vendor_id = 0x11AB << 0 | 0x11AB << 16;
    s->pci_express_expansion_rom_bar_register = 0x0 /* 0 1 19 22 */;
    s->pci_express_capability_list_pointer_register = 0x40 << 0 | 0x0 << 8;
    s->pci_express_interrupt_pin_and_line_register = 0x0 << 0 | 0x1 << 8 | 0x0 << 16;
    s->pci_express_power_management_capability_header_register = 0x01 << 0 | 0x50 << 8 | 0x2 << 16 /* 0 8 16 19 21 22 25 26 27 */;
    s->pci_express_power_management_control_and_status_register = 0x0 /* 0 2 8 9 13 15 16 24 */;
    s->pci_express_msi_message_control_register = 0x5 << 0 | 0x60 << 8 | 0x1 << 23 /* 0 8 16 17 20 23 24 */;
    s->pci_express_msi_message_address_register = 0x0 << 0 | 0x0 << 2;
    s->pci_express_msi_message_address_high_register = 0x0 << 0;
    s->pci_express_msi_message_data_register = 0x0 << 0 | 0x0 << 16;
    s->pci_express_capability_register = 0x10 << 0 | 0x1 << 16 /* 0 8 16 20 24 25 30 */;
    s->pci_express_device_capabilities_register = 0x2 << 6 /* 0 3 6 9 12 13 14 15 18 26 28 */;
    s->pci_express_device_control_status_register = 0x2 << 12 /* 0 1 2 3 4 5 8 10 11 12 15 16 17 18 19 20 21 22 */;
    s->pci_express_link_capabilities_register = 0x1 << 0 | 0x0 << 4 | 0x1 << 10 | 0x0 << 12 | 0x7 << 15 | 0x0 << 18 | 0x0 << 24;
    s->pci_express_link_control_status_register = 0x1 << 3 | 0x1 << 16 | 0x1 << 28 /* 0 2 3 4 5 6 7 8 16 20 26 27 28 29 */;
    s->pci_express_advanced_error_report_header_register = 0x1 << 0 | 0x1 << 16 | 0x0 << 20;
    s->pci_express_uncorrectable_error_status_register = 0x0 /* 0 4 5 12 13 14 15 16 17 18 19 20 21 */;
    s->pci_express_uncorrectable_error_mask_register = 0x0 << 0;
    s->pci_express_uncorrectable_error_severity_register = 0x60010 << 0;
    s->pci_express_correctable_error_status_register = 0x0 /* 0 1 6 7 8 9 12 13 */;
    s->pci_express_correctable_error_mask_register = 0x0 << 0;
    s->pci_express_advanced_error_capability_and_control_register = 0x0 << 0 | 0x0 << 5;
    s->pci_express_header_log_first_dword_register = 0x0 << 0;
    s->pci_express_header_log_second_dword_register = 0x0 << 0;
    s->pci_express_header_log_third_dword_register = 0x0 << 0;
    s->pci_express_header_log_fourth_dword_register = 0x0 << 0;
    s->pci_express_bar1_control_register = 0x1 << 0 | 0x0 << 1 | 0x3FFF << 16;
    s->pci_express_bar2_control_register = 0x1 << 0 | 0x0 << 1 | 0x0FFF << 16;
    s->pci_express_expansion_rom_bar_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 19 | 0x0 << 22;
    s->pci_express_configuration_address_register = 0x0 << 0 | 0x0 << 2 | 0x0 << 8 | 0x0 << 11 | 0x0 << 16 | 0x0 << 24 | 0x0 << 28 | 0x0 << 31;
    s->pci_express_configuration_data_register = 0x0 << 0;
    s->pci_express_interrupt_cause = 0x0 << 0 /* 0 1 2 3 4 5 8 9 10 11 12 13 16 17 18 19 20 21 22 23 24 25 26 27 28 */;
    s->pci_express_interrupt_mask = 0x0 << 0;
    s->pci_express_window0_control_register = 0x1 << 0 | 0x0 << 1 | 0x0 << 4 | 0x0E << 8 | 0x0FFF << 16;
    s->pci_express_window0_base_register = 0x0 << 0 | 0x0 << 16;
    s->pci_express_window0_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window1_control_register = 0x1 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x0D << 8 | 0x0FFF << 16;
    s->pci_express_window1_base_register = 0x0 << 0 | 0x1000 << 16;
    s->pci_express_window1_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window2_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x0B  << 8 | 0x0FFF << 16;
    s->pci_express_window2_base_register = 0x0 << 0 | 0x2000 << 16;
    s->pci_express_window2_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window3_control_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 2 | 0x0 << 4 | 0x07  << 8 | 0x0FFF << 16;
    s->pci_express_window3_base_register = 0x0 << 0 | 0x3000 << 16;
    s->pci_express_window3_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window4_control_register = 0x1 << 0 | 0x1 << 1 | 0x0 << 2 | 0x1 << 4 | 0x1B  << 8 | 0x07FF << 16;
    s->pci_express_window4_base_register = 0x0 << 0 | 0xF000 << 16;
    s->pci_express_window4_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_window5_control_register = 0x1 << 0 | 0x1 << 1 | 0x0 << 2 | 0x1 << 4 | 0x0F << 8 | 0x07FF << 16;
    s->pci_express_window5_base_register = 0x0 << 0 | 0xF800 << 16;
    s->pci_express_window5_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_default_window_control_register = 0x0 << 0 | 0x0 << 4 | 0x0 << 8 | 0x0 << 16;
    s->pci_express_expansion_rom_window_control_register = 0x0 << 0 | 0x1 << 4 | 0xF << 8 | 0x0 << 16;
    s->pci_express_expansion_rom_window_remap_register = 0x0 << 0 | 0x0 << 1 | 0x0 << 16;
    s->pci_express_control_register = 0x1 << 0 | 0x1 << 3 | 0x3 << 8 | 0x14 << 16 /* 0 1 2 3 8 19 16 24 25 26 27 28 29 */;
    s->pci_express_status_register = 0x0 /* 0 1 5 8 16 21 24 25 26 27 28 */;
    s->pci_express_completion_timeout_register = 0x2710 << 0 | 0x0 << 16;
    s->pci_express_flow_control_register = 0x0 << 0 | 0x8 << 8 | 0x0 << 16 | 0x78 << 24;
    s->pci_express_acknowledge_timers_1x_register = 0x4 << 0 | 0x320 << 16;
    s->pci_express_debug_control_register = 0x0 << 0 | 0x1 << 16 | 0x17 << 1 | 0x0 << 0 | 0x1 << 19 | 0x0 << 20;
    s->pci_express_tl_control_register = 0x0 << 0;
    s->port0_usb_2_0_id = 0x0;
    s->port0_usb_2_0_hwgeneral = 0x0;
    s->port0_usb_2_0_hwhost = 0x0;
    s->port0_usb_2_0_hwdevice = 0x0;
    s->port0_usb_2_0_hwtxbuf = 0x0;
    s->port0_usb_2_0_hwrxbuf = 0x0;
    s->port0_usb_2_0_hwtttxbuf = 0x0;
    s->port0_usb_2_0_hwttrxbuf = 0x0;
    s->port0_usb_2_0_caplength = 0x0;
    s->port0_usb_2_0_hciversion = 0x0;
    s->port0_usb_2_0_hcsparams = 0x0;
    s->port0_usb_2_0_hccparams = 0x0;
    s->port0_usb_2_0_dciversion = 0x0;
    s->port0_usb_2_0_dccparams = 0x0;
    s->port0_usb_2_0_usbcmd = 0x0;
    s->port0_usb_2_0_usbsts = 0x0;
    s->port0_usb_2_0_usbintr = 0x0;
    s->port0_usb_2_0_frindex = 0x0;
    s->port0_usb_2_0_periodiclistbase__or__device_addr = 0x0;
    s->port0_usb_2_0_asynclistaddr__or__endpointlist_addr = 0x0;
    s->port0_usb_2_0_ttctrl = 0x0;
    s->port0_usb_2_0_burstsize = 0x0;
    s->port0_usb_2_0_txfilltuning = 0x0;
    s->port0_usb_2_0_txttfilltuning = 0x0;
    s->port0_usb_2_0_configflag = 0x0;
    s->port0_usb_2_0_portsc1 = 0x0;
    s->port0_usb_2_0_otgsc = 0x0;
    s->port0_usb_2_0_usbmode = 0x0;
    s->port0_usb_2_0_enpdtsetupstat = 0x0;
    s->port0_usb_2_0_endptprime = 0x0;
    s->port0_usb_2_0_endptflush = 0x0;
    s->port0_usb_2_0_endptstatus = 0x0;
    s->port0_usb_2_0_endptcomplete = 0x0;
    s->port0_usb_2_0_endptctrl0 = 0x0;
    s->port0_usb_2_0_endptctrl1 = 0x0;
    s->port0_usb_2_0_endptctrl2 = 0x0;
    s->port0_usb_2_0_endptctrl3 = 0x0;
    s->port0_usb_2_0_bridge_control_register = 0x0;
    s->port0_usb_2_0_bridge_interrupt_cause_register = 0x0;
    s->port0_usb_2_0_bridge_interrupt_mask_register = 0x0;
    s->port0_usb_2_0_bridge_error_address_register = 0x0;
    s->port0_usb_2_0_window0_control_register = 0x0;
    s->port0_usb_2_0_window0_base_register = 0x0;
    s->port0_usb_2_0_window1_control_register = 0x0;
    s->port0_usb_2_0_window1_base_register = 0x0;
    s->port0_usb_2_0_window2_control_register = 0x0;
    s->port0_usb_2_0_window2_base_register = 0x0;
    s->port0_usb_2_0_window3_control_register = 0x0;
    s->port0_usb_2_0_window3_base_register = 0x0;
    s->port0_usb_2_0_power_control_register = 0x0;
    s->phy_address = 0x0;
    s->smi = 0x0;
    s->ethernet_unit_default_address_euda = 0x0;
    s->ethernet_unit_default_id_eudid = 0x0;
    s->ethernet_unit_reserved_eu = 0x0;
    s->ethernet_unit_interrupt_cause_euic = 0x0;
    s->ethernet_unit_interrupt_mask_euim = 0x0;
    s->ethernet_unit_error_address_euea = 0x0;
    s->ethernet_unit_internal_address_error_euiae = 0x0;
    s->ethernet_unit_port_pads_calibration_eupcr = 0x0;
    s->ethernet_unit_control_euc = 0x0;
    s->base_address_0_ba0 = 0x0;
    s->size_s_0_sr0 = 0x0;
    s->base_address_1_ba1 = 0x0;
    s->size_s_1_sr1 = 0x0;
    s->base_address_2_ba2 = 0x0;
    s->size_s_2_sr2 = 0x0;
    s->base_address_3_ba3 = 0x0;
    s->size_s_3_sr3 = 0x0;
    s->base_address_4_ba4 = 0x0;
    s->size_s_4_sr4 = 0x0;
    s->base_address_5_ba5 = 0x0;
    s->size_s_5_sr5 = 0x0;
    s->high_address_remap_ha_harr0 = 0x0;
    s->high_address_remap_ha_harr1 = 0x0;
    s->high_address_remap_ha_harr2 = 0x0;
    s->high_address_remap_ha_harr3 = 0x0;
    s->base_address_enable_bare = 0x0;
    s->ethernet_port_access_protect_epap = 0x0;
    s->port_configuration_gec = 0x0;
    s->port_configuration_extend_gecx = 0x0;
    s->mii_serial_parameters = 0x0;
    s->gmii_serial_parameters = 0x0;
    s->vlan_ethertype_evlane = 0x0;
    s->mac_address_low_macal = 0x0;
    s->mac_address_high_macah = 0x0;
    s->sdma_configuration_sdc = 0x0;
    s->ip_differentiated_services_codepoint_0_to_priority_dscp0 = 0x0;
    s->ip_differentiated_services_codepoint_1_to_priority_dscp1 = 0x0;
    s->ip_differentiated_services_codepoint_2_to_priority_dscp2 = 0x0;
    s->ip_differentiated_services_codepoint_23_to_priority_dscp3 = 0x0;
    s->ip_differentiated_services_codepoint_24_to_priority_dscp4 = 0x0;
    s->ip_differentiated_services_codepoint_25_to_priority_dscp5 = 0x0;
    s->ip_differentiated_services_codepoint_6_to_priority_dscp6 = 0x0;
    s->port_serial_control_psc = 0x0;
    s->vlan_priority_tag_to_priority_vpt2p = 0x0;
    s->ethernet_port_status_ps = 0x0;
    s->transmit_queue_command_tqc = 0x0;
    s->maximum_transmit_unit_mtu = 0x0;
    s->port_interrupt_cause_ic = 0x0;
    s->port_interrupt_cause_extend_ice = 0x0;
    s->port_interrupt_mask_pim = 0x0;
    s->port_extend_interrupt_mask_peim = 0x0;
    s->port_rx_fifo_urgent_threshold_prfut = 0x0;
    s->port_tx_fifo_urgent_threshold_ptfut = 0x0;
    s->port_rx_minimal_frame_size_pmfs = 0x0;
    s->port_rx_discard_frame_counter_gedfc = 0x0;
    s->port_overrun_frame_counter_pofc = 0x0;
    s->port_internal_address_error_euiae = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q0 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q1 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q2 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q3 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q4 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q5 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q6 = 0x0;
    s->ethernet_current_receive_descriptor_pointers_crdp_q7 = 0x0;
    s->receive_queue_command_rqc = 0x0;
    s->transmit_current_served_descriptor_pointer = 0x0;
    s->transmit_current_queue_descriptor_pointer_tcqdp_q0 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q0 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q0 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q0 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q1 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q1 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q1 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q2 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q2 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q2 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q3 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q3 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q3 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q4 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q4 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q4 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q5 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q5 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q5 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q6 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q6 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q6 = 0x0;
    s->transmit_queue_token_bucket_counter_tqxtbc_q7 = 0x0;
    s->transmit_queue_token_bucket_configuration_tqxtbc_q7 = 0x0;
    s->transmit_queue_arbiter_configuration_tqxac_q7 = 0x0;
    s->mac_mib_countersnterrupt_cause_register = 0x0;
    s->destination_address_filter_special_multicast_table_dfsmt = 0x0;
    s->destination_address_filter_other_multicast_table_dfut = 0x0;
    s->destination_address_filter_unicast_table_dfut = 0x0;
    s->des_data_out_low_register = 0x0;
    s->des_data_out_high_register = 0x0;
    s->des_data_buffer_low_register = 0x0;
    s->des_data_buffer_high_register = 0x0;
    s->des_initial_value_low_register = 0x0;
    s->des_initial_value_high_register = 0x0;
    s->des_key0_low_register = 0x0;
    s->des_key0_high_register = 0x0;
    s->des_key1_low_register = 0x0;
    s->des_key1_high_register = 0x0;
    s->des_key2_low_register = 0x0;
    s->des_key2_high_register = 0x0;
    s->des_command_register = 0x0;
    s->sha_1_or_md5_data_in_register = 0x0;
    s->sha_1_or_md5_bit_count_low_register = 0x0;
    s->sha_1_or_md5_bit_count_high_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_a_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_b_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_c_register = 0x0;
    s->sha_1_or_md5_initial_value_or_digest_d_register = 0x0;
    s->sha_1_initial_value_or_digest_e_register = 0x0;
    s->sha_1_or_md5_authentication_command_register = 0x0;
    s->aes_encryption_data_in_or_out_column_3_register = 0x0;
    s->aes_encryption_data_in_or_out_column_2_register = 0x0;
    s->aes_encryption_data_in_or_out_column_1_register = 0x0;
    s->aes_encryption_data_in_or_out_column_0_register = 0x0;
    s->aes_encryption_key_column_3_register = 0x0;
    s->aes_encryption_key_column_2_register = 0x0;
    s->aes_encryption_key_column_1_register = 0x0;
    s->aes_encryption_key_column_0_register = 0x0;
    s->aes_encryption_key_column_7_register = 0x0;
    s->aes_encryption_key_column_6_register = 0x0;
    s->aes_encryption_key_column_5_register = 0x0;
    s->aes_encryption_key_column_4_register = 0x0;
    s->aes_encryption_command_register = 0x0;
    s->aes_decryption_data_in_or_out_column_3_register = 0x0;
    s->aes_decryption_data_in_or_out_column_2_register = 0x0;
    s->aes_decryption_data_in_or_out_column_1_register = 0x0;
    s->aes_decryption_data_in_or_out_column_0_register = 0x0;
    s->aes_decryption_key_column_3_register = 0x0;
    s->aes_decryption_key_column_2_register = 0x0;
    s->aes_decryption_key_column_1_register = 0x0;
    s->aes_decryption_key_column_0_register = 0x0;
    s->aes_decryption_key_column_7_register = 0x0;
    s->aes_decryption_key_column_6_register = 0x0;
    s->aes_decryption_key_column_5_register = 0x0;
    s->aes_decryption_key_column_4_register = 0x0;
    s->aes_decryption_command_register = 0x0;
    s->security_accelerator_command_register = 0x0;
    s->security_accelerator_descriptor_pointer_session_0_register = 0x0;
    s->security_accelerator_descriptor_pointer_session_1_register = 0x0;
    s->security_accelerator_configuration_register = 0x0;
    s->security_accelerator_status_register = 0x0;
    s->cryptographic_engines_and_security_accelerator_interrupt_cause_register = 0x0;
    s->cryptographic_engines_and_security_accelerator_interrupt_mask_register = 0x0;
}

static void wrt350n_v2_init(MachineState *machine)
{
    WRT350NV2State *s = g_new0(WRT350NV2State, 1);
    Error *err = NULL;
    DriveInfo *dinfo;
    static struct arm_boot_info binfo;

    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    object_initialize(&s->ic, sizeof(s->ic), TYPE_MV88F5181L_IC);
    qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, 0xf1020200);
    object_initialize(&s->bridge, sizeof(s->bridge), TYPE_MV88F5181L_BRIDGE);
    qdev_set_parent_bus(DEVICE(&s->bridge), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->bridge), 0, 0xf1020100);
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->bridge), 0, qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 0));
    object_initialize(&s->timer, sizeof(s->timer), TYPE_MV88F5181L_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, 0xf1020300);
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 0, qdev_get_gpio_in_named(DEVICE(&s->bridge), BRIDGE_IRQ, 1));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 1, qdev_get_gpio_in_named(DEVICE(&s->bridge), BRIDGE_IRQ, 2));
    serial_mm_init(get_system_memory(), 0xf1012000, 2, qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 3), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    dinfo = drive_get(IF_PFLASH, 0, 0);
    pflash_cfi01_register(0xf4000000, "flash", 8 * MiB, dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 64 * KiB, 4, 0, 0, 0, 0, 0);

    memory_region_init_io(&s->mv88f5181l_gpio_mmio, NULL, &mv88f5181l_gpio_ops, s, TYPE_WRT350N_V2, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010100, &s->mv88f5181l_gpio_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_cpu_address_map_mmio, NULL, &mv88f5181l_cpu_address_map_ops, s, TYPE_WRT350N_V2, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1020000, &s->mv88f5181l_cpu_address_map_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_ddr_sdram_controller_mmio, NULL, &mv88f5181l_ddr_sdram_controller_ops, s, TYPE_WRT350N_V2, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1001400, &s->mv88f5181l_ddr_sdram_controller_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_pins_multiplexing_interface_mmio, NULL, &mv88f5181l_pins_multiplexing_interface_ops, s, TYPE_WRT350N_V2, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010000, &s->mv88f5181l_pins_multiplexing_interface_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_pci_interface_mmio, NULL, &mv88f5181l_pci_interface_ops, s, TYPE_WRT350N_V2, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1030000, &s->mv88f5181l_pci_interface_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_pcie_interface_mmio, NULL, &mv88f5181l_pcie_interface_ops, s, TYPE_WRT350N_V2, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1040000, &s->mv88f5181l_pcie_interface_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_usb_2_0_controller_mmio, NULL, &mv88f5181l_usb_2_0_controller_ops, s, TYPE_WRT350N_V2, 0x500);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1050000, &s->mv88f5181l_usb_2_0_controller_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_gigabit_ethernet_controller_mmio, NULL, &mv88f5181l_gigabit_ethernet_controller_ops, s, TYPE_WRT350N_V2, 0x2000);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1072000, &s->mv88f5181l_gigabit_ethernet_controller_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_cesa_mmio, NULL, &mv88f5181l_cesa_ops, s, TYPE_WRT350N_V2, 0x200);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf109DD00, &s->mv88f5181l_cesa_mmio, 0);

    wrt350n_v2_reset(s);

    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    binfo.board_id = 0x661;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}

static void wrt350n_v2_machine_init(MachineClass *mc)
{
    /* mc->family = ; */
    /* mc->name = "wrt350n_v2"; */
    /* mc->alias = ; */
    mc->desc = "Linksys WRT350N v2 (MV88F5181L)";
    /* mc->deprecation_reason = ; */
    mc->init = wrt350n_v2_init;
    /* mc->reset = ; */
    /* mc->hot_add_cpu = ; */
    /* mc->kvm_type = ; */
    /* mc->block_default_type = ; */
    /* mc->units_per_default_bus = ; */
    /* mc->max_cpus = ; */
    /* mc->min_cpus = ; */
    /* mc->default_cpus = ; */
    /* mc->no_serial = 1; */
    /* mc->no_paralled = 1; */
    /* mc->no_floppy = 1; */
    /* mc->no_cdrom = 1; */
    /* mc->no_sdcard = 1; */
    /* mc->pci_allow_0_address = 1; */
    /* mc->legacy_fw_cfg_order = 1; */
    /* mc->is_default = ; */
    /* mc->default_machine_opts = ; */
    /* mc->default_boot_order = ; */
    /* mc->default_display = ; */
    /* mc->compat_props = ; */
    /* mc->hw_version = ; */
    mc->default_ram_size = 32 * MiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm926");
    /* mc->default_kernel_irqchip_split = ; */
    /* mc->option_rom_has_mr = ; */
    /* mc->minimum_page_bits = ; */
    /* mc->has_hotpluggable_cpus = ; */
    mc->ignore_memory_transaction_failures = true;
    /* mc->numa_mem_align_shift = ; */
    /* mc->valid_cpu_types = ; */
    /* mc->allowed_dynamic_sysbus_devices = ; */
    /* mc->auto_enable_numa_with_memhp = ; */
    /* mc->numa_auto_assign_ram = ; */
    /* mc->ignore_boot_device_suffixes = ; */
    /* mc->smbus_no_migration_support = ; */
    /* mc->nvdimm_supported = ; */
    /* mc->get_hotplug_handler = ; */
    /* mc->cpu_index_to_instance_props = ; */
    /* mc->CPuArchIdList = ; */
    /* mc->get_default_cpu_node_id = ; */
}

DEFINE_MACHINE("wrt350n_v2", wrt350n_v2_machine_init)