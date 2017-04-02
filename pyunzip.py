import os
import rarfile
import zipfile

os.chdir('c:/Users/jay/Downloads')

def makedir():
    if os.path.exists('c:/Users/jay/Downloads/zipfolder')==False:
        os.makedirs('c:/Users/jay/Downloads/zipfolder',1)
    else: print('folder already exists...')

def extract_zip():
    for i in os.listdir('.'):
        if zipfile.is_zipfile(i) is True:
            file = zipfile.ZipFile(i,'r')
            os.makedirs('c:/Users/jay/Downloads/zipfolder/'+i, 1)
            file.extractall('c:/Users/jay/Downloads/zipfolder/'+i)
            print(file)

def extract_rar():
    rarfile.PATH_SEP='/'
    for i in os.listdir('.'):
        if rarfile.is_rarfile('c:\\Users\\jay\\Downloads\\Windows XP NeoMAX Edition 2016') is True:
           print(a)

makedir()
extract_rar()