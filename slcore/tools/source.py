from slcore.project import project_get_srcodec


def project_source_analysis(ep, **kwargs):
    """
    We simply preprocess the c file containing the entry point
    if no other arguments assigned.
    """
    srcodec = project_get_srcodec()

    # 1 symbol2file
    path_to_entry_point = srcodec.symbol2file(ep)
    if path_to_entry_point is None:
        path_to_entry_point = srcodec.symbol2fileg(ep)
        if path_to_entry_point is None:
            print('[-] cannot find {}'.format(ep))
            return
    print('[+] find {} in {}'.format(ep, path_to_entry_point))
    cmdline = srcodec.get_cmdline(path_to_entry_point)
    path_to_pentry_point = srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
    print('[+] preprocess and save as {}/{}'.format(srcodec.get_path_to_source_code(), path_to_pentry_point))

