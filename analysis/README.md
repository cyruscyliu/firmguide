# analysis module

put analysis scripts here

## extraction

### by binwalk
+ requirements
    - firmware.working_dir NOT NONE
    - firmware.working_path NOT NONE
    - firmware.size  NOT NONE
+ settings
    - firmware.image_type = see conventions below
    - firmware.image_path = extracted_path
 
 ### by uboot tools
 + requirements
    - firmware.image_type 'fit uImage' OR 'legacy uImage'
    - firmware.image_path NOT NONE
 + settings
    - firmware.kernel
    - firmware.dtb = NONE if 'lagacy uImage'

### by lzma tools
+ requirements
    - firmware.image_type 'trx kernel'
    - firmware.image_path NOT NONE
+ settings
    - firmware.kernel
    - firmware.dtb = NONE
    
## metadata

### by file
+ requirements
    - firmware.image_type 'legacy uImage'
    - firmware.image_path NOT NONE
+ settings
    - firmware.metadata
        + kernel_version: 1
        + os: 1
        + arch: 1
        + kernel_created_time: 1
        + kernel_load_address: 1
        + kernel_entry_point: 1  
        
### by dumpimage
+ requirements
    - firmware.image_type 'fit uImage'
    - firmware.image_path NOT NONE
+ settings
    - firmware.metadata
        + created_time: 1
        + os: 1
        + arch: 1
        + kernel_load_address: 1
        + kernel_entry_point: 1
        + brand: 1
        + kernel_version: 1

### by kernel version
+ requirements
    - firmware.metadata.kernel_version
+ settings
    - firmware.openwrt_revision

### by device tree
+ requirements
    - firmware.dtb NOT NONE
    - firmware.openwrt_revision
+ settings
    - firmware.openwrt
    - firmware.most_possible_target
    - firmware.most_possible_subtarget

### by strings
+ requirements
    - firmware.kernel
    - firmware.most_possible_target
    - firmware.openwrt_revision
+ settings
    - firmware.metadata
        + possible_targets
        + possible_subtargets
    - firmware.most_possible_target
    - firmware.most_subpossible_target
    - firmware.openwrt
    
    
## conventions

### firmware.image_type
|support|convention name|
|:---:|:---:|
|legacy uImage|legecy uImage|
|FIT uImage|fit uImage|
|TRX image|trx kernel|


