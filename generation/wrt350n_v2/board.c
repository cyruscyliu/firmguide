#include "qemu/osdep.h"
#include "hw/arm/mv88f5181L.h"

static void wrt350n_v2_init(MachineState *machine) {

}

static void wrt350n_v2_machine_init(MachineClass *mc) {
    /* mc->family = ; */
    /* mc->name = ; */
    /* mc->alias = ; */
    mc->desc = "wrt350n_v2";
    mc->init = wrt350n_v2_init;
    mc->max_cpus = MV88F5181L_NCPUS;
    mc->min_cpus = MV88F5181L_NCPUS;
    mc->default_cpus = MV88F5181L_NCPUS;
    mc->default_ram_size = 1024 * 1024 * 1024;
}
DEFINE_MACHINE("wrt350n_v2", wrt350n_v2_machine_init)