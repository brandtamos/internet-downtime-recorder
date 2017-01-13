import urllib2
import time
import os.path
import datetime

currentState = ''
oldState = 'up' #assume we're up initially
stateFileName = 'statefile'
dataFileName = 'data.csv'

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

if(os.path.exists(stateFileName)):
	stateFile = open(stateFileName, 'rb+')
	oldState = stateFile.readline()
	stateFile.close()

#create the data file if it doesn't exist
if(not os.path.exists(dataFileName)):
	dataFile = open(dataFileName, 'wb+')
	dataFile.write('down_time,up_time\n')
	dataFile.close()

if(internet_on()):
	currentState = 'up'
else:
	currentState = 'down'
	
if(oldState != currentState):
	print 'state changed!'
else:
	print 'state is the same'

dataFile = open(dataFileName, 'ab+')

if(oldState == 'up' and currentState == 'down'):
	dataFile.write(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S') + ',')
if(oldState == 'down' and currentState == 'up'):
	dataFile.write(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S') + '\n')

stateFile = open(stateFileName, 'wb+') #overwrite the file
stateFile.write(currentState)
stateFile.close()