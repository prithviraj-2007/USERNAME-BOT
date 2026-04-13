
import string
import random
import secrets

#PASSWORD-GENERATION

def password(length=10):

    alphabet = string.ascii_letters + string.digits + "@#$!%^&*"
    pl=[
        secrets.choice(string.ascii_lowercase),  
        secrets.choice(string.ascii_uppercase), 
        secrets.choice(string.digits),           
        secrets.choice("@#$!%^&*")              
    ]
    pl += [secrets.choice(alphabet) for i in range(length - 4)]
    secrets.SystemRandom().shuffle(pl)
    print("PASSWORD:","".join(pl))
    


#MAIN-FUNCTION FOR MAIL GENERATION
def mail(f_name,l_name,mailname,b_year,initial,r_year):
    x=random.randint(99,9999)
    y=random.randint(99,9999)
    emails=[f"{f_name}{l_name}{x}@{mailname}.com",f"{f_name}.{l_name}{y}@{mailname}.com",f"{f_name}_{l_name}{y}@{mailname}.com",f"{f_name}{f_name}{x}@{mailname}.com",f"{l_name}.{f_name}{y}@{mailname}.com",f"{l_name}{x}@{mailname}.com",f"{f_name}.{y}@{mailname}.com",f"{f_name}{l_name}{b_year}@{mailname}.com",f"{f_name}.{l_name}{b_year}@{mailname}.com",f"{f_name}{f_name}{b_year}@{mailname}.com",f"{l_name}.{f_name}{b_year}@{mailname}.com",f"{l_name}{b_year}@{mailname}.com",f"{f_name}.{b_year}@{mailname}.com",f"{f_name}{l_name}{initial}{x}@{mailname}.com",f"{f_name}{initial}{x}@{mailname}.com",f"{f_name}.{initial}{x}@{mailname}.com",f"{l_name}{initial}{x}@{mailname}.com",f"{f_name}.{initial}{x}@{mailname}.com",f"{f_name}{l_name}{r_year}@{mailname}.com",f"{f_name}.{l_name}{r_year}@{mailname}.com",f"{f_name}{f_name}{r_year}@{mailname}.com",f"{l_name}.{f_name}{r_year}@{mailname}.com",f"{l_name}{r_year}@{mailname}.com",f"{f_name}.{r_year}@{mailname}.com"]
    
    print()
    
    emails=list(set(emails))
    emails.sort(key=len)

    print("NEW COMBINATION OF USERNAMES")
    print("-" * 30)
    for i in emails:
        print("➤  ", i)

    password()

    file_sv=input("SAVE FILE [YES/NO]   ").lower()
    if file_sv=="yes":
        with open("usernmpwd.txt","w") as f:
            for i in emails:
                f.write(i+"\n")



def insta(f_name,l_name,b_year,initial):
    x=random.randint(99,9999)
    y=random.randint(1,99)

    insta_uname=[f"{f_name}{l_name}_official",f"{f_name}_{l_name}._sparkzyy",f"{f_name}_{l_name}{y}",f"{f_name}_{f_name}.offl",f"its_{f_name}.404",f"{f_name}_{b_year}",f"the_real{f_name}.{y}",f"{f_name}_.{f_name}{x}",f"the_{l_name}_{x}",f"{f_name}.{b_year}_dev",f"the_{f_name}xz",f"x_{f_name}z{x}",f"nameis{f_name}{y}",f"being_{f_name}",f"{f_name}.{initial}_epic"]
    
    insta_uname=list(set(insta_uname))
    insta_uname.sort(key=len)

    print("NEW COMBINATION OF USERNAMES")
    print("-" * 30)
    for i in insta_uname:
        print("➤  ", i)


    inst_pwd=input("GENERATE PASSWORD:[YES/NO]     ").lower()
    if inst_pwd=="yes":
        password()
    
    
    file_sv=input("SAVE FILE [YES/NO]   ").lower()
    if file_sv=="yes":
        with open("usernmpwd.txt","w") as f:
            for i in insta_uname:
                f.write(i+"\n")
    else:
        print()
        print("Thank you for using Mail Generator😺")
        print("Have a great day 😊")

def twitter(f_name,l_name,b_year,initial,r_year):
    x=random.randint(99,999)
    y=random.randint(1,99)

    twitter_name=[f"@{f_name}{l_name}{x}",f"@{f_name}.{l_name}{y}",f"@{f_name}_{l_name}{y}",f"@{f_name}{f_name}{x}",f"@{l_name}.{f_name}{y}",f"@{l_name}{x}",f"@{f_name}.{y}",f"@{f_name}{l_name}{b_year}",f"@{f_name}.{l_name}{b_year}",f"@{f_name}{f_name}{b_year}",f"@{l_name}.{f_name}{b_year}",f"@{l_name}{b_year}",f"@{f_name}.{b_year}",f"@{f_name}{l_name}{initial}{x}",f"@{f_name}{initial}{x}",f"@{f_name}.{initial}{x}",f"@{l_name}{initial}{x}",f"@{f_name}.{initial}{x}",f"@{f_name}{l_name}{r_year}",f"@{f_name}.{l_name}{r_year}",f"@{f_name}{f_name}{r_year}",f"@{l_name}.{f_name}{r_year}",f"@{l_name}{r_year}",f"@{f_name}.{r_year}"]
    
    twitter_name=list(set(twitter_name))
    twitter_name.sort(key=len)

    print("NEW COMBINATION OF USERNAMES")
    print("-" * 30)
    for i in twitter_name:
        print("➤  ", i)


    twit_pwd=input("GENERATE PASSWORD:[YES/NO]     ").lower()
    if twit_pwd=="yes":
        password()
    
    
    file_sv=input("SAVE FILE [YES/NO]   ").lower()
    if file_sv=="yes":
        with open("usernmpwd.txt","w") as f:
            for i in twitter_name:
                f.write(i+"\n")
#GETTING USER INPUT
while True:
    def main():

        print("====CHOOSE DOMAIN====")
        print("1.GMAIL")
        print("2.OUTLOOK")
        print("3.I-CLOUD")
        print("4.YAHOO")
        print("5.REDIFF")
        print("6.HOTMAIL")
        print("7.LIVEMAIL")
        print("8.COMPANY MAIL")
        print("9.COLLEGE MAIL")
        print("10.OTHER--ENTER DOMAIN NAME")
        print("11.INSTAGRAM-USER NAME")
        print("12.TWITTER-X")
        print("CHOOSE BY NUMBER:")

        domain_lst=[1,2,3,4,5,6,7,8,9,10,11,12]


        domain=int(input("DOMAIN NUMBER:"))
        while domain not in domain_lst:
            print("INVALID--CHOICE")
            domain=int(input("DOMAIN NUMBER:"))

        f_name=input("FIRST NAME:").lower()
        while f_name.isdigit():
            print("INVALID NAME:")
            f_name=input("FIRST NAME:").lower()


        l_name=input("LAST NAME:").lower()
        while l_name.isdigit():
            print("INVALID NAME:")
            l_name=input("LAST NAME:").lower()

        initial=input("INITIAL:").lower()
        while initial.isdigit():
            print("Invalid-INITIAL")
            initial=input("INITIAL:").lower()

        b_year=input("BITH YEAR:")
        while not (b_year.isdigit() and len(b_year) == 4):
            print("INVALID INPUT ")
            b_year=input("BITH YEAR:")

        r_year=b_year[::-1]


        #ADDRESSING FOR RIGHT MAIL

        if domain==1:
            mailname="gmail"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==2:
            mailname="outlook"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==3:
            mailname="icloud"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==4:
            mailname="yahoo"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==5:
            mailname="rediff"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==6:
            mailname="hotmail"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==7:
            mailname="livemail"
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==8:
            mailname=input("COMPANY NAME:")
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==9:
            mailname=input("COLLEGE NAME:")
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==10:
            mailname=input("DOMAIN NAME:")
            mail(f_name,l_name,mailname,b_year,initial,r_year)

        elif domain==11:
            insta(f_name,l_name,b_year,initial)

        elif domain==12:
            twitter(f_name,l_name,b_year,initial,r_year)


    main()

    user_inp=input("DO YOU WANT TO EXIT  YES OR NO ").lower()
    if user_inp!="yes":
        break

    else:
        print()
        print("Thank you for using  Mail Generator😺")
        print("Have a great day 😊")


