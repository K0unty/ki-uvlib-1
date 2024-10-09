#!/usr/bin/env bash 

set -euox pipefail

# Bash script for writing to image with artem

g1() {
    fi="k.jpeg"
    artem \
        $fi \
        -o k.ansi
}
g1