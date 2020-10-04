#!/bin/bash

# Script is run by cron so we need to define environment, 
# which is different that for a user
PATH=/usr/bin:/bin:/usr/local/bin:/usr/local/share
python /home/pi/projects/speaking-clock/speak.py

