import pandas as pd
df = pd.read_csv("GLS/version2\Gls_product_pp.csv")
out_df = pd.DataFrame()
asin_limit = 10
idx = 1
for state, frame in df.groupby(['record_id']):
    id = int(frame['record_id'].iloc[0])
    frame = frame.sort_values(by=['total_ratings'])
    frame = frame[['asin', 'name', 'brand', 'features', 'aida']]#,asin,total_ratings,brand,features,name,aida
    temp = [id]
    for x in frame.to_dict('records')[:asin_limit]:
        temp.extend(x.values())
    names = ['record_id']
    for i in range(len(frame.index)):
        i = i
        names.extend([f"Products:{i}:"+"ASIN", f"Products:{i}:"+"NAME", f"Products:{i}:"+"Brand", f"Products:{i}:"+"Features", f"Products:{i}:"+"Aida"])
    temp_df = pd.DataFrame(dict(zip(names, temp)), index=[idx])
    out_df = pd.concat([out_df, temp_df])
    idx += 1
out_df.to_csv("GLS_tranposed.csv")