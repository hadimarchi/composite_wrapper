#!/bin/bash
source ./comp_wrapper_env/bin/activate
python run.py --username username --password password --granule_count 5 --lon_lat_minimum 150.0 65.0 --lon_lat_maximum 150.2 65.5
