import re

def collection():
    content="Email\n"
    reg_email=r"[A-Za-z0-9]+@[A-Za-z0-9]+.[A-Za-z0-9]"
    reg_phone=r"(\d{3})?-?\.?(\(?\d\d\d\)?(-?\s?)?\.?)?\d\d\d-?\.?\d\d\d\d"
    with open('assets/potential-contacts.txt','r') as file:
        # file.read()
        # b=5
        # match = re.search(r'([\w.-]+)@([\w.-]+)', str)
        file=file.read()
        find_email=re.findall(reg_email,file)
        find_phone_num=re.fu(reg_phone,file)
        # print(find_email,len(find_email))
        print(find_phone_num)
    with open('assets/email.csv','w+') as file:
        file.write(str(find_email))
    # print(find_email)
    

collection()
    