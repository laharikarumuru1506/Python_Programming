email=input("enter the email:").lower().strip()
x=list(email.split("@"))
username=x[0]
domain=x[len(x)-1]
print("Your username is:",username)
print("Your domain name is:",domain)