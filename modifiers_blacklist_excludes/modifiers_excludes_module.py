import csv
import pandas as pd
import time
import sys


FULL_DOCUMENT= 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSfYGhg8qV5V43l1rfjEyY3u2dc_BPsmI9XJBwFMB3V3GJZu6NaPvaFkbkx_YSaTJvNArmulgVAGAc7/pub?output=xlsx' #this would be a variable that would have to change with the different sheet you're trigger it from.

df_MASTER = pd.read_excel(FULL_DOCUMENT ,sheet_name="keyword_list_GoogleKWP") #THE KEYWORDS
df_ML = pd.read_excel(FULL_DOCUMENT ,sheet_name="modifiers_list") #The modifiers List

MODIFIERS_LIST_PRE = df_ML["Modifier"].astype(str).to_list()

MODIFIERS_BLACKLIST_EXCLUDES = []
#Excludes -NORMALIZED 


for i in MODIFIERS_LIST_PRE:
        i = i.lower()
        i = f" {i} "
        MODIFIERS_BLACKLIST_EXCLUDES.append(i) 
        

        
LANGUAGE_LIST = []
KW_LIST_2 = [] #KW WHITELIST NORMALIZED!!!! -2 be reused Throughout   #
KW_LIST = df_MASTER["KW"].astype(str).to_list()
for i in KW_LIST:
    i = i.lower()
    KW_LIST_2.append(f" {i} ")
    

MODIFIER_WHITELIST = [word for word in KW_LIST_2 if not any(
    bad in word for bad in MODIFIERS_BLACKLIST_EXCLUDES)]

MODIFIERS_BLACKLISTED_ITEMS = list(set(KW_LIST_2) - set(MODIFIER_WHITELIST))


MODIFIERS_BLACKLISTED_ITEM2 = []
for i in MODIFIERS_BLACKLISTED_ITEMS:
    i = i[1:-1]
    MODIFIERS_BLACKLISTED_ITEM2.append(i)       


newtest4 = [] 
newtest4_old = []
newtest5 = []
newtest6_CHECK = []

#copy_test2 = BRAND_BLACKLISTED_ITEMS
for n in MODIFIERS_BLACKLISTED_ITEMS:
    for i in MODIFIERS_BLACKLIST_EXCLUDES:
        if i in n:
            a = f"{i}"
            x = a[1:-1]
            z = n.replace(i," ")
            if len(z)== 1:
                y = "MODIFIER"
            elif len(z) > 0:
                y = "MODIFIER+"
    
     
    newtest4_old.append(a)
    newtest4.append(x) 
    newtest5.append(z)  
    newtest6_CHECK.append(y)
    
    
df_WL_ME = pd.DataFrame(MODIFIER_WHITELIST,
                     columns = ['MODIFIERS_WHITELISTED_TERMS']) 

df_Modifiers_Blacklisted = pd.DataFrame(MODIFIERS_BLACKLISTED_ITEM2 , #First Frame
                     columns = ['MODIFIED_KEYWORDS']) 

df_Modifiers_Blacklisted2 = pd.DataFrame(MODIFIERS_BLACKLISTED_ITEMS , #First Frame
                     columns = ['MODIFIED_KEYWORDS']) 

df_MBL_trig = pd.DataFrame(newtest4,
                     columns = ['MODIFIERS_BLACKLISTED_TRIGGER']) #SECOND FRAME


df_Product2 = pd.DataFrame(newtest5,
                     columns = ['STRIPPED_PRODUCT']) #SECOND FRAME

df_Modifier_Check = pd.DataFrame(newtest6_CHECK,
                     columns = ['MODIFIER/MODIFIER+']) #SECOND FRAME
    
MODIFIERS_BLACKLISTED_ITEM2 = []
for i in MODIFIERS_BLACKLISTED_ITEMS:
    i = i[1:-1]
    MODIFIERS_BLACKLISTED_ITEM2.append(i)
    
test1 = pd.concat([df_Modifiers_Blacklisted, df_MBL_trig, df_Product2], axis=1, join="inner")
df_MASTER = df_MASTER[["KW","SV"]]
dfModifiersFinal2x = pd.merge(test1, df_MASTER, how = "left" , left_on="MODIFIED_KEYWORDS"
, right_on="KW").drop('KW', 1)

dfModifiersFinal2x.to_csv("df_modifier_final.csv")