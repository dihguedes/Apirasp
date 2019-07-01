#Progam : TornonTurnoffApi

#lib
import cec
import time
import requests
import json

##cec control
cec.init()
tv=cec.Device(0)



#Address Api
serverApi='https://deft-virtue-240520.appspot.com'




def turn_on():
    
    tv.power_on()   
    
def turn_off():

    tv.standby()

def wait():
    
    time.sleep(300)

#Main
while True:
    
try:
    status= json.loads(requests.get(serverApi).text)
    print(status)
       
except:
    wait()
            
   
   if status['body'] == 'on':
      
       if tv.is_on() == False:
           turn_on()
           
           time.sleep(20)
           
                   
       else:
           wait()
                
                   
   else:
       
       if tv.is_on() == True:
           turn_off()
                 
       else:
           wait()
           

   
    
    
       
       
           
    
