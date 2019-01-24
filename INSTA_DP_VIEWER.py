import requests
import datetime
import os
"""
@author: Gakhar's
"""  
#asks user to enter username
un=input("Enter User Name: ")
#gets the source code of the webpage of given user 
sourceCode = str(requests.get('https://www.instagram.com/'+un+"/").text)
#gets date to be saved in filename
i = datetime.datetime.now()
time=str(i.day)+"-"+ str(i.month) + "-" +str(i.year)+"("+str(i.hour)+"_"+str(i.minute)+")" #time, as string, in readble form
#filename is the final name of file
filename = un + str(time) + ".jpg"
#left and right are the indices in source code, which has url of DP
left=sourceCode.find("pic_url_hd")+13
right=sourceCode.find("requested_by_viewer")-3
#hdurl is the url of the DP
hdurl=sourceCode[left:right]
#reponse has the Display Picture Stored    
response=requests.get(hdurl)
#writing image in a image file called filename
f = open(filename,'wb')
f.write(response.content)
f.close()
#to open the image
os.startfile(filename)

