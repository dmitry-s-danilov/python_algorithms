#!/bin/bash

# Measures execution time
# of specified python function
# for different argument values
# with python timeit module
# using command-line interface.

# function and arguments
MODULE='example_2_lib_fib' # python module
FUNC='fib_1' # module function
PARAMS=(0 1 2 3 4 5 10) # arguments list

# timeit options
NUMBER=1000 # executions number
REPEAT=10 # repeat count
UNIT=usec # time unit

printf 'python module: %s\n' $MODULE
printf 'module function: %s\n' $FUNC

printf 'executions number: %s\n' $NUMBER
printf 'repeat count: %s\n' $REPEAT
printf 'time unit: %s\n' $UNIT

printf '%s | %s\n' 'param' 'timeit'
for param in "${PARAMS[@]}"
do
  printf '%s | ' "$param"
  python3 -m timeit --process --number=$NUMBER --repeat=$REPEAT --unit=$UNIT \
  --setup="from $MODULE import $FUNC" "$FUNC($param)"
done
