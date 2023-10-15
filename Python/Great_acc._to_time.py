# Great according to time
import time
t=time.strftime("%H:%M:%S")
# hour=int(time.strftime("%H"))
name=input("Enter Your Name: ")
hour=int(input("Enter Hour: "))
print(hour)
if (hour>0 and hour<5):
    print("Hi, ",name," Good Night")
elif (hour>=5 and hour<12):
    print("Hi, ",name," Good Morning")
elif (hour>=12 and hour<17):
    print("Hi, ",name," Good Afternoon")
elif (hour>=17 and hour<22):
    print("Hi, ",name," Good Evening")
elif (hour>=22 and hour<=24):
    print("Hi, ",name," Good Night")
    
