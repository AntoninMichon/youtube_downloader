#!/usr/bash

echo  "Are you sure os module is not installed ? In Linux distribution it is installed by default [y/n]"
read ask
if [ $ask == y ]; then
    pip install platform
else
    exit
if