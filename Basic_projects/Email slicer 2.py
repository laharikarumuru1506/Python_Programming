email=input("enter the email:").lower().strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
output="Your username is:{}\n Your domain name is:{}".format(username,domain_name)
print(output)