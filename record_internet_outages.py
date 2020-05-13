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

print 'Downtime recorder is running...'
print 'Connection state is polled every 15 seconds'
while(1):
	if(internet_on()):
		currentState = 'up'
	else:
		currentState = 'down'
		
	if(oldState != currentState):
		print '*** CONNECTION STATE CHANGED *** to ' + currentState
	else:
		print 'Connection state is still ' + currentState

	if(oldState == 'up' and currentState == 'down'):
		dataFile = open(dataFileName, 'ab+')
		dataFile.write(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S') + ',')
		dataFile.close()
	if(oldState == 'down' and currentState == 'up'):
		dataFile = open(dataFileName, 'ab+')
		dataFile.write(datetime.datetime.now().strftime('%m/%d/%y %H:%M:%S') + '\n')
		dataFile.close()

	#stateFile = open(stateFileName, 'wb+') #overwrite the file
	#stateFile.write(currentState)
	#stateFile.close()
	oldState = currentState;
	time.sleep(15);