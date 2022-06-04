#!/bin/bash

while getopts f: flag
do
    case "${flag}" in
        f) filename=${OPTARG};;
    esac
done

cd /home/ubuntu/python_telegram_services

source /home/ubuntu/python_telegram_services/venv3/bin/activate

python3 /home/ubuntu/python_telegram_services/src/$filename