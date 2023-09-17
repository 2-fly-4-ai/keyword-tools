import csv
import urllib.request
import time
import pandas as pd

df1 = pd.read_csv("GLS/version2/GLS_aida_generated.csv", engine= "python", error_bad_lines= False)                 
df2 = pd.read_csv("GLS/version2/GLS_features_generated.csv", engine= "python", error_bad_lines= False)
df3 = pd.read_csv("GLS/version2/GLS_titles_generated.csv", engine= "python", error_bad_lines= False)
df4 = pd.read_csv("GLS/version2/scraped active-keywords-nuked.gunlawsuits.org-2022-06-22-06-44-03.csv", engine= "python", error_bad_lines= False)

#df1 = df1[]

#df1["keyword"] = df1["keyword"].str.lower()
#df2["keyword"] = df2["keyword"].str.lower()

newFrame = pd.merge(df1, df2 , on =['id','asin'], how='left')
newFrame = pd.merge(newFrame, df3 , on =['id','asin'], how='left')
newFrame = pd.merge(newFrame, df4 , on =['id','asin'], how='left')

newFrame = newFrame[["id","asin","search_term","total_ratings","product_features","final_titles","brand","final_features","final_adverts"]]
#newFrame = newFrame.sort_values(by=['intro'])
#newFrame = newFrame.drop(['Unnamed: 0'], axis = 
#newFrame = newFrame[['ID','TERM','SV']]
#newFrame = newFrame[["Index_x","Term","Context_x","Introduction","Blog1"]]

#dfdedupe =  newFrame.drop_duplicates(subset=["Term"], keep='first', inplace=False)
newFrame.to_csv("z_merge_test_for_context.csv", index =False)