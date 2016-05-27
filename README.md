# cwbeacon

A Python prorgam for the Raspberry Pi that accepts a text string aand optionally a parameter specifying Characters Per Second, and keys a transceiver using an Open Collector transistor keying circuit.
To use as a periodic beacon, a cron job can be configured to run the program when required.

For example to beacon my callsign and grid-square every 5 minutes, I would add the following line to the crontab for user 'pi':

```
5,10,15,20,25,30,35,40,45,50,55,0 * * * * python /home/pi/cwbeacon/beacon.py -c 25 ei8drb io53mf
```

Dependencies: RPi.GPIO Python module

```
usage: CW Beacon Sender - uses GPIO pin [-h] [-c CPS] message [message ...]
CW Beacon Sender - uses GPIO pin: error: too few arguments
```
