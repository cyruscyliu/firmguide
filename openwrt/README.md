# Intro

Bash scripts extracting kernel .config file.

# Usage

Run `test.sh` to see how it basically runs.

```bash
bash test.sh
```

The `extract_kernel.sh` is the main entry, must provide first 8 parameters. 

```bash
bash extract_kernel.sh [params]...

##################################################################
#
# Params should be passed in:
# 1. openwrt version (like "10.03" or "15.05")
# 2. url for downloading or file path of openwrt.tar
# 3. url for downloading or file path of kernel.tar
# 4. url for downloading or file path of .config for openwrt
# 5. kernel detail version (like "2.6.32")
# 6. board info (like "orion")
# 7. subtarget info (string, but notice that pass "NULL" means "")
# 8. output directory (the final kernel source copy from work dir,
#                      if use relative path, it will base on
#                      the working directory;
#                      if pass "NULL", means "";)
# 9. working directory (if not set, will use "./${DEFAULT_WORK_DIR}"
#                       as default
#                       if default, will clean the ./${DEFAULT_WORK_DIR}
#                       first;
#                       NOTICE: will clean the target directory first)
#
##################################################################

```

