import time
import urllib2
import cookielib
from getpass import getpass
import sys
import bluetooth  
import lightblue  
import subprocess


target_name = "Anand"  
file_to_send = "/home/lab316-25/Desktop/NPL/message.txt"  

lightblue.obex.sendfile( "BE:5F:46:65:72:DA",4, file_to_send ) 

def executeSomething():
    #code here
    

    fh = open("user.txt","r")
    username=fh.read()

    fh1 = open("pass.txt","r")
    passwd=fh1.read()

    fh2 = open( "/home/lab316-25/Desktop/NPL/message.txt","r")
    message = fh2.read()

    fh3 = open("reciever.txt","r")
    number= fh3.read()
    message = "+".join(message.split(' '))
 
    #Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
 
    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]
 
    try:
        usock = opener.open(url, data)
    except IOError:
        print "Error while logging in."
        sys.exit(1)
 
 
    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
 
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "Error while sending message"
    
    #sys.exit(1)
    #print "SMS has been sent."


#time.sleep(60)
#while True:
executeSomething()
subprocess.call(["python", "n1.py"])
