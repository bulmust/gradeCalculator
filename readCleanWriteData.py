import pandas as pd

def readcsv_writexlsx(str_dataName_csv, *args):
    df = pd.read_csv(str_dataName_csv)
            
    # Drop All Columns with name 'Points'
    df=df.drop(df.filter(regex='Points').columns, axis=1)
    
    # Drop All Columns with name starting with 'Feedback'
    df=df.drop(df.filter(regex='Feedback').columns, axis=1)
    
    # Drop Unwanted Columns Coming from kwargs if any
    for arg in args:
        df=df.drop(arg, axis=1)
    
    # Make First Name and Last Name First Letter Capital
    df['First Name']= df['First Name'].str.title()
    df['Last Name']= df['Last Name'].str.title()
    # Remove Spaces from First Name and Last Name at the end
    df['First Name']= df['First Name'].str.rstrip()
    df['Last Name']= df['Last Name'].str.rstrip()
    
    # Change Email to Student Number
    df['Email Address']= df['Email Address'].str.split('@').str[0]
        
    # Change Email Address Name to Student Number
    df= df.rename({'Email Address':'Student Number'}, axis=1)
    
    # Change Student Number to Integer
    df['Student Number']= df['Student Number'].astype(int)
    
    # Sort Columns
    df=df.sort_index(axis=1)
        
    # ----------------------------------------
    #! Following part needs to be done manually for each document.
    orderCol= ['Student Number', 'First Name', 'Last Name', 'Final Notları', 'Arasınav']
    df=df[orderCol].join(df.drop(orderCol, axis=1))
    #! End of manual part
    # ----------------------------------------
    df.to_excel('grades.xlsx', index=False)