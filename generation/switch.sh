#!/bin/bash

set -e


[ "$1" = arm ] && {
	echo "switching to arm building env..."
	rm -rf config.yaml  machines  makefiles  template
	cp -r arm/* .
}

[ "$1" = mipsel ] && {
	echo "switching to mipsel building env..."
	rm -rf config.yaml  machines  makefiles  template
	cp -r mipsel/* .
}
