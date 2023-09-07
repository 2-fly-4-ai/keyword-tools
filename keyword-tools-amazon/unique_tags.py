import pandas as pd
import json
from collections import Counter


keywords ="batch_dogs\keywords_batch_dogs\keywords_training_behavior.csv"
tagged_keywords = "batch_dogs/keywords_tagged_dogs/tagged_training_behaviour.csv"


df1 = pd.read_csv(tagged_keywords)
df2 = pd.read_csv(keywords,  encoding= "utf-8")
tag_list= []

for asin,title,tags in zip(df1["asin"],df1["title"],df1["tags"]):
    print(tags)
    tags = tags.replace("['","").replace("']","").replace("[","").replace("]","").replace('"',"").split("', '")
    for i in tags:
        if(i!=""):
         tag_list.append(i)

x = (Counter(tag_list))
df_final = pd.DataFrame.from_records(list(dict(x).items()), columns=['Keyword','Count'])
df_merged = pd.merge(df2,df_final, on="Keyword" )

df_merged.to_csv("unique_training_behaviour.csv")