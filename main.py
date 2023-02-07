from os import path
from readCleanWriteData import readcsv_writexlsx

if __name__ == '__main__':
    fileName= 'FIZ365-Fizikte Bilgisayarlı Yöntemler I (22-23 GÜZ) grades - 02-07-2023, 01-41 PM.csv'
    path_curr= path.dirname(path.abspath(__file__))
    # File is in 'studentsGrade' folder
    path_file= path.join(path_curr, 'studentsGrade', fileName)
    
    excludeColumns= ['Final (Öğrenci Cevapları)', 'Final Hariç Ortalama Notlar']
    
    # Check if file exists
    if path.exists(path_file):
        readcsv_writexlsx(path_file, excludeColumns)
        print('Done.')
    else:
        quit('File does not exist.')