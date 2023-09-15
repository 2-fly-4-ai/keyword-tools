import pandas as pd
df = pd.read_csv("SERP\serp_product_pp.csv")
df = df
out_df = pd.DataFrame()
asin_limit = 10
idx = 1
for state, frame in df.groupby(['record_id']):
    id = int(frame['record_id'].iloc[0])
    frame = frame.sort_values(by=['total_ratings'])
    frame = frame[['asin', 'name', 'brand', 'image_urls', 'aida']]
    temp = [id]
    for x in frame.to_dict('records')[:asin_limit]:
        temp.extend(x.values())
    names = ['record_id']
    for i in range(len(frame.index)):
        i = i+1
        names.extend([f"Products : {i} : "+"ASIN", f"Products : {i} : "+"Product Name", f"Products : {i} : "+"Brand Name", f"Products : {i} : "+"Product Image URL", f"Products : {i} : "+"Product AIDA"])
    temp_df = pd.DataFrame(dict(zip(names, temp)), index=[idx])
    out_df = pd.concat([out_df, temp_df])
    idx += 1
out_df.to_csv("output_files/z_serp_transposed.csv") 