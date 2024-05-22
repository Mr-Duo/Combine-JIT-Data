#!/bin/bash

rm -rf logs

git pull

python3 main.py \
    -data_path /media/aiotlab3/27934be5-a11a-44ba-8b28-750d135bc3b3/duongnd/rcp/dg_cache/dataset \
    -output_path /media/aiotlab3/27934be5-a11a-44ba-8b28-750d135bc3b3/duongnd/rcp/crawling
