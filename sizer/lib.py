import sys
import os
import pandas as pd

def dirsize(basepath, unit = None, rnd = 3):

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
    
    return total_size
    
def filesize(basepath, unit = None, rnd = 3):
    
    total_size = os.path.getsize(basepath)
    
    metric = {"KB":1,"MB":2,"GB":3}
    
    if unit != None:
        final_size = total_size/ (1024**metric[unit])
        return round(final_size, rnd)
    
    return total_size

def sizer(basepath, unit = None, rnd = 3):
    #dirsize filesize
    
    size = 0
    
    for path in os.listdir(basepath):
        
        if os.path.isfile(path):
            size += filesize(path, unit = unit, rnd = rnd)
            
        if os.path.isdir(path):
            size += dirsize(path, unit = unit, rnd = rnd)
        
    return size

def list_size(basepath, unit = None, rnd = 3, to_excel = False):
    

        
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
    d.set_index(0, inplace = True)#[1]
    d.columns = ["sizes"]
    print(d.sizes.sort_values(ascending = False))


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
    	
    main()
