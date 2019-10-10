# Intro

Bash scripts extracting kernel .config file.

# Usage

Run `test.sh` to see how it basically runs.

```bash
bash test.sh
```

The `extract_dot_config.sh` is the main entry, must provide first 8 parameters. 

```bash
bash extract_dot_config.sh [params]...

##################################################################
#
# Params should be passed in:
# 1. openwrt version (like "10.0.3" or "15.05")
# 2. url for downloading openwrt.tar
# 3. url for downloading kernel.tar
# 4. url for downloading .config for openwrt
# 5. kernel detail version (like "2.6.32")
# 6. board info (like "orion")
# 7. subtarget info (string, but notice that pass "NULL" means "")
# 8. output file name (the output file copy from final .config,
#                      if use relative path, it will base on
#                      the working directory)
# 9. working directory (if not set, will use "./build" as default
#                       if default, will clean the ./build first
#                       if set, assume it is an empty or not-exist
#                       dir)
#
##################################################################

```

