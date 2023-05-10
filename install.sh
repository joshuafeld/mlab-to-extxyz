#!/bin/bash

TARGET_PATH="/home/opt/mlab-to-extxyz"
LINK_PATH="/usr/local/bin/mlab-to-extxyz"

chmod +x mlab-to-extxyz.py

cp mlab-to-extxyz.py mlab-to-extxyz

if [ -d $TARGET_PATH ]; then
    sudo rm -rf $TARGET_PATH
fi

sudo mkdir -p $TARGET_PATH

sudo cp *.py $TARGET_PATH/
sudo cp mlab-to-extxyz $TARGET_PATH/mlab-to-extxyz

if [ ! -d $LINK_PATH ]; then
    sudo rm $LINK_PATH
fi

sudo ln -s $TARGET_PATH/mlab-to-extxyz $LINK_PATH