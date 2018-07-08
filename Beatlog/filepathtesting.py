import os, sys, datetime, csv, platform

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


## INPUTDIRECTORIES
subpath = []
subdirs = []
thefiles = []
thelist = []
#/Users/blakenicholson/Documents/Personal/Projects/Music Production/Ableton Projects

#/Volumes/Samsung_T3/Old Ableton Projects/1.RELEASED/Neuromansah - DumbBlake Project

filePath = r"/Users/blakenicholson/Dropbox/Ableton Projects"
#filePath = raw_input('File path would you like to use: ')
dirs = mylistdir(filePath)
print(dirs)

#Get everything split
#only roots
#roots = next(os.walk(dirs for dirs in x)[0]
#print("Roots = %s" % roots)

#only direcs
#direcs = next(os.walk(dirs))[1]
#print("Directs = %s" % direcs)

#only files
#files = next(os.walk(files))[2]
#print("Files = %s" % files)


def collectElements(dir):
    ## collecting elements into a list
    for directory in dir:
    	for filename in directory:
    		if filename.endswith(".als"):
        			thefiles.append(filename) 
    return thefiles
 	
print(collectElements(dirs))


file = open("testtext.txt","w+")
for item in fileList(filePath):
  file.write(os.path.basename(item) +", "+convertIntToTimestamp(get_lastupdate_date(item))+", "+convertIntToTimestamp(creation_date(item))+", "+os.path.abspath(item)+"\n")
  
file.close

#convert txt -> csv

with open('testcsv.csv', 'w+') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerow(['File Name','Updated Date','Created Date','Path'])
    for item in fileList(filePath):
        a.writerow([ os.path.basename(item) , convertIntToTimestamp(get_lastupdate_date(item)), convertIntToTimestamp(creation_date(item)), os.path.abspath(item)])
    