# Latency_Test

Author: Kevin Cheng(tcheng8@binghamton.edu) Roja Eswaran (reswara1@binghamton.edu) - OSNET Lab, Binghamton University 

Kernel Level Timer Interrupt Latency Test

How to use it?


1) ./kcyclictest.sh <cpu-id> <duration>

2) View the test result - cat /sys/kernel/debug/tracing/trace - The Last column is the latency value which is in nanoseconds.

3) Clean the test result - echo > /sys/kernel/debug/tracing/trace

# Cumulative Distribution Curve (CDC)

Author: Roja Eswaran (reswara1@binghamton.edu) - OSNET Lab, Binghamton University

You can use cdc.py to create CDC for your trace.

How to use it?

1) copy /sys/kernel/debug/tracing/trace to the same working directory as cdc.py

2) Run - python cdc.py 

3) Enter your trace name: "trace"  

4) The output result is stored in timer_CDC.csv - Output Format ( Latency in microseconds, Cumulative Distribution) 
