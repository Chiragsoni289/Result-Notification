#This Program will Send you a Whatsapp message when GTU results will be declared
#Credits to Aagam Shah

import os
from twilio.rest import Client
from dotenv import load_dotenv
import urllib.request
import re 
import time



while 1: 
 
    html_content = urllib.request.urlopen('https://www.gtu.ac.in/result.aspx').read().decode('utf8')	
    matches = re.findall('BE SEM 5 - Regular', html_content); 
 
 
    if len(matches) == 0:  
       print ("Tenshan mat kar abhi tak nahi aaya hai") #will not send anything 
       time.sleep(1800) #sleep for 2 hours 
 
    else: 
       load_dotenv('tokens.env')
       account_sid =os.getenv('SID')
       auth_token = os.getenv('AUTH_TOKEN')
       client= Client(account_sid, auth_token)

       message = client.messages \
       .create(
         media_url=['https://www.memestemplates.com/wp-content/uploads/2022/09/jethalal-looking-from-window.jpg'],
	 body='GTU ka result aagaya hai BC !! baago' ,	
         from_='whatsapp:+14155238886' ,
         to='whatsapp:Your Number here'
       )
       print ("SMS Sent Thanks") 
       quit() 
