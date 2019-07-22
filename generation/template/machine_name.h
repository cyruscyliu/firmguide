{{license}}

#ifndef {{machine_name|upper}}_H
#define {{machine_name|upper}}_H

#define {{machine_name|upper}}_FLASH_ADDR      {{flash_addr}}
#define {{machine_name|upper}}_FLASH_SIZE      ({{flash_size}})
#define {{machine_name|upper}}_FLASH_SECT_SIZE ({{flash_sect_size}})

typedef struct {{machine_name|upper}}State {
    {{soc_name|upper}}State soc;
    MemoryRegion ram;
} {{machine_name|upper}}State;

static const int {{machine_name}}_board_id = {{board_id}};

#endif /* {{machine_name|upper}}_H */