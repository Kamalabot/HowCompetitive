#Ljestvica coci12c5p1
import sys
musik = sys.stdin.readline()

mu_list = musik.split("|")

A = ["A","D","E"]
C = ["C","F","G"]

minor = major = 0
print(mu_list)

#Get each element
#Check 1st element 
    #if belongs to A, add 1 to minor
    #if belongs to C, add 1 to major
#go to last element
    #if == C then add 1 major
    #if == A then add 1 minor
for m in mu_list:
    if m[0] in A:
        minor += 1
        print(f"minor = {minor}")
    if m[0] in C:
        major += 1
        print(f"major = {major}")

if minor > major:
    print('A-mol')

elif major > minor:
    print('C-dur')

elif minor == major:
    
    if mu_list[-1][0] == 'A':
        print('A-mol')

    if mu_list[-1][0] == 'C':
        print('C-dur')
    
