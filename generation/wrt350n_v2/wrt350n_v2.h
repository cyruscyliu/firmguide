/* 
 * automatically generated, don't change
 */

#ifndef WRT350N_V2_H
#define WRT350N_V2_H

#define WRT350N_V2_FLASH_ADDR      0xf4000000
#define WRT350N_V2_FLASH_SIZE      (8 * MiB)
#define WRT350N_V2_FLASH_SECT_SIZE (64 * KiB)

typedef struct WRT350N_V2State {
    MV88F5181LState soc;
    MemoryRegion ram;
    PFlashCFI01 *flash;
} WRT350N_V2State;

static const int wrt350n_v2_board_id = 0x661;

#endif /* WRT350N_V2_H */