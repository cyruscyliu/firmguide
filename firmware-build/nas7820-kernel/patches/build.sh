#!/usr/bin/env bash

# update the packages
target="./chaos_camler_1505_oxnas"
cd $target
./scripts/feeds update -a
./scripts/feeds install -a
# cp feeds_packages_utils_bc.Makefile ./feeds/packages/utils/bc/Makefile
make -j4 V=s
