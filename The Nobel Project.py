import pandas as pd
import numpy as np
from time import sleep 
import re 
import shutil 

def realcsv():
    # reading the real csv file as dataframe "csvdf".
    csvdf = pd.read_csv("D:\\Programming\\Git\\The-Nobel-Project\\Nobel Laureates 1901-2021.csv")
    csvdf.index.name = "Index" # assigning the index column a title "Index"
    return csvdf 

def newcsv(ndf): 
    # updating the real csv file into a new csv file as dataframe "ndf"
    ndf.to_csv("D:\\Programming\\Git\\The-Nobel-Project\\Nobel Laureates 1901-2021.csv",
               index = False) # "index = False" to avoid the duplication of index upon updating the file each time.

def home(ndf): # creating the home page of the project
    x = "Project Report"
    y = "On"
    z = "The Nobel Project"
    p = "Created by"
    q = "Tushar Agarwal"
    rows = shutil.get_terminal_size().columns # using shutil library to align the texts in the center of the ouput screen.
    print("\033[1m" + x.center(rows) + "\033[0m") # using special codes to apply bold
    print("\033[1m" + y.center(rows) + "\033[0m")
    print("\033[1m" + z.center(rows) + "\033[0m")
    print("\033[1m" + p.center(rows) + "\033[0m")
    print("\033[1m" + '\033[3m' + q.center(rows) + "\033[0m")
    print()
    # giving out instructions for the user.
    instr1 = "Hello! This program allows the user to access some information about all the Nobel Laureates from 1901 to 2021. \
You can use several filters to view or edit the data. Please follow all the instructions given to have the \
best experience with the program. \n\nYou are currently in 'Home,' please enter 'M' to proceed to the Main Menu or enter 'E' to exit: "
    for instr1a in instr1:
        print(instr1a, end="")
        sleep(0.001) # using sleep from time library to create the animated text effect.
    user1 = input(instr1[-1:-95])
    print("-"*156)
    if user1 == "M":
        mainmenu(ndf) 
    if user1 == "E":
        exit()

def mainmenu(ndf): # creating the main menu of the project
    instr2 = "Choose the academic discipline that you want the data to be displayed of. \n"
    for instr2a in instr2:
        print(instr2a, end="")
        sleep(0.001)
    print()
    fields = "1. All \n2. Chemistry \n3. Economics \n4. Literature \n5. Medicine \n6. Peace \n7. Physics \nH. Return to Home \nE. Exit \n"
    for sub in fields:
        print(sub, end="")
        sleep(0.001)
    print()
    subject = input("Enter the option: ")
    print("-"*156)
    if subject == "1":
        all(ndf)    
    if subject == "2":
        chem(ndf) 
    if subject == "3":
        eco(ndf)
    if subject == "4":
        lit(ndf)
    if subject == "5":
        med(ndf)
    if subject == "6":
        peace(ndf)
    if subject == "7":
        phy(ndf)
    if subject == "H":
        home(ndf)
    if subject == "E":
        exit()

def all(ndf): # assigning the operations for all the academic disciplines
    print(ndf)
    print()
    print("The data of all the nobel laureates in all fields has been displayed above.")
    operate(ndf)


def chem(ndf): # assigning the operations for chemistry
    print(ndf[ndf["Category"] == "Chemistry"])
    print()
    print("The data for all the nobel laureates in Chemistry has been displayed above")
    operate(ndf)

def eco(ndf): # assigning the operations for economics
    print(ndf[ndf["Category"] == "Economics"])
    print()
    print("The data for all the nobel laureates in Economics has been displayed above")
    operate(ndf)

def lit(ndf): # assigning the operations for literature
    print(ndf[ndf["Category"] == "Literature"])
    print()
    print("The data for all the nobel laureates in Literature has been displayed above")
    operate(ndf)

def med(ndf): # assigning the operations for medicine
    print(ndf[ndf["Category"] == "Medicine"])
    print()
    print("The data for all the nobel laureates in Medicine has been displayed above")
    operate(ndf)

def peace(ndf): # assigning the operations for peace
    print(ndf[ndf["Category"] == "Peace"])
    print()
    print("The data for all the nobel laureates in Peace has been displayed above")
    operate(ndf)

def phy(ndf): # assigning the operations for physics
    print(ndf[ndf["Category"] == "Physics"])
    print()
    print("The data for all the nobel laureates in Physics has been displayed above")
    operate(ndf)

def operate(ndf): # creating the operation menu of the project
    print("-"*156)
    instr3 = "You can now perform your next action by choosing an option from the following options. \n"
    for instr3a in instr3:
        print(instr3a, end="")
        sleep(0.001)
    print()
    opr = "1. Add a New Data \n2. Remove an Existing Data \n3. Update an Existing Data \n4. Search a Data \
\nM. Return to Main Menu  \nH. Return to Home \nE. Exit\n\n"
    for opr1 in opr:
        print(opr1, end="")
        sleep(0.001)
    action = input("Enter the option: ")
    print("-"*156)
    if action == "1":
        add(ndf)
    if action == "2":
        remove(ndf) 
    if action == "3":
        update(ndf)
    if action == "4":
        search(ndf)
    if action == "M":
        mainmenu(ndf)
    if action == "H":
        home(ndf)
    if action == "E":
        exit()

def abort(): # allowing the user to terminate a user defined input sequence
    print()
    instrab = "The action has been aborted, and the original data has been displayed above."
    for instrabo in instrab:
        print(instrabo, end="")
        sleep(0.001)
    print()
    
def add(ndf): # allowing the addition of a new data in the csv
    instr4 = "To add a new data, follow the following instructions. \n"
    for instr4a in instr4:
        print(instr4a, end="")
        sleep(0.001)
    print()
    instr4b = "NOTE: If you do not wish to add the data, you can enter 'ABORT' in any of the following fields to terminate the process \
and head back to the Operation Menu.\n"
    for instr4c in instr4b:
        print(instr4c, end="")
        sleep(0.001)
    print()
    Year = input("Enter the year of the award: ")
    if Year == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Name = input("Enter the name of the laureate: ")
    if Name == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    DOB = input("Enter the date of birth of the laureate: ")
    if DOB == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Sex = input("Enter the sex of the laureate: ")
    if Sex == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Category = input("Enter the category (academic field) of the award: ")
    if Category == "ABORT":
        print()
        print()
        print(ndf)
        abort()
        operate(ndf)
    Motivation = input("Enter the motivation of the laureate's award: ")
    if Motivation == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Birth_Country = input("Enter the place where the laureate was born: ")
    if Birth_Country == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Affiliation = input("Enter the affiliation of the laureate: ")
    if Affiliation == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    Affiliation_Place = input("Enter the place of affiliation of the laureate: ")
    if Affiliation_Place == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    ndf.loc[len(ndf.index)] = [Year, Name, DOB, Sex, Category, Motivation, Birth_Country, Affiliation, Affiliation_Place]
    newcsv(ndf) # overwrites/updates the old csv by entering the new data
    print()
    print(ndf)
    while True: 
        instr5 = "\nThe updated data has been displayed above. \n\nYou can perform the same action again by entering '1', or head back to the\
 operation options by pressing 'B': "
        for instr5a in instr5:
            print(instr5a, end="")
            sleep(0.001)
        inp1 = input(instr5a)
        if inp1 == "1": 
            print("-"*156)
            add(ndf)
        if inp1 == "B":
            operate(ndf)
            break

def namdec(): # using regex module from re library to match a variable with the data present in the csv dataframe.
    #name variable
    nam = input("Enter the name of the laureate: ")
    if nam == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    print()
    #name match variable
    namat = ndf.loc[ndf["Name"].str.match("(.*)"+nam+"(.*)")]
    print(namat)
    print(namat.index)
    print()

def remove(ndf): # allowing the removal of a data from the csv
    instr6 = "Here, you shall enter the name of the laureate whose data you want to remove. Upon doing so, the whole record of that \
certain laureate will be displayed. You then have to identify the index of that laureate from the output and type it in the next option. \
Then the record will be removed. \n"
    for instr6a in instr6:
        print(instr6a, end="")
        sleep(0.001)
    print()
    instr6b = "NOTE: If you do not wish to remove the data, you can enter 'ABORT' in any of the following fields to terminate \
the process and head back to the Operation Menu.\n"
    for instr6c in instr6b:
        print(instr6c, end="")
        sleep(0.001)
    print()
    namdec()
    #input the index
    ind1 = input("Enter the index: ")
    if ind1 == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    ndf.drop(int(ind1), axis = 0, inplace = True)
    newcsv(ndf)
    print()
    print(ndf)
    while True:
        instr7 = "\nThe updated data has been displayed above. \n\nYou can perform the same action again by entering '2', or head back to the\
 operation options by pressing 'B': "
        for instr7a in instr7:
            print(instr7a, end="")
            sleep(0.001)
        inp2 = input(instr7a)
        if inp2 == "2": 
            print("-"*156)
            remove(ndf)
        if inp2 == "B":
            operate(ndf)
            break

def update(ndf): # allowing the updation of a data from the csv
    instr8 = "Here, you shall enter the name of the laureate whose data you want to update. Upon doing so, the whole record of that \
certain laureate will be displayed. You then have to identify the index of that laureate from the output and type it in the next option. \
Then the record will be updated based on your inputs. \n"
    for instr8a in instr8:
        print(instr8a, end="")
        sleep(0.001)
    print()
    instr6b = "NOTE: If you do not wish to update the data, you can enter 'ABORT' in any of the following fields to terminate the process \
and head back to the Operation Menu.\n"
    for instr6c in instr6b:
        print(instr6c, end="")
        sleep(0.001)
    print()
    namdec()
    ind2 = input("Enter the index: ")
    if ind2 == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    print()

    instr9 = "Now, enter the new data with which you want to update an existing data. \n"
    old1 = ndf.loc[int(ind2), "Year"]
    Year = input("Enter the year of the award: ")
    if Year == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Year: # if the user leaves the option empty, then the old/original data will be displayed.
        Year =  old1

    old2 = ndf.loc[int(ind2), "Name"]
    Name = input("Enter the name of the laureate: ")
    if Name == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Name:
        Name =  old2

    old3 = ndf.loc[int(ind2), "DOB"]
    DOB = input("Enter the date of birth of the laureate: ")
    if DOB == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not DOB:
        DOB =  old3

    old4 = ndf.loc[int(ind2), "Sex"]
    Sex = input("Enter the sex of the laureate: ")
    if Sex == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Sex:
        Sex =  old4

    old5 = ndf.loc[int(ind2), "Category"]
    Category = input("Enter the category (academic field) of the award: ")
    if Category == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Category:
        Category =  old5

    old6 = ndf.loc[int(ind2), "Motivation"]
    Motivation = input("Enter the motivation of the laureate's award: ")
    if Motivation == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Motivation:
        Motivation =  old6

    old7 = ndf.loc[int(ind2), "Birth Country"]
    Birth_Country = input("Enter the place where the laureate was born: ")
    if Birth_Country == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Birth_Country:
        Birth_Country =  old7

    old8 = ndf.loc[int(ind2), "Affiliation"]
    Affiliation = input("Enter the affiliation of the laureate: ")
    if Affiliation == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Affiliation:
        Affiliation =  old8

    old9 = ndf.loc[int(ind2), "Affiliation Place"]
    Affiliation_Place = input("Enter the place of affiliation of the laureate: ")
    if Affiliation_Place == "ABORT":
        print()
        print(ndf)
        abort()
        operate(ndf)
    if not Affiliation_Place:
        Affiliation_Place =  old9
        
    print()
    ndf.loc[int(ind2)] = [Year, Name, DOB, Sex, Category, Motivation, Birth_Country, Affiliation, Affiliation_Place]
    newcsv(ndf)
    print(ndf)
    while True:
        instr9 = "\nThe updated data has been displayed above. \n\nYou can perform the same action again by entering '3', or head back to \
the operation options by pressing 'B': "
        for instr9a in instr9:
            print(instr9a, end="")
            sleep(0.001)
        inp3 = input(instr9a)
        if inp3 == "3": 
            print("-"*156)
            update(ndf)
        if inp3 == "B": 
            operate(ndf)
            break

def search(ndf): # allowing the user to search data based on their input.
    instr10 = "Choose the attribute based on which you want the data to be filtered and displayed.\n\n"
    for instr10a in instr10:
        print(instr10a, end="")
        sleep(0.001)
    # extra specific data list
    extr = "1. Year \n2. Name \n3. DOB \n4. Sex \n5. Birth Country \n6. Affiliation \
\n7. Affiliation Place \nSL. Specific Data of a Laureate \nSE. Specific Data of Every Laureate \nB. Back to the Operation Menu \
\nM. Return to Main Menu  \nH. Return to Home \nE. Exit\n\n"
    for extr1 in extr:
        print(extr1, end="")
        sleep(0.001)
    action = input("Enter the option: ")
    print("-"*156)
    if action == "1":
        year(ndf)
    if action == "2":
        name(ndf) 
    if action == "3":
        dob(ndf)
    if action == "4":
        sex(ndf)
    if action == "5":
        birth(ndf)
    if action == "6":
        aff(ndf)
    if action == "7":
        affp(ndf)
    if action == "SL":
        specl(ndf)        
    if action == "SE":
        spece(ndf)
    if action == "B":
        operate(ndf)
    if action == "M":
        mainmenu(ndf)
    if action == "H":
        home(ndf)
    if action == "E":
        exit()

def year(ndf): # assigning the user-given year to base the extraction of data.
    instr11 = "You can extract data for a single year or a list of years. If you want data for the latter, enter each year in the \
following option with comma as a separator (example: 2021, 2020, 2019): "
    for instr11a in instr11:
        print(instr11a, end="")
        sleep(0.001)
    print()
    datain1 = input("Enter the year(s) of the award: ")
    lstd1 = list(map(int, datain1.split(", ")))
    print()
    print(ndf.loc[ndf["Year"].isin(lstd1)].sort_values("Year"))
    while True:
        instr11b = "\nThe data based on the given year(s) has been displayed above. \n\nYou can perform the similar action again by \
entering '1', or head back to the choices by pressing 'C': "
        for instr11c in instr11b:
            print(instr11c, end="")
            sleep(0.001)
        inp4 = input(instr11c)
        print("-"*156)
        if inp4 == "1":
            year(ndf)
        if inp4 == "C":
            search(ndf)
            break 

def name(ndf): # assigning the user-given name to base the extraction of data.
    instr12 = "You can extract data for a single name or a list of names. If you want data for the latter, enter each \
name in the following option with comma as a separator (example: Albert, Marie, Niels): "
    for instr12a in instr12:
        print(instr12a, end="")
        sleep(0.001)
    print()
    datain2 = input("Enter the name(s) of the laureate: ")
    lstd2 = list(map(str, datain2.split(", ")))
    print()
    # using re library to match the user input to the data of the csv dataframe
    print(ndf.loc[ndf["Name"].str.match("(.*)"+"|".join(lstd2)+"(.*)")].sort_values("Name"))
    while True:
        instr12b = "\nThe data based on the given name(s) has been displayed above. \n\nYou can perform the similar action again by entering '2', or head back to\
 the choices by pressing 'C': "
        for instr12c in instr12b:
            print(instr12c, end="")
            sleep(0.001)
        inp5 = input(instr12c)
        print("-"*156)
        if inp5 == "2": 
            name(ndf)
        if inp5 == "C": 
            search(ndf)
            break

def dob(ndf): # assigning the user-given dob to base the extraction of data.
    instr13 = "You can extract data for a single dob or a list of dobs. If you want data for the latter, enter each \
dob in the following option with comma as a separator (example: 10/16/2004, 01/09/2004): "
    for instr13a in instr13:
        print(instr13a, end="")
        sleep(0.001)
    print()
    datain3 = input("Enter the dob(s) (dd/mm/yyyy or mm/dd/yyyy) of the laureate: ")
    lstd3 = list(map(str, datain3.split(", ")))
    print()
    print(ndf.loc[ndf["DOB"].str.match("(.*)"+"|".join(lstd3)+"(.*)", na = False)].sort_values("DOB"))
    while True:
        instr13b = "\nThe data based on the given dob(s) has been displayed above. \n\nYou can perform the similar action again by entering '3', or head back to\
 the choices by pressing 'C': "
        for instr13c in instr13b:
            print(instr13c, end="")
            sleep(0.001)
        inp6 = input(instr13c)
        print("-"*156)
        if inp6 == "3": 
            dob(ndf)
        if inp6 == "C": 
            search(ndf)
            break

def sex(ndf): # assigning the user-given sex to base the extraction of data.
    instr14 = "You can extract data for a single sex or a list of sexes. If you want data for the latter, enter each sex in the \
following option with comma as a separator (example: Male, Female): "
    for instr14a in instr14:
        print(instr14a, end="")
        sleep(0.001)
    print()
    datain4 = input("Enter the sex(es) of the laureate: ")
    lstd4 = list(map(str, datain4.split(", ")))
    print()
    print(ndf.loc[ndf["Sex"].isin(lstd4)].sort_values("Sex"))
    while True:
        instr14b = "\nThe data based on the given sex(es) has been displayed above. \n\nYou can perform the similar action again by entering '4', or head back to\
 the choices by pressing 'C': "
        for instr14c in instr14b:
            print(instr14c, end="")
            sleep(0.001)
        inp7 = input(instr14c)
        print("-"*156)
        if inp7 == "4": 
            sex(ndf)
        if inp7 == "C": 
            search(ndf)
            break

def birth(ndf): # assigning the user-given birth country to base the extraction of data.
    instr15 = "You can extract data for a single birth country or a list of birth countries. If you want data for the latter, \
enter each birth country in the following option with comma as a separator (example: India, Russia, China, United States of America): "
    for instr15a in instr15:
        print(instr15a, end="")
        sleep(0.001)
    print()
    datain5 = input("Enter the birth country(ies) of the laureate: ")
    lstd5 = list(map(str, datain5.split(", ")))
    print()
    print(ndf.loc[ndf["Birth Country"].str.match("(.*)"+"|".join(lstd5)+"(.*)", na = False)].sort_values("Birth Country"))
    while True:
        instr15b = "\nThe data based on the given birth country(ies) has been displayed above. \n\nYou can perform the similar action again by entering '5', or head back to\
 the choices by pressing 'C': "
        for instr15c in instr15b:
            print(instr15c, end="")
            sleep(0.001)
        inp8 = input(instr15c)
        print("-"*156)
        if inp8 == "5": 
            birth(ndf)
        if inp8 == "C":
            search(ndf)
            break

def aff(ndf): # assigning the user-given affiliation to base the extraction of data.
    instr16 = "You can extract data for a single affiliation or a list of affiliations. If you want data for the latter, enter each \
affiliation in the following option with comma as a separator (example: Harvard University, Stanford Univeristy, Princeton University): "
    for instr16a in instr16:
        print(instr16a, end="")
        sleep(0.001)
    print()
    datain6 = input("Enter the affiliation(s) of the laureate: ")
    lstd6 = list(map(str, datain6.split(", ")))
    print()
    print(ndf.loc[ndf["Affiliation"].str.match("(.*)"+"|".join(lstd6)+"(.*)", na = False)].sort_values("Affiliation"))
    while True:
        instr16b = "\nThe data based on the given affiliation(s) has been displayed above. \n\nYou can perform the similar action again by entering '6', or head back to\
 the choices by pressing 'C': "
        for instr16c in instr16b:
            print(instr16c, end="")
            sleep(0.001)
        inp9 = input(instr16c)
        print("-"*156)
        if inp9 == "6": 
            aff(ndf)
        if inp9 == "C": 
            search(ndf)
            break

def affp(ndf): # assigning the user-given affiliation place to base the extraction of data.
    instr17 = "You can extract data for a single affiliation place or a list of affiliation places. If you want data for the latter, enter each \
affiliation place in the following option with comma as a separator (example: Japan, United Kingdom, China): "
    for instr17a in instr17:
        print(instr17a, end="")
        sleep(0.001)
    print()
    datain7 = input("Enter the affiliation place(s) of the laureate: ")
    lstd7 = list(map(str, datain7.split(", ")))
    print()
    print(ndf.loc[ndf["Affiliation Places"].str.match("(.*)"+"|".join(lstd7)+"(.*)", na = False)].sort_values("Affiliation Places"))
    while True:
        instr17b = "\nThe data based on the given affiliation place(s) has been displayed above. \n\nYou can perform the similar action \
again by entering '7', or head back to the choices by pressing 'C': "
        for instr17c in instr17b:
            print(instr17c, end="")
            sleep(0.001)
        inp10 = input(instr17c)
        print("-"*156)
        if inp10 == "7": 
            affp(ndf)
        if inp10 == "C": 
            search(ndf)
            break

# specific data of a laureate extraction
def specl(ndf): # assigning the user-given specific row and column values to base the extraction of data.
    instr18 = "Here, you shall enter the name of the laureate whose specific data you want to be displayed. Upon doing so, the \
record of all the laureates with that name will be displayed. You then have to identify the index of the specific laureate from the \
output and type it in the next option. Then the record of that specific laureate will be displayed. \n"
    for instr18a in instr18:
        print(instr18a, end="")
        sleep(0.001)
    namdec()
    ind3 = int(input("Enter the index of the laureate whose data you want to be displayed: "))
    # column name
    col1 = input("Enter the specific data that you want to be displayed: ")
    print()
    print(ndf.loc[ind3, col1])
    while True:
        instr18b = "\nThe specific desired data of a laureate has been displayed above. \n\nYou can perform the similar action again by entering 'SL', or head back to\
 the choices by pressing 'C': "
        for instr18c in instr18b:
            print(instr18c, end="")
            sleep(0.001)
        inp11 = input(instr18c)
        print("-"*156)
        if inp11 == "SL": 
            specl(ndf)
        if inp11 == "C": 
            search(ndf)
            break

# specific data of every laureate extraction
def spece(ndf): # assiging the user-given specific column values to base the extraction of data.
    instr19 = "You can get specific data or a list of specific data of every laureate by following the instructions given ahead. \
If you want data for the latter, enter each specific data in the following option with comma as a separator (example: Year, Name, DOB):\n"
    for instr19a in instr19:
        print(instr19a, end="")
        sleep(0.001)
    col2 = input("Enter the specific data that you want to be displayed: ")
    lstd8 = list(map(str, col2.split(", ")))
    print()
    print(ndf[lstd8])
    while True:
        instr19b = "\nThe specific desired data of every laureate has been displayed above. \n\nYou can perform the similar action again by entering 'SE', or head back to\
 the choices by pressing 'C': "
        for instr19c in instr19b:
            print(instr19c, end="")
            sleep(0.001)
        inp11 = input(instr19c)
        print("-"*156)
        if inp11 == "SE": 
            spece(ndf)
        if inp11 == "C": 
            search(ndf)
            break

while True:
    ndf = realcsv() # assigning/updating the updated csv, ndf, as real csv
    home(ndf)
    break


