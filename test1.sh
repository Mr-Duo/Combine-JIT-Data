#!/bin/bash

rm -rf logs

git pull

python3 main1.py \
    -data_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling/single-lang \
    -output_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling