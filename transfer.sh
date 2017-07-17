#!/bin/bash

VECTOR_SIZE=36

# preper vector
echo "Prepering vector of $VECTOR_SIZE 0s and 1s"
for i in {1..$VECTOR_SIZE}; do
    VAL=$(shuf -i 0-1 -n 1)
    vector[$i]=$VAL
    echo $i
done

echo "Now, for each cell at vector, transfer stream"
for i in {1..$VECTOR_SIZE}; do
    echo $i
    if [ vector[$i] -eq 1 ]; then
        echo $i
    else
        echo $i
    fi
done




