import csv
import pandas as pd
import time
import sys

FULL_DOCUMENT= 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSfYGhg8qV5V43l1rfjEyY3u2dc_BPsmI9XJBwFMB3V3GJZu6NaPvaFkbkx_YSaTJvNArmulgVAGAc7/pub?output=xlsx' #this would be a variable that would have to change with the different sheet you're trigger it from.
FULL_DOCUMENTx = "TEST-AFTER-GPT-EXCLUDER.csv"


#df_MASTER = pd.read_excel(FULL_DOCUMENT ,sheet_name="keyword_list_GoogleKWP") #THE KEYWORDS
df_MASTER = pd.read_csv(FULL_DOCUMENTx ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS
df_MASTER.info()
df_REMOVED = pd.read_csv(FULL_DOCUMENTx ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS

df_excludes = pd.read_excel(FULL_DOCUMENT ,sheet_name="excludes_list")

COMBO_EXCLUDES_DF = df_excludes.stack().reset_index() #this takes all the excludes from the excludes lisy
COMBO_EXCLUDES_DF["FULL_LIST"] = COMBO_EXCLUDES_DF.iloc[:, 2]
BLACKLIST_PRE = COMBO_EXCLUDES_DF["FULL_LIST"].astype(str).to_list()
KW_LIST = df_MASTER["KW"].astype(str).to_list()


BLACKLIST_EXCLUDES = []
#Excludes -NORMALIZED 
for i in BLACKLIST_PRE:
    i = i.lower()
    i = f" {i} "
    BLACKLIST_EXCLUDES.append(i)
    
KW_LIST_2 = [] #KW WHITELIST NORMALIZED!!!! -2 be reused Throughout   #

for i in KW_LIST:
    i = i.lower()
    KW_LIST_2.append(f" {i} ")
    
WHITELIST = [word for word in KW_LIST_2 if not any( 
    bad in word for bad in BLACKLIST_EXCLUDES)]

BLACKLISTED_ITEMS = list(set(KW_LIST_2) - set(WHITELIST))

blacklisted = []
excludes_CHECK = []
#copy_test = BLACKLISTED_ITEMS
for n in BLACKLISTED_ITEMS:
    for i in BLACKLIST_EXCLUDES:
        if i in n:
            x = f"{i}"
            x = x[1:-1]
            y = f"EXCLUDE"
           
    blacklisted.append(x)
    excludes_CHECK.append(y)
    
BLACKLISTED_ITEM2 = []
for i in BLACKLISTED_ITEMS:
    i = i[1:-1]
    BLACKLISTED_ITEM2.append(i)
    
#Blacklisted Terms 

df_Blacklisted = pd.DataFrame(BLACKLISTED_ITEM2,
                     columns = ['EXCLUDES_BLACKLISTED_TERMS']) #FIRST FRAME

df_Blacklist_match = pd.DataFrame(blacklisted,
                     columns = ['EXCLUDES_BLACKLISTED_TRIGGER']) #SECOND FRAME

df_Exclude_Check = pd.DataFrame(excludes_CHECK,
                     columns = ['EXCLUDE']) #SECOND FRAME





test1 = pd.concat([df_Blacklisted, df_Blacklist_match, df_Exclude_Check,], axis=1, join="inner")
df_exclude_final2 =  pd.merge(test1, df_MASTER, how = "left" , left_on="EXCLUDES_BLACKLISTED_TERMS"
, right_on="KW")
df_MASTER = df_MASTER[["KW"]]#,"SV"
dfModifiersFinal2x = pd.merge(test1, df_MASTER, how = "left" , left_on="EXCLUDES_BLACKLISTED_TERMS"
, right_on="KW").drop('KW', 1)

#df_exclude_final2 = df_exclude_final2.drop("KW", axis= 1)
#df_exclude_final.to_csv('df_exclude_final2.csv')

dfModifiersFinal2x.to_csv('WHOLE_EXLUDED_LIST_MKC.csv')