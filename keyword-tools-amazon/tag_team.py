
import pandas as pd
from bs4 import BeautifulSoup
import ftfy
#! coding: utf-8

keywords = "batch_small_animals\keywords_batch_small_animals\keywords_batch_small_animals_treats.csv"
sheet_url = "batch_small_animals\products_batch_small_animals\products_small_animals_treats.csv"

df1 = pd.read_csv(sheet_url,  encoding= "utf-8")
df2 = pd.read_csv(keywords,  encoding= "utf-8")
keyword_list = df2["Keyword"].values.tolist()

asin_list = []
title_list = []
tags_list = []
subcategory_list = []
reviews_list = []

for asin,title,subcategory,num_reviews in zip(df1["ASIN"],df1["product_title"],df1["context"],df1["num_reviews"]):
    tags= []

    title = title.lower().replace("'s","")
    
    

    for keyword in keyword_list:
        # if i.lower() in title:
        #     tags.append(i)
        if keyword in title:
            test_var_1 = True
        else:
            test_var_1 = False
            
        s = keyword.replace("'s","").replace(" and "," ").replace(" for "," ").replace(" your "," ").replace(" a "," ")
        
            
        
        test_var_2 = all(elem in (title.split(" ")) for elem in (s.lower().split(" ")))
        
        test_var3_list = s.lower().split(" ")
        
        
        test_var_3_shortened = []
        true_false_list = []
        
        true_check = 0
        false_check = 0
        
        for i in test_var3_list:
            
            if i[-1] == "s":
                i = i[:-1]
            i = f" {i} "
            
            str_context_list = f" {title} "
            if i in str_context_list:
                true_check += 1
            else:
                false_check += 1
            

        if true_check > 0 and false_check < 1:
            test_var_3 = True
        else:
            test_var_3 = False
        
        
        if test_var_1 or test_var_2 or test_var_3 == True :
            tags.append(keyword)
            
    asin_list.append(asin)
    title_list.append(title)
    tags_list.append(str(tags))
    subcategory_list.append(str(subcategory))
    reviews_list.append(str(num_reviews))

df_asin = pd.DataFrame (asin_list, columns = ['asin'])
df_title = pd.DataFrame (title_list, columns = ['title'])
df_tags_list = pd.DataFrame (tags_list, columns = ['tags'])
df_subcategory_list = pd.DataFrame (subcategory_list, columns = ['Subcategory'])
df_num_reviews_list = pd.DataFrame (reviews_list, columns = ['Subcategory'])

result1 = pd.concat([df_asin, df_title, df_tags_list,df_subcategory_list,df_num_reviews_list], axis=1, join="inner")

result1.to_csv("batch_small_animals/unique_tags_small_animals/tagged_small_animals_treats.csv")
        
        
        
        
        
        

        
        
        
        


