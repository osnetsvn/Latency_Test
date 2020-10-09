#!/bin/bash

# Run Cylictest in the kernel.

if [ $# -ne 2 ]; then
        echo "Usage: $0 <cpu> <duration>"
        exit 1
fi
cpu=$1
duration=$2


taskset -c $cpu make insert
sleep $duration
make remove
