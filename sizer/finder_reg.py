import os 
import re

wd = os.getcwd()

def finder_reg(printer = False):
    paths_to_search = []
    for path, directory, files in os.walk(wd):
        for filename in files:
            path_name = os.path.join(path,filename)
            paths_to_search.append(path_name)


    keywords_list = []
    ext = "none"
    print("please add a keyword to look for:")
    while keywords_list == []:
        keywords_list = input().split(" ")
        keywords_list = [word.lower() for word in keywords_list]
        
        


    found_items = []
    for keyword in keywords_list:
        for path in paths_to_search:
            if keyword in  path.lower():
                found_items.append(path)
    
    
    
    if printer == True and len(found_items) != 0:
        for item in found_items:
            print(item)
    
    return found_items, keywords_list

if __name__ == "__main__":
    
    finder(printer = True)