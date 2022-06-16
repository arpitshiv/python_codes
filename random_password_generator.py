from random import *
import string


alphabet=list(string.ascii_letters)
numbers=list(string.digits)
symbols=['!','@','#','$','%','^','&','*']
print(numbers)
password_list=[]
nr_letters=randint(0,5)
nr_symbols=randint(0,5)
nr_numbers=randint(0,5)
for char in range(0,nr_letters+1):
    password_list+=choices(alphabet)
    
for char in range(0,nr_symbols+1):
    password_list+=choices(symbols)
    
for char in range(0,nr_numbers+1):
    password_list+=choices(numbers)

shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(f"your password is {password}")

#for i in password_list:
    #print(i,end="")
