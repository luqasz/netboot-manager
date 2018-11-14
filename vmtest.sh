#!/bin/sh

ISO=$1
BOOT_FILE=$2

qemu-system-x86_64 \
    -m 1024 \
    $ISO \
    -display sdl \
    -vga std \
    -netdev user,id=user0,bootfile=$BOOT_FILE,tftp=. \
    -device virtio-net-pci,netdev=user0
