#ecoo19r2p1 Storing collection of e-mail addresses

import sys

from typing import List

def gettinput():

    getting_email = []
    
    mails = int(sys.stdin.readline().strip('\n'))
    

    for r in range(mails):

        getting_email.append(sys.stdin.readline().strip('\n'))
        
    return getting_email

def count_email(e_list: List[str]) -> int:

    corrected_email = []

    for mail in e_list:

        mail = mail.lower() #lowercase the entire email
        
        temp = mail.split('@')[0] #take the mail part before @

        temp = temp.replace('.','') #replace all the dots and remove the space there

        temp = temp.split('+')[0] #anything before the + sign is required

        temp = temp + '@' + mail.split('@')[1] #You take the values after the @ symbol

        corrected_email.append(temp)

    corrected_email = set(corrected_email) #converting to set 

    print(corrected_email)

    return len(corrected_email)

def main():

    for i in range(10):

        mails = gettinput()

        print(count_email(mails))

if __name__ == '__main__': main()