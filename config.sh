#!/bin/bash


# 드라이버 설정
# instantclient_23_6 폴더가 존재하지 않는다면
if [ ! -d instantclient_23_6 ]; then
    wget "https://download.oracle.com/otn_software/linux/instantclient/2360000/instantclient-basic-linux.x64-23.6.0.24.10.zip"
    unzip instantclient-basic-linux.x64-23.6.0.24.10.zip
    rm -rf instantclient-basic-linux.x64-23.6.0.24.10.zip META-INF
fi