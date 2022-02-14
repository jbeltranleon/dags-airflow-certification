# Sensors

Sensors are a special type of Operator that are designed to do exactly one thing - wait for something to occur. It can be time-based, or waiting for a file, or an external event, but all they do is wait until something happens, and then succeed so their downstream tasks can run.


* `mode`: default `poke`, `reschedule` optimize resources usage 
* `exponential_backoff` increase the waiting time


### diff  between timeout and execution_timeout

`timeout` could use `soft_fail` but `execution_timeout` not