from distutils import extension
import os
import pandas
import shutil
from sizer.finder_reg import finder_reg


def reg_mover():


    found_list, extensions = finder_reg(printer=True)



    destination= ""
    while destination == "":
        destination = input("please input a destination folder\n")

    if os.path.isdir(destination) == False:
        os.mkdir(destination)


    print(f"warning, this will move {len(found_list)} items")

    confirmation  = ""
    while not confirmation in ["yes","no","y","n"]:
        confirmation = input("confirm?").lower()

    if confirmation in ["yes", "y"]:
        for base in found_list:
            shutil.move(base, destination)
            
if __name__ == "__main__":
    
    reg_mover()