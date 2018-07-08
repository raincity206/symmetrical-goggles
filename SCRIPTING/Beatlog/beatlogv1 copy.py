#!/usr/bin/python3
# feedback_solution.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os, sys, datetime, csv, platform

class Feedback:

    def __init__(self, master):
        
        master.title('Beatlog V1.0')
        master.resizable(False, False)
        master.configure(background = '#ffffff')
        
        # Style section
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#ffffff')
        self.style.configure('TButton', background = '#ffffff')
        self.style.configure('TLabel', background = '#ffffff', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      


        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        # Header
        self.logo = PhotoImage(file = 'Beatlog.gif')
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'BeatLog', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("Enter in the parent folder of where you create your Ableton Projects. Then, enter in a name of the text file")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = 'Project Path:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Export Name:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
        ttk.Label(self.frame_content, text = 'Comments:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
        
        self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
        self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))
        
        self.entry_name.grid(row = 1, column = 0, padx = 5)
        self.entry_email.grid(row = 1, column = 1, padx = 5)
        self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)
        
        ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        ttk.Button(self.frame_content, text = 'Clear',
                   command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

    def submit(self):
        print('Project Path: {}'.format(self.entry_name.get()))
        filePath = str('Project Path: {}'.format(self.entry_name.get()))
        print('Export Name: {}'.format(self.entry_email.get()))
        exportName = str('Export Name: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title = 'Scraped Ableton Files', message = 'Files Scraped!')

    
    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

####FUNCTIONS####

#Get Creation Time
def get_lastupdate_date(path):
    return os.path.getmtime(path)
    
# Get File Creation Time
def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

#Get Date From String
def convertIntToTimestamp(timeint):
    return str(datetime.datetime.fromtimestamp(timeint))

#Get Filename
def getFilename(name):
    return os.path.basename(name)
    
#Print List
def print_list(x):
    for i in range(0,len(x)):
        print(x[i])
    return x

#Listing Files
def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(('.als')):
                matches.append(os.path.join(root, filename))
    return matches
    
def mylistdir(directory):
    """A specialized version of os.listdir() that ignores files that
    start with a leading period."""
    filelist = os.listdir(directory)
    return [x for x in filelist
            if not (x.startswith('.'))]


filePath = r"/Users/blakenicholson/Dropbox/Ableton Projects"
dirs = mylistdir(filePath)
print(dirs)

def collectElements(dir):
    ## collecting elements into a list
    for directory in dir:
        for filename in directory:
            if filename.endswith(".als"):
                    thefiles.append(filename) 
    return thefiles
    
##print(collectElements(dirs))


file = open("example_test.txt","w+")
for item in fileList(filePath):
  file.write(os.path.basename(item) +", "+convertIntToTimestamp(get_lastupdate_date(item))+", "+convertIntToTimestamp(creation_date(item))+", "+os.path.abspath(item)+"\n")
  
file.close

#convert txt -> csv

with open('example_test.csv', 'w+') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerow(['File Name','Updated Date','Created Date','Path'])
    for item in fileList(filePath):
        a.writerow([ os.path.basename(item) , convertIntToTimestamp(get_lastupdate_date(item)), convertIntToTimestamp(creation_date(item)), os.path.abspath(item)])
    
    
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()