import csv
import pandas as pd
import time
import sys

FULL_DOCUMENT= 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSfYGhg8qV5V43l1rfjEyY3u2dc_BPsmI9XJBwFMB3V3GJZu6NaPvaFkbkx_YSaTJvNArmulgVAGAc7/pub?output=xlsx' #this would be a variable that would have to change with the different sheet you're trigger it from.
FULL_DOCUMENTx = "TEST-AFTER-GPT-EXCLUDER.csv"

#df_MASTER = pd.read_excel(FULL_DOCUMENT ,sheet_name="keyword_list_GoogleKWP") #THE KEYWORDS
df_MASTER = pd.read_csv(FULL_DOCUMENTx ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS

df_BL = pd.read_excel(FULL_DOCUMENT ,sheet_name="brands_list")

BRANDS_LIST_PRE = df_BL["Brands"].astype(str).to_list()

BRAND_BLACKLIST_EXCLUDES = []
#Excludes -NORMALIZED 
for i in BRANDS_LIST_PRE:
        i = i.lower()
        i = f" {i} "
        BRAND_BLACKLIST_EXCLUDES.append(i)

LANGUAGE_LIST = []
KW_LIST_2 = [] #KW WHITELIST NORMALIZED!!!! -2 be reused Throughout   #
KW_LIST = df_MASTER["KW"].astype(str).to_list()
for i in KW_LIST:
    i = i.lower()
    KW_LIST_2.append(f" {i} ")
    
BRAND_WHITELIST = [word for word in KW_LIST_2 if not any( 
    bad in word for bad in BRAND_BLACKLIST_EXCLUDES)]

BRAND_BLACKLISTED_ITEMS = list(set(KW_LIST_2) - set(BRAND_WHITELIST))


newtest2 = [] 
newtest3 = []
newtest4_CHECK = []

#copy_test2 = BRAND_BLACKLISTED_ITEMS
for n in BRAND_BLACKLISTED_ITEMS:
    for i in BRAND_BLACKLIST_EXCLUDES:
        if i in n:
            x = f"{i}"
            x = x[1:-1]
            z = n.replace(i," ")
            output ="" #query({"inputs": i,"parameters": {"use_gpu": True}})                              
            if len(z)== 1:
                y = "BRAND"
            elif len(z)> 0:
                y = "BRAND+"
            
    newtest2.append(x) 
    newtest3.append(z)  
    newtest4_CHECK.append(y)


BRAND_BLACKLISTED_ITEM2 = []
for i in BRAND_BLACKLISTED_ITEMS:
    i = i[1:-1]
    BRAND_BLACKLISTED_ITEM2.append(i)
    
f_WL_BE = pd.DataFrame(BRAND_WHITELIST,
                     columns = ['BRAND_WHITELISTED_TERMS']) 

df_Brands_Blacklisted = pd.DataFrame(BRAND_BLACKLISTED_ITEM2, #First Frame
                     columns = ['BRANDED_KEYWORDS']) 

#df_Brands_Blacklisted_old = pd.DataFrame(BRAND_BLACKLISTED_ITEMS, #First Frame
                     #columns = ['BRANDED_KEYWORDS']) 

df_BBL_trig = pd.DataFrame(newtest2,
                     columns = ['BRANDS_BLACKLISTED_TRIGGER']) #SECOND FRAME

df_Product = pd.DataFrame(newtest3,
                     columns = ['STRIPPED_PRODUCT']) #SECOND FRAME

df_Brand_Check = pd.DataFrame(newtest4_CHECK,
                     columns = ['BRAND/BRAND+']) #SECOND FRAME


test1 = pd.concat([df_Brands_Blacklisted , df_BBL_trig, df_Product], axis=1, join="inner")
df_MASTER = df_MASTER[["KW"]]#,"SV"
dfModifiersFinal2x = pd.merge(test1, df_MASTER, how = "left" , left_on="BRANDED_KEYWORDS"
, right_on="KW").drop('KW', 1)

dfModifiersFinal2x.to_csv("df_brand_final.csv")
dfModifiersFinal2x.to_csv("BRAND_TEST.csv")