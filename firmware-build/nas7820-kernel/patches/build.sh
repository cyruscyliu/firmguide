#!/usr/bin/env bash

# update the packages
target="./chaos_camler_1505_oxnas"
cd $target
./scripts/feeds update -a
./scripts/feeds install -a
make -j4 V=s
