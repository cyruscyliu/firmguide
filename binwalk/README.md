# Binwalk

Binwalk is a fast, easy to use tool for analyzing, reverse engineering, and extracting firmware images.
Check the [repo](https://github.com/ReFirmLabs/binwalk) for more details.

However, Binwalk is not enough for our analysis. We want Binwalk to support the following features.

+ extract legacy uImage directly
+ extract FIT uImage directly

## install
see project [README.md](../README.md).

## start
Use binwalk as usual except, to support FIT uImage, adding --block size_in_byte to load all FIT uImage.

```shell script
binwalk --block size_in_byte path/to/firmware
```
