email = input("Enter your email address: ")
k,j,d=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@")==1):
            if(email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong email! Invalid character detected ")#5
                else:
                    print("Valid Email")
            else:
                print("Wrong email! '_' is misplaced ")#4
        else:
            print("Wrong email! Email must contain one '@' and one '.'")#3
    else:
        print("Wrong email! The first character must be a letter.")#2               
else:
    print("Wrong email! Please enter a valid email address,")#1                              

