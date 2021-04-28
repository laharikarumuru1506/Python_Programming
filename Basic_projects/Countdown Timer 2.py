import time
def countdown(temp):
    while temp>0:
        mins,secs=divmod(temp,60)
        print("{:02d}:{:02d}".format(mins, secs))
        time.sleep(1)
        temp-=1
    print("Time's up")

temp=int(input("enter the countdown:"))
countdown(temp)