import os 

wd = os.getcwd()

def finder_ext(printer = False):
    paths_to_search = []
    for path, directory, files in os.walk(wd):
        for filename in files:
            path_name = os.path.join(path,filename)
            paths_to_search.append(path_name)


    extensions_list = []
    ext = "none"
    print("please add an extention to look for:")
    while extensions_list == []:
        extensions_list = input().replace(".","").split(" ")
        
        


    found_items = []
    for extension in extensions_list:
        for path in paths_to_search:
            if path.endswith(extension):
                found_items.append(path)
    
    
    
    if printer == True and len(found_items) != 0:
        for item in found_items:
            print(item)
    
    return found_items, extensions_list

if __name__ == "__main__":
    
    finder(printer = True)