####################################################
import shutil
import os
from sizer.lib import list_size_df
pwd = os.getcwd()
# list_size(pwd)

test = "/mnt/f/Users/Windows10/Documents/Zoom"
unit = "MB"

df = list_size_df(test, rnd = 3, unit = unit)

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
#################################################################


cut_size = float(input("which size would you like to separate?"))

direction = ""
while not direction in ["a","b"]:

    direction = input("would you like to move file above or below this thershold ?  (A/B) ").lower()


if direction == "a":
    cut_df = df[df["size"] > cut_size]
if direction == "b":
    cut_df = df[df["size"] < cut_size]

print(cut_df)



filenames = [test +"/"+ filename for filename in cut_df["file"]] #ojo con las direcciones!!

# print(filenames)

destination= ""
while destination == "":
    destination = input("please input a destination folder")

if os.path.isdir(destination) == False:
    os.mkdir(destination)


total_sum_of_size = round(cut_df["size"].sum())
print(f"warning, this will move {len(cut_df)} items with {total_sum_of_size} {unit}")

confirmation  = ""
while not confirmation in ["yes","no","y","n"]:
    confirmation = input("confirm?").lower()

if confirmation in ["yes", "y"]:
    for base in filenames:
        shutil.move(base, destination)
        
        # /mnt/f/Users/Windows10/Documents/Zoom