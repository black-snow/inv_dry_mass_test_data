#!/usr/bin/env python3
import pandas as pd
import sys

# round.py path col [col [col [...]]]
# round to two decimals, expects headers
NUM_DECIMALS = 3

df = pd.read_csv(sys.argv[1])
col_map = {x: NUM_DECIMALS for x in sys.argv[2:]} if len(sys.argv) > 2 else {'length_mm': NUM_DECIMALS, 'dry_weight_mg': NUM_DECIMALS}
df = df.round(col_map)
df.to_csv(sys.argv[1], index=False)