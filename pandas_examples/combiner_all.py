import pandas as pd
from pathlib import Path

source_files = sorted(Path('all_intro_serp').glob('*.csv'))

dataframes = []
for file in source_files:
    # additional arguments up to your needs
    df = pd.read_csv(file, encoding = "utf8", error_bad_lines = False )
    df = df
    #df.info()
    #test = file.name
    #test = test.replace(".csv", "")
    #df['source'] = test
    dataframes.append(df)


df_all = pd.concat(dataframes)

#df_all = df_all.rename(columns={'#': 'ID', 'Keyword': 'TERM', 'Volume': 'SV'})

#df_all[["#","Keyword","Volume"]] = df_all[["ID","TERM","SV"]]
#ID,TERM,CONTEXT


df_all.to_csv('SERP-FINAL-INTROS.csv', encoding='utf8', index= None)