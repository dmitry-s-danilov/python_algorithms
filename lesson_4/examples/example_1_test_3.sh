#!/bin/bash

# an array length
m=100000
# an executions number
n=100

echo "array length: $m"
echo "execution number: $n"

for f in my_func_1 my_func_2 my_func_3
do
    echo "function: $f"
    python3 -m timeit -n $n -s "from example_1_lib import $f; $f(range($m))"
done
