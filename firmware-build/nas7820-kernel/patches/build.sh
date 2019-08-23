# update the packages
target="./chaos_camler_1505_oxnas"
cd $target
./scripts/feeds update -a
./scripts/feeds install -a
make -j8 V=99
