import shutil
import os
from sizer.lib import list_size_df
pwd = os.getcwd()
# list_size(pwd)

test = "/mnt/f/Users/Windows10/Documents/Zoom"

df = list_size_df(test, rnd = 3, unit = "MB")

print("showing filesizes in MB")

if len(df) > 20:
    len_response = input("there are more than 20 items, proceed (Enter) or specify a desired number of rows (number) ")
    if len_response != "" and int(len_response) > 0:
       length = int(len_response)
    
       
    else:
        length = len(df)
        
for index, row in df.head(length).iterrows():
#     print(row["file"], "--", row["size"])
    print(row["size"], "----", row["file"])

