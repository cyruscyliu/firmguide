#!/bin/bash

#set -x

dir=`realpath $0 | xargs dirname`
dirname=`basename $dir`
srv=`head -n 3 ${dir}/docker-compose.yml | tail -n 1 | awk -F: '{print $1}' | tr -d ' '`

docker exec -it `docker ps | grep $dirname | grep $srv | awk '{print $1}'` bash $1
