import pandas as pd
size = 10000
filename = 'serp_difference\Id_term_serp.csv'
for i, chunk in enumerate(pd.read_csv(filename, chunksize=size)):
    chunk.to_csv(f"serp_split_id_term/SERP-PRODUCT{i}.csv", index=False)
    