import csv
import os
import fnmatch
import datetime
from datetime import date, timedelta
import shutil
import PySimpleGUI as sg     


###### GUI Layout for popup window		
layout = [      
			[sg.Text('Enter the dates to comapre (YYYY_MM_DD Format)')],      
			[sg.Text('Newest Date:', size=(15, 1)), sg.InputText('YYYY_MM_DD', key='_newFile_')],      
			[sg.Text('Oldest Date:', size=(15, 1)), sg.InputText('YYYY_MM_DD', key='_oldFile_')],      
			[sg.Submit(), sg.Cancel()]      
			]      
			
window = sg.Window('Title of Tool', layout)  ##Title for GUI popup here
event, values = window.Read()    
	
sg.Popup('You Chose to Compare:', values['_newFile_'], values['_oldFile_']) ##secondary popup to confirm selection


####Add Defect #'s to list below. (If there are non-numeric characters, put in quotes - EX '4747F')
defects_PPP = [6414,4510,4626,4896,8239,4129,2347,3508,7717,7716,'3153C','1Dont','2Dont','1Repri',10244,11457,11313,11903,11854] 
defects_WUPS = [4237,6317,5327,5231,4172,4312,5319,5008,5009,5254,5260,4763,3314,5107,7232,9325,9347,5105,5261,4110,4062,6219,4794,2184,10031,'7033F','7033H','4747F','4747H',8520,11526] 

local = r'C:'  # Local path for compare files to drop to
path = '\\\\server/Backup'  #Path where the data files are located
attach = r'C:\Attachments'  #Drops a copy of the latest compared file to this folder

today = values['_newFile_']
yesterday = values['_oldFile_']


###########################Main Compare Functions###############################

###PPP Report
def compare_PPP():
    os.chdir(path)
    cwd = os.getcwd()
    with open(Old, 'r') as Yest, open(New, 'r') as Today:
        fileone = Yest.readlines()
        filetwo = Today.readlines()
    os.chdir(local)
    with open('PPP_update_'+str(today)+'.csv', 'a') as outFile:
        for line in filetwo:
            if line not in fileone:
                    outFile.write(line)

for file in os.listdir(path): ##Update this path to point to directory where .csv is stored and for results output file
    for x in defects_PPP:
        if fnmatch.fnmatch(file,('RunDate_'+str(today)+'*'+str(x)+'*.csv')):
            New = file
##            print(file)
            for file2 in os.listdir(path):
                if fnmatch.fnmatch(file2,('RunDate_'+str(yesterday)+'*'+str(x)+'*.csv')):
                    Old = file2
##                    print(file2)
                    compare_PPP()       ##compare function call
                    os.chdir(local)
                    open('PPP_update_'+str(today)+'.csv', 'a').write(str(x)+' - Compare ran on: '+str(today)+' against ' +str(yesterday)+ ' for the above results^^^\n')


###WUPS Report                    
def compare_WUPS():
    os.chdir(path)
    cwd = os.getcwd()
    shutil.copy(New, attach)
##    print(cwd)
    with open(Old, 'r') as Yest, open(New, 'r') as Today:
        fileone = Yest.readlines()
        filetwo = Today.readlines()
    os.chdir(local)
    with open('WUPS_update_'+str(today)+'.csv', 'a') as outFile:
        for line in filetwo:
            if line not in fileone:
                    outFile.write(line)

for file in os.listdir(path): ##Update this path to point to directory where .csv is stored and for results output file
    for x in defects_WUPS:
        if fnmatch.fnmatch(file,('RunDate_'+str(today)+'*'+str(x)+'*.csv')):
            New = file
##            print(file)
            for file2 in os.listdir(path):
                if fnmatch.fnmatch(file2,('RunDate_'+str(yesterday)+'*'+str(x)+'*.csv')):           
                    Old = file2
##                    print(file2)
                    compare_WUPS()       ##compare function call
                    os.chdir(local)
                    open('WUPS_update_'+str(today)+'.csv', 'a').write(str(x)+' - Compare ran on: '+str(today)+' against ' +str(yesterday)+ ' for the above results^^^\n')

