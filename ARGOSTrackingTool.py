#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Azura Liu (yl720@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name= './data/raw/sara.txt'

#Create a file object
file_object = open(file_name, 'r')

#Read contents of file into a list
line_list = file_object.readlines()

#close the file
file_object.close()


#iterate through all lines in the line list
for lineString in line_list :
    if lineString[0] == "#" or lineString[0] == 'u' : continue  
     #=  if lineString[0] in ("#", 'u') : continue
    #split the string into a list of data items
    lineData=lineString.split()
    
    #extract items in list into variables
    record_id=lineData[0]
    obs_date=lineData[2]
    obs_lc=lineData[4]
    obs_lat=lineData[6]
    obs_lon=lineData[7]
    
    #print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat: {obs_lat}, lon: {obs_lon} on {obs_date}")
    






