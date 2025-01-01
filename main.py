import time,os
blue= '\033[34m'
yellow='\033[33m'
default = '\033[0m' 
website ={"name": None, "url": None, "desc": None, "rating": None}

for name, value in website.items( ):
  website[name] = input(f"{name}: ")

  print( )
  time.sleep(1)
  os.system("clear")
print (f"{blue}Welcome to my school website")
for name , value in website.items( ):
  print (f"{yellow}{name} : {value} ")