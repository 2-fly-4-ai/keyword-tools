
import csv
import pandas as pd
import time


FULL_DOCUMENTx = "TEST-AFTER-GPT-EXCLUDER.csv"
FULL_DOCUMENTy = "porn_excludes.csv"
REMOVED = "1MILLION_KEYWORD_CHALLENGE_EXCLUDES.csv"


df_MASTER = pd.read_csv(FULL_DOCUMENTx ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS
df_porn = pd.read_csv(FULL_DOCUMENTy  ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS


porn_list = df_porn["KW"].astype(str).to_list()

KW_LIST = df_MASTER["KW"].astype(str).to_list()
df_MASTER.info()

REMOVED_DF = pd.read_csv(REMOVED ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS
REMOVED_LIST= REMOVED_DF["EXCLUDES_BLACKLISTED_TERMS"].astype(str).to_list()
NO_EXCLUDES = (set(KW_LIST) - set(REMOVED_LIST))#- set(porn_list)
NO_EXCLUDES = NO_EXCLUDES - set(porn_list)
newray = []
for i in NO_EXCLUDES:
    words = i.split(" ")
    if len(words) > 4 or len(words) == 1:
        del i
    else:
        newray.append(i)


NO_EXCLUDES_DF = df_Exclude_Check = pd.DataFrame(newray,
                     columns = ['KW']) #SECOND FRAME

NO_EXCLUDES_DF.to_csv('TEST-AFTER-GPT-EXCLUDER.csv')



