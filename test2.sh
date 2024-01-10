#!/bin/bash

rm -rf logs

git pull

python3 main2.py \
    -single_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling/single-lang \
    -cross_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling/cross-lang \
    -output_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling