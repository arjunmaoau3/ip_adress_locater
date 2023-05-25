#Ip adress tracker----->
from ip2geotools.databases.noncommercial import DbIpCity
  
input(print('''
    __            __    ______   _       ______     _____    _     _   ______
    \ \          / /   |  ___/  | |     |  ____|   /  _  \  | \   / | |  ___/
     \ \  /  \  / /    |  ___/  | |     | |       |  | |  | |  \_/  | |  ___/
      \ \/ /\ \/ /     |  |___  | |____ | |____/\ |  |_|  | | |\_/| | | |___ 
       \__/  \__/      |_____/  |_____/  \______/  \_____/  |_|   |_| |_____/
  
                                                    -Coded by bibechan dhakal










[+] Press enter to continue  :  '''))
user=input("[+] Enter the valid ip adress to find details : ")

Response=DbIpCity.get(user,api_key='free')

Details=f'''                





                    
                 
     + ------------------------------------------------------+
      [+] The Details of the {Response.ip_address} is:          
                                                            
                                                            
      it lies in {Response.region} of {Response.city}       
      It lies in the {Response.latitude} degree  latitude   
      It lies in {Response.longitude} degree longitude      
     + ------------------------------------------------------+
'''



print(" --> The following information are saved in the Ipinformation.txt file")


with open("ip_info.txt","w") as f:
         f.write(Details)
print(Details)
