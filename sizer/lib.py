import sys
import os
import pandas as pd

def dirsize(basepath, unit = None, rnd = 3):
    '''
    This function gets you the TOTAL size of every FOLDER in the directory and its children
    
    returns a float

    dirsize(basepath, 
             unit = None,  
             rnd = 3)
    
    basepath: the relavite path to the folder whose contents you want to calculate
    
    unit: {"KB":1,"MB":2,"GB":3}
        the unit in which you want to calculate. default KB
        
    rnd: (int)
        how many decimals you want the resulting number to have. default 3.
    
    '''


    total_size = 0
    for path, directories, files in os.walk(basepath):
        for file in files:
            filepath = os.path.join(path , file)
            #print(filepath)
            size = os.stat(filepath).st_size
            size2 = os.path.getsize(filepath)
            #print(filepath , size, size2)
            total_size += size
    
    metric = {"KB":1,"MB":2,"GB":3}
    
    if unit != None:
        final_size = total_size/ (1024**metric[unit])
        return round(final_size, rnd)
    
    return round(total_size / 1024, rnd)
 
# print(dirsize(pwd)) 

# print(dirsize(pwd, "KB")) 



def filesize(basepath, unit = None, rnd = 3):
    '''
    This function gets you the TOTAL size of every file in the directory and its children
    
    returns a float

    dirsize(basepath, 
             unit = None,  
             rnd = 3)
    
    basepath: the relavite path to the folder whose contents you want to calculate
    
    unit: {"KB":1,"MB":2,"GB":3}
        the unit in which you want to calculate. default KB
        
    rnd: (int)
        how many decimals you want the resulting number to have. default 3.
    
    '''

    
    total_size = os.path.getsize(basepath)
    
    metric = {"KB":1,"MB":2,"GB":3}
    
    if unit != None:
        final_size = total_size/ (1024**metric[unit])
        return round(final_size, rnd)
    
    return round(total_size / 1024, rnd)



def sizer(basepath, unit = None, rnd = 3):
    
    '''
    This function gets you the TOTAL size of EVERYTHING (file and folder) in the directory and its children
    
    returns a float

    dirsize(basepath, 
             unit = None,  
             rnd = 3)
    
    basepath: the relavite path to the folder whose contents you want to calculate
    
    unit: {"KB":1,"MB":2,"GB":3}
        the unit in which you want to calculate. default KB
        
    rnd: (int)
        how many decimals you want the resulting number to have. default 3.
    
    '''
    
    size = 0
    import pathlib
    for path in os.listdir(basepath):
        
        if os.path.isfile(path):
            # size += filesize(path, unit = unit, rnd = rnd)
            size += filesize(pathlib.Path(path), unit = unit, rnd = rnd)

            
        if os.path.isdir(path):
            # size += dirsize(path, unit = unit, rnd = rnd)
            size += dirsize(pathlib.Path(path), unit = unit, rnd = rnd)
        
    return size

def list_size(basepath, unit = "KB", rnd = 3, to_excel = False):
    
    '''
    This function calculates the sizes of everything contained in  the path (files and folders)
    
    returns a pandas series
    
    basepath: the parent directory in which to calculate the size of its children
    
    unit: the unit in which you want to calculate it. default KB
    
    rnd: (int)
        how many decimals you want the resulting number to have. default 3.
        
    '''

        
    data = []
    
    for path in os.listdir(basepath):
        
        p = os.path.join(basepath, path)
        
        if os.path.isfile(p):
            size = filesize(p, unit = unit, rnd = rnd)
            
            #print(path, size)
            
            result = (path,size)
            
            data.append(result)
            
        if os.path.isdir(p):
            size = dirsize(p, unit = unit, rnd = rnd)
            
            #print(path, size)
            
            result = (path,size)
            
            data.append(result)
    d = pd.DataFrame(data)
    d.columns = ["file", "size"]
    d.set_index("file", inplace = True)
    
    sorted_sizes = d.sort_values(by = "size",ascending = False)
    
    if len(sorted_sizes) > 10:
        decision = input("more than 10 files found, select number of files to show\n")
        print( sorted_sizes.head(int(decision))    )

    if to_excel == True:
        from datetime import datetime
        now = datetime.now()
        now = str(now.astimezone())[:16].replace(":","-")
        
        filepath_list = os.getcwd().split("/")
        # if len(filepath_list) > 1:
        #     filename = filepath_list[-1]
        # if len(filepath_list) == 1:
        #     filename = __file__
        
        sorted_sizes.to_csv(f"/home/tomascdg/code/reports/{now} {filepath_list[-1]}.csv")        
    
    return sorted_sizes

def list_size_df(basepath, unit = "KB", rnd = 3, to_excel = False):
    
    '''
    This function calculates the sizes of everything contained in  the path (files and folders)
    
    returns a pandas series
    
    basepath: the parent directory in which to calculate the size of its children
    
    unit: the unit in which you want to calculate it. default KB
    
    rnd: (int)
        how many decimals you want the resulting number to have. default 3.
        
    '''

        
    data = []
    
    for path in os.listdir(basepath):
        
        p = os.path.join(basepath, path)
        
        if os.path.isfile(p):
            size = filesize(p, unit = unit, rnd = rnd)
            
            #print(path, size)
            
            result = (path,size)
            
            data.append(result)
            
        if os.path.isdir(p):
            size = dirsize(p, unit = unit, rnd = rnd)
            
            #print(path, size)
            
            result = (path,size)
            
            data.append(result)
    d = pd.DataFrame(data)
    d.columns = ["file", "size"]
    
    sorted_sizes = d.sort_values(by = "size",ascending = False)
    
    
    return sorted_sizes


def main():

        if len(sys.argv) == 1:
            print("unit: MB")
            size = sizer(os.getcwd(), unit = "MB", rnd = 2)
            
        if len(sys.argv) == 2:
            size = sizer(sys.argv[1])
            print("unit: MB")
            
        if len(sys.argv) == 3:
            print(f"unit: {sys.argv[2]}")  
            size = sizer(sys.argv[1], 
                unit = sys.argv[2])
            
        if len(sys.argv) == 4:
            print(f"unit: {sys.argv[2]}")
            size = sizer(sys.argv[1], 
                unit = sys.argv[2],
                rnd = sys.argv[3])
            
        if size != None:
            print(size)
        
if __name__ == "__main__":
    	
    print(main())