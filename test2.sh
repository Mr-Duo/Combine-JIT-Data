#!/bin/bash

rm -rf logs

git pull

python3 main.py \
    -data_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling/cross-lang \
    -output_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling