import csv
import urllib.request
import time
import pandas as pd

df1 = pd.read_csv("GLS_new_context.csv", engine= "python", error_bad_lines= False)                 
df2 = pd.read_csv("GLS/version2/gls_faqs.csv", engine= "python", error_bad_lines= False)


newFrame = pd.merge(df1, df2 , on =['id'], how='right')

newFrame.to_csv("faq_preprocess.csv", index =False)