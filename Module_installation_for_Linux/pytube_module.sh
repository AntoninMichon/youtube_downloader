#!/usr/bash

echo "Do you want install Pytube module ? [y/n]git a"
read ask
if [ $ask == y ]; then
    pip install pytube
else
    exit
fi