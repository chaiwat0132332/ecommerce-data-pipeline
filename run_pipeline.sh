#!/bin/bash

echo "Start pipeline at $(date)"
python3 /Users/chaiwatyingsunton/ecommerce_data_pipeline/scripts/transform_data.py
python3 /Users/chaiwatyingsunton/ecommerce_data_pipeline/scripts/load_to_sqlite.py
python3 /Users/chaiwatyingsunton/ecommerce_data_pipeline/scripts/analyte.py
echo "Pipeline finished at $(date)"

