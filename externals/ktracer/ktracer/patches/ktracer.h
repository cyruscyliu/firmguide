#ifndef KTRACER_H
#define KTRACER_H


#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

#include "qemu/osdep.h"
#include "cpu.h"
//#include "trace.h"
//#include "disas/disas.h"
#include "exec/exec-all.h"
//#include "tcg.h"
//#include "qemu/atomic.h"
//#include "sysemu/qtest.h"
//#include "qemu/timer.h"
//#include "qemu/rcu.h"
//#include "exec/tb-hash.h"
//#include "exec/tb-lookup.h"
//#include "exec/log.h"
#include "exec/address-spaces.h"
//#include "qemu/main-loop.h"
//#include "sysemu/cpus.h"
//#include "sysemu/replay.h"


int before_block_exec(CPUState *cs, TranslationBlock *tb);

#endif

