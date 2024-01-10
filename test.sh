#!/bin/bash

rm -rf logs

git pull

python3 main.py \
    -data_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling/truncated_median_date_tan_dataset \
    -output_path /data/gpfs/projects/punim1928/RISE/JITDP/crawling