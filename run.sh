#!/bin/bash
conda activate composite_wrapper_env
python run.py --username username --password password --granule_count 5 --lon_lat_minimum 130.0 65.0 --lon_lat_maximum 130.2 65.5
