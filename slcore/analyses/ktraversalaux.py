files_whitelist = [
    'init/main.c',
    'arch/arm/kernel/setup.c',
    'arch/arm/kernel/irq.c',
    'arch/arm/kernel/time.c',
    'arch/mips/kernel/setup.c',
    'arch/mips/kernel/irq.c',
    'arch/mips/kernel/time.c',
    'arch/mips/kernel/csrc-r4k.c',
    'arch/mips/kernel/cevt-r4k.c',
    'arch/mips/kernel/irq_cpu.c',
    'drivers/irqchip/irqchip.c',
    'drivers/of/irq.c',
    'drivers/clocksource/clksrc-of.c',
    'drivers/clk/clk-fixed-rate.c',
    'drivers/clk/clk-fixed-factor.c',
]


dirs_blacklist = [
    'include', '.pc', 'samples', 'patches', 'user_headers', 'tools',
    'Documentation', 'usr', 'scripts', 'virt'
]


funccalls_blacklist = [
    'early_init_dt_scan', 'of_flat_dt_get_machine_name', 'of_scan_flat_dt',
    'kmemdup', 'kfree', 'msleep', '__builtin_memcmp', 'add_memory_region', 'detect_memory_region',
    'clk_get_rate', 'clk_put', 'sprintf',  '__udelay',
    '__builtin_memset', 'pcibios_init', 'ipc_ns_init', 'init_mmap_min_addr', 'net_ns_init',
    'wq_sysfs_init', 'ksysfs_init', 'init_jiffies_clocksource', 'init_zero_pfn', 'fsnotify_init',
    'filelock_init', 'init_script_binfmt', 'init_elf_binfmt', 'debugfs_init', 'prandom_init',
    'sock_init', 'netlink_proto_init', 'bdi_class_init', 'mm_sysfs_init', 'kobject_uevent_init',
    'gpiolib_sysfs_init', 'pcibus_class_init', 'pci_driver_init', 'tty_class_init', 'pi_init',
    'i2c_init', 'frame_info_init', 'debugfs_mips', 'signal_setup', 'trap_pm_init', 'r4k_cache_init_pm',
    'r4k_tlb_init_pm', 'topology_init', 'init_vdso', 'uid_cache_init', 'param_sysfs_init', 'pm_sysrq_init',
    'default_bdi_init', 'percpu_enable_async', 'init_reserve_notifier', 'init_admin_reserve',
    'init_user_reserve', 'cryptomgr_init', 'init_bio', 'blk_settings_init', 'blk_ioc_init',
    'blk_softirq_init', 'blk_iopoll_setup', 'blk_mq_init', 'genhd_device_init', 'gpiolib_debugfs_init',
    'nxp_74hc153_init', 'pcf857x_init', 'pci_slot_init', 'misc_init', 'dma_buf_init', 'mtdsplit_seama_init',
    'mtdsplit_squashfs_init', 'mtdsplit_lzma_init', 'phy_init', 'i2c_gpio_init', 'watchdog_init', 'leds_init',
    'proto_init', 'net_dev_init', 'neigh_init', 'fib_rules_init', 'pktsched_init', 'tc_filter_init',
    'tc_action_init', 'genl_init', 'wireless_nlevent_init', 'mips_dma_init', 'clocksource_done_booting',
    'init_pipe_fs', 'eventpoll_init', 'anon_inode_init', 'proc_cmdline_init', 'proc_consoles_init',
    'proc_cpuinfo_init', 'proc_devices_init', 'proc_interrupts_init', 'proc_loadavg_init', 'proc_meminfo_init',
    'proc_stat_init', 'proc_uptime_init', 'proc_version_init', 'proc_softirqs_init', 'proc_kmsg_init',
    'init_ramfs_fs', 'blk_scsi_ioctl_init', 'chr_dev_init', 'firmware_class_init', 'sysctl_core_init',
    'inet_init', 'ipv4_offload_init', 'af_unix_init', 'ipv6_offload_init', 'debugfs_unaligned', 'segments_info',
    'proc_execdomains_init', 'ioresources_init', 'init_posix_timers', 'init_posix_cpu_timers',
    'timekeeping_init_ops', 'init_clocksource_sysfs', 'init_timer_list_procfs', 'alarmtimer_init',
    'clockevents_init_sysfs', 'init_tstats_procfs', 'futex_init', 'proc_modules_init', 'kallsyms_init',
    'utsname_sysctl_init', 'crashlog_init_fs', 'init_per_zone_wmark_min', 'kswapd_init', 'setup_vmstat',
    'workingset_init', 'proc_vmalloc_init', 'procswaps_init', 'slab_sysfs_init', 'fcntl_init',
    'proc_filesystems_init', 'dio_init', 'fsnotify_mark_init', 'inotify_user_setup', 'proc_locks_init',
    'init_devpts_fs', 'init_squashfs_fs', 'init_jffs2_fs', 'ovl_init', 'ipc_init', 'ipc_sysctl_init',
    'key_proc_init', 'crypto_algapi_init', 'aes_init', 'proc_genhd_init', 'noop_init', 'deadline_init',
    'phy_core_init', 'pci_proc_init', 'pty_init', 'sysrq_init', 'serial8250_init', 'topology_sysfs_init',
    'init_mtd', 'mtdsplit_uimage_init', 'redboot_parser_init', 'cmdline_parser_init', 'myloader_mtd_parser_init',
    'tplink_parser_init', 'cybertan_parser_init', 'init_mtdblock', 'cfi_probe_init', 'physmap_init', 'm25p80_driver_init',
    'net_olddevs_init', 'swconfig_init', 'marvell_init', 'rtl_init', 'ksphy_init', 'gpio_led_driver_init',
    'timer_trig_init', 'defon_trig_init', 'netdev_trig_init', 'staging_init', 'llc_init', 'snap_init',
    'blackhole_module_init', 'fq_codel_module_init', 'gre_offload_init', 'sysctl_ipv4_init', 'ipv4_netfilter_init',
    'cubictcp_register', 'packet_init', 'br_init', 'br_netfilter_init', 'dsa_init_module', 'vlan_proto_init',
    'init_oops_id', 'pm_qos_power_init', 'printk_late_init', 'tk_debug_sleep_time_init', 'fault_around_debugfs',
    'init_root_keyring', 'prandom_reseed', 'pci_resource_alignment_sysfs_init', 'pci_sysfs_init',
    'deferred_probe_initcall', 'tcp_congestion_default', 'ar933x_uart_init', 'ap83_spi_init', 'ath79_spi_driver_init',
    'ip17xx_init', 'ar8xxx_init', 'rtl8366s_module_init', 'rtl8366rb_module_init', 'rtl8367_module_init', 'atheros_init',
    'mv88e6060_init', 'mv88e6063_init', 'ag71xx_module_init', 'ath79_wdt_driver_init', 'strlcpy', 'printk',
    'irq_create_mapping', 'of_address_to_resource', 'of_property_read_u32_array', 'irq_of_parse_and_map',
    'irq_set_handler_data', 'arch_mem_addpart', 'print_memory_map', 'mips_parse_crashkernel', 'bootmem_init',
    'cpu_report', 'check_bugs_early', 'resource_init', 'plat_smp_setup', 'prefill_possible_map', 'cpu_cache_init',
    'paging_init', 'device_tree_init', 'strlcat', 'set_isa', 'decode_configs', 'spram_config',
    'setup_early_printk', 'cpu_probe', 'cp0_compare_irq', 'c0_compare_int_usable',
    'clockevent_delta2ns', 'clocks_calc_mult_shift', 'get_c0_compare_int', 'irq_modify_status',
    'cpu_has_mfc0_count_bug', 'debugfs_create_file', 'of_find_compatible_node', 'of_platform_populate',
    'reset_controller_register', 'early_init_dt_verify', 'of_flat_dt_match_machine', 'sanity_check_meminfo',
    'setup_processor', 'request_standard_resources', 'smp_build_mpidr_hash', 'setup_machine_fdt', 'parse_early_param',
    'sanity_check_meminfo', 'arm_memblock_init', 'unflatten_device_tree', 'arm_dt_init_cpu_maps',
    'init_static_idmap', 'ptrace_break_init', 'twd_clk_init', 'atomic_pool_init', 'exceptions_init', 'proc_cpu_init', 'alignment_init',
    'early_init_fdt_scan_reserved_mem', 'early_init_fdt_scan_reserved_mem', 'of_count_phandle_with_args',
    'of_property_read_u32_index', 'of_parse_phandle_with_args', 'mips_set_machine_name'
    'early_init_fdt_reserve_self', 'of_property_count_elems_of_size', 'of_find_property', 'of_property_read_variable_u32_array',
    'warn_slowpath_null', 'vprintk', 'mutex_lock', 'of_get_cpu_node', 'mips_sysrq_init', 'pcibios_set_cache_line_size',
    'of_iomap', 'irq_set_chip_data', 'of_clk_get', 'of_irq_count', 'of_get_property', 'of_get_parent', '_raw_spin_lock_irqsave',
    'of_find_node_by_phandle', 'arch_local_irq_save', 'arch_local_irq_restore', 'of_irq_parse_raw', 'of_irq_parse_one',
    'of_irq_find_parent', '_raw_spin_unlock_irqrestore', '__iounmap', 'irq_get_irq_data', 'warn_slowpath_fmt', 'irq_domain_disassociate',
    'irq_free_descs', 'schedule', '__request_region', 'alloc_resource', '__request_resource', 'free_resource',
    'irq_domain_remove', 'irq_domain_update_bus_token', '__cpuhp_setup_state', 'cpus_read_lock', 'printk_deferred',
    'set_task_stack_end_magic', 'smp_setup_processor_id', 'boot_cpu_init', 'current_thread_info', 'set_cpu_online', 'set_cpu_active',
    'set_cpu_present', 'set_cpu_possible', 'mm_init_cpumask', 'mangle_bootargs', 'setup_command_line', 'strlen',
    'memblock_virt_alloc_try_nid', 'memblock_virt_alloc_try_nid', 'memblock_virt_alloc_try_nid', 'memblock_virt_alloc',
    'memblock_virt_alloc', 'memblock_virt_alloc', 'strcpy', 'setup_nr_cpu_ids', 'setup_per_cpu_areas',
    'smp_prepare_boot_cpu', 'build_all_zonelists', 'page_alloc_init', 'parse_early_options', 'parse_args', 'parse_args',
    'parse_args', 'IS_ERR_OR_NULL', 'jump_label_init', 'setup_log_buf', 'pidhash_init', 'vfs_caches_init_early', 'sort_main_extable',
    'trap_init', 'mm_init', 'page_cgroup_init_flatmem', 'mem_init', 'kmem_cache_init', 'percpu_init_late', 'pgtable_init', 'vmalloc_init',
    'sched_init', 'arch_irqs_disabled_flags', 'arch_irqs_disabled_flags', 'idr_init_cache', 'rcu_init', 'context_tracking_init',
    'radix_tree_init', 'early_irq_init', 'tick_init', 'rcu_init_nohz', 'init_timers', 'hrtimers_init', 'softirq_init', 'timekeeping_init',
    'sched_clock_postinit', 'profile_init', 'call_function_init', 'kmem_cache_init_late', 'console_init', 'kmemleak_init',
    'setup_per_cpu_pageset', 'numa_policy_init', 'sched_clock_init', 'calibrate_delay', 'pidmap_init', 'anon_vma_init',
    'acpi_early_init', 'thread_info_cache_init', 'cred_init', 'fork_init', 'proc_caches_init', 'buffer_init', 'key_init',
    'security_init', 'vfs_caches_init', 'signals_init', 'page_writeback_init', 'proc_root_init', 'delayacct_init', 'check_writebuffer_bugs',
    'ftrace_init', 'rcu_scheduler_starting', 'numa_default_policy', 'rcu_read_lock', 'find_task_by_pid_ns',
    'rcu_read_unlock', 'complete', 'current_thread_info', 'init_idle_bootup_task', 'schedule_preempt_disabled', 'cpu_startup_entry',
    'read_cpuid_id', 'lookup_processor_type', 'early_paging_init', 'setup_dma_zone', 'psci_init', 'is_smp', 'is_smp',
    'smp_set_ops', 'smp_init_cpus', 'hyp_mode_check', 'reserve_crashkernel', 'vsnprintf', 'early_print',
    'INIT_LIST_HEAD', 'INIT_LIST_HEAD', 'of_find_matching_node_and_match', 'of_find_matching_node_and_match',
    'of_find_matching_node', 'of_find_matching_node', 'of_device_is_available', 'kmem_cache_alloc', 'kzalloc',
    'list_empty', 'list_empty', '__list_del', '__list_del', '__list_del', '__list_del', 'list_del', 'list_del',
    'list_del', 'list_del', 'of_match_node', 'no_printk', 'of_property_read_u32', 'of_property_read_u32', 'numa_node_id', 
    '__irq_alloc_descs', 'set_smp_cross_call', 'register_cpu_notifier', 'gic_get_cpumask', 'gic_dist_config', 'gic_get_cpumask',
    'gic_cpu_config', 'gic_cpu_if_up', '__alloc_percpu', '__alloc_percpu', 'cpu_pm_register_notifier',
    'numa_node_id', '__irq_alloc_descs', 'preempt_count', 'preempt_count', 'initcall_blacklisted', 'kasprintf',
    'strcmp', 'do_one_initcall_debug', 'task_pid_nr', 'ktime_get', 'ktime_get', 'preempt_count_ptr', 'lockup_detector_init',
    'smp_init', 'sched_init_smp', 'cpuset_init_smp', 'usermodehelper_init', 'shmem_init', 'driver_init', 'init_irq_proc', 'do_ctors',
    '__usermodehelper_set_disable_depth', 'usermodehelper_enable', 'preempt_count', 'preempt_count',
    'initcall_blacklisted', 'kasprintf', 'strcmp', 'do_one_initcall_debug', 'task_pid_nr', 'ktime_get', 'ktime_get', 'preempt_count_ptr',
    'random_int_secret_init', 'sys_open', 'sys_dup', 'sys_dup', 'sys_access', 'prepare_namespace', 'load_default_modules',
    'load_default_elevator_module', 'async_synchronize_full', 'free_initmem', 'mark_rodata_ro', 'flush_delayed_fput',
    'run_init_process', 'getname_kernel', 'do_execve', 'run_init_process', 'getname_kernel', 'do_execve', 'try_to_run_init_process',
    'run_init_process', 'getname_kernel', 'do_execve', 'try_to_run_init_process', 'run_init_process', 'getname_kernel',
    'do_execve', 'try_to_run_init_process', 'run_init_process', 'getname_kernel', 'do_execve', 'try_to_run_init_process',
    'run_init_process', 'getname_kernel', 'do_execve', 'try_to_run_init_process', 'run_init_process', 'getname_kernel', 'do_execve',
     'wait_for_completion', 'set_mems_allowed', 'set_cpus_allowed_ptr', 'task_pid', 'smp_prepare_cpus', 'do_pre_smp_initcalls', 'panic',
     '__raw_writel', '__raw_readl', 'aer_service_init', 'bgpio_driver_init', 'check_cpu_stall_init', 'clk_debug_init',
     'clk_disable_unused', 'cpu_pm_init', 'cpu_stop_init', 'cpucache_init', 'cpuidle_init', 'crypto_xz_mod_init', 'deflate_mod_init',
     'dma_bus_init', 'dma_channel_table_init', 'dma_debug_do_init', 'dnotify_init', 'dummy_timer_register', 'extfrag_debug_init',
     'gate_vma_init', 'gpio_poweroff_driver_init', 'hashlib_init', 'hung_task_init', 'icplus_init', 'inet_diag_init', 'init_ladder',
     'init_menu', 'init_scsi', 'init_sd', 'init_workqueues', 'input_init', 'ip_auto_config', 'jump_label_init_module',
     'lzo_mod_init', 'max_swapfiles_check', 'memblock_init_debugfs', 'migration_init', 'mm_compute_batch_init', 'nand_base_init',
     'of_init', 'of_platform_serial_driver_init', 'ofpart_parser_init', 'packet_diag_init', 'pci_apply_final_quirks', 'pcie_pme_service_init',
     'pcie_portdrv_init', 'pcs_driver_init', 'pinctrl_init', 'plat_nand_driver_init', 'pm_init', 'populate_rootfs', 'power_supply_class_init',
     'pps_init', 'ptp_init', 'pwm_debugfs_init', 'pwm_sysfs_init', 'rand_initialize', 'ras_init', 'rcu_spawn_gp_kthread', 'realtek_init',
     'regmap_initcall', 'relay_init', 'rtc_hctosys', 'rtc_init', 'sched_clock_syscore_init', 'serial8250_console_init', 'serial_pci_driver_init',
     'slab_proc_init', 'sock_diag_init', 'spawn_ksoftirqd', 'spi_init', 'stmmac_init', 'syscon_init', 'tcp_diag_init', 'ubi_init', 'ubifs_init',
     'usb_init', 'v6_userpage_init', 'kthreadd', 'IS_ERR', 'clk_prepare', 'clk_enable', 'clk_unprepare', 'clk_prepare_enable',  'free_percpu_irq',
     'IS_ERR', 'PTR_ERR', 'clk_prepare', 'clk_enable', 'clk_unprepare', 'clk_prepare_enable', '__my_cpu_offset', 'enable_percpu_irq',
     'enable_percpu_irq', 'get_jiffies_64', 'get_jiffies_64', 'get_jiffies_64', 'get_cpu_mask', '__arm_iounmap', 'free_percpu',
     'of_property_read_string', 'ERR_PTR', 'kmalloc', 'of_clk_add_provider', 'of_clk_get_parent_name', 'gic_dist_init', 'gic_cpu_init', 'gic_pm_init',
     'add_latent_entropy', 'add_device_randomness', 'get_random_bytes', 'boot_cpu_hotplug_init', 'early_trace_init', 'workqueue_init_early',
     'printk_safe_init', 'mem_encrypt_init', 'debug_objects_mem_init', 'thread_stack_cache_init', 'pagecache_init', 'nsfs_init',
     'check_bugs', 'acpi_subsystem_init', 'arch_post_acpi_subsys_init',  'setup_machine_tags', 'dump_stack_set_arch_desc', 'early_fixmap_init',
     'early_ioremap_init', 'early_mm_init', 'xen_early_init', 'adjust_lowmem_bounds', 'adjust_lowmem_bounds', 'early_ioremap_reset',
     'of_node_to_fwnode', '__irq_alloc_domain_generic_chips', 'irq_get_domain_generic_chip', 'resource_size', 'resource_size', 'ioremap',
     'of_node_to_fwnode', '__irq_alloc_domain_generic_chips', 'resource_size', 'resource_size', 'irq_get_domain_generic_chip', 'ioremap',
     'of_device_is_compatible', '__kmalloc', 'kmalloc_array', 'kcalloc', 'iounmap', 'atomic_io_modify', 'of_property_read_string_helper', 'ERR_CAST',
     'of_property_read_string_index', 'clk_disable_unprepare', 'clk_disable', 'page_address_init',  '__arm_ioremap', 'of_property_read_bool', 
     'read_cpuid_part', '__ioremap', '__ioremap_mode', 'rt_intc_w32', 'reserve_bootmem', 'clear_c0_cause', 'virt_to_phys',
     'check_bugs32', 'clockevent_set_clock', 'snprintf', 'plat_of_remap_node' 'arch_mem_init', 'set_io_port_base', 'dma_contiguous_reserve',
     '__div64_32', 'mips_cm_probe', '__BUG_ON', '___pa', '__dt_setup_arch', 'early_init_fdt_reserve_self', 'rdhwr_count_usable',
     '__get_free_pages', 'setup_early_fdc_console', 'rdhwr_count', 'reserve_bootmem_region', 'get_order', 'calculate_min_delta',
     'debug_objects_early_init', 'boot_init_stack_canary', 'cgroup_init_early', 'arch_local_irq_disable', 'arch_local_irq_disable',
     'psci_smp_available', 'obsolete_checksetup', 'cgroup_init', 'initcall_levels', 'efi_late_init', 'cpuset_init', 'sfi_init_late',
     'efi_free_boot_services', 'arch_local_save_flags', 'parameqn', 'obs_kernel_param.setup_func', 'strncmp',  '__builtin_expect',
     'arch_local_irq_enable', '__check_is_bitmap', 'strchr', 'taskstats_init_early', 'unknown_bootoption', 'efi_enabled', 'perf_event_init',
     'memmove', 'set_init_arg',  'page_cgroup_init',
]
