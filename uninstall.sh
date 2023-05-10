#!/bin/bash

TARGET_PATH="/home/opt/mlab-to-extxyz"
LINK_PATH="/usr/local/bin/mlab-to-extxyz"

if [ -d $LINK_PATH ]; then
    sudo rm -f $LINK_PATH
fi

if [ -d $TARGET_PATH ]; then
    sudo rm -rf $TARGET_PATH
fi