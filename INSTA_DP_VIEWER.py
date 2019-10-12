import requests
import datetime
import os
import subprocess
import sys
#Author: Harshit-Gakhar
un=input("Enter User Name: ")                                               #asks user to enter username
sourceCode = str(requests.get('https://www.instagram.com/'+un+"/").text)    #gets the source code of the webpage of given user 
date = datetime.datetime.now()                                              #gets date to be saved in filename
time=str(date.day)+"-"+ str(date.month) + "-" +str(date.year)               #time, as string, in readble form
filename = un + " ({})".format(time) + ".jpg"                               #filename is the final name of file
left=sourceCode.find("pic_url_hd")+13                                       #left and right are the indices in source code, which has url of DP
right=sourceCode.find("requested_by_viewer")-3
hdurl=sourceCode[left:right]                                                #hdurl is the url of the DP 
response=requests.get(hdurl)                                                #reponse has the Display Picture Stored
f = open(filename,'wb')
f.write(response.content)                                                   #writing image in a image file called filename
f.close()
if sys.platform == "win32":                                     
        os.startfile(filename)                                              #to open the image on Windows
else:
    opener ="open" if sys.platform == "darwin" else "xdg-open"  
    subprocess.call([opener, filename])                                     #to open the image on Mac&Linux

