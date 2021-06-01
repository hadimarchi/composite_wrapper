#!/bin/bash
echo 'Installing conda-pack'
conda install conda-pack

echo 'Installing composite wrapper environment to ./comp_wrapper_env'
mkdir -p comp_wrapper_env
tar -xzf comp_wrapper_env.tar.gz -C comp_wrapper_env

echo 'exit' || ./comp_wrapper_env/bin/python

source ./comp_wrapper_env/bin/activate

echo 'exit' || python
conda-unpack

echo 'Environment installed.'
