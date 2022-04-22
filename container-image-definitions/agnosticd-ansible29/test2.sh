#!/bin/bash
if [[ -p /dev/stdin ]]
then
    echo "stdin is coming from a pipe"
fi
if [[ -t 0 ]]
then
    echo "stdin is coming from the terminal"
fi
if [[ ! -t 0 && ! -p /dev/stdin ]]
then
    echo "stdin is redirected"
fi
read
echo "$REPLY"
