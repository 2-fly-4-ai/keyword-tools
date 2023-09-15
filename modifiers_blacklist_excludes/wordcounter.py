
import csv
import pandas as pd
import time


FULL_DOCUMENTx = "part1-Million-Keyword-Challenge-CHopped-after-GPTJ.csv"

df_MASTER = pd.read_csv(FULL_DOCUMENTx ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS
KW_LIST = df_MASTER["KW"].astype(str).to_list()
df_MASTER.info()

REMOVED = "df_exclude_final.csv"
REMOVED_DF = pd.read_csv(REMOVED ,engine="python",encoding = "utf8", error_bad_lines = False) #THE KEYWORDS
REMOVED_LIST= REMOVED_DF["EXCLUDES_BLACKLISTED_TERMS"].astype(str).to_list()
NO_EXCLUDES = set(KW_LIST) - set(REMOVED_LIST)

newray = []
for i in NO_EXCLUDES:
    words = i.split(" ")
    if len(words) > 4 or len(words) == 1:
        del i
    else:
        newray.append(i)


NO_EXCLUDES_DF = df_Exclude_Check = pd.DataFrame(newray,
                     columns = ['Cleanlist KW']) #SECOND FRAME

NO_EXCLUDES_DF.to_csv('TEST-AFTER-GPT-EXCLUDER.csv')



