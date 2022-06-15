from itertools import count


name1=input("enter your name")
name2=input("enter his or her name")
name1,name2=name1.lower(),name2.lower()
lover_names=name1+name2
t=lover_names.count("t")
r=lover_names.count("r")
u=lover_names.count("u")
e=lover_names.count("e")
true=t+r+u+e
l=lover_names.count("l")
o=lover_names.count("o")
v=lover_names.count("v")
e=lover_names.count("e")
love=l+o+v+e
love_persent=10*true+love
if love_persent>90:
    print("you both are like coke and mentos together")
elif love_persent>40:
    print(f"your love persent is {love_persent} you both are really doing well")
else:
    print('yuou love persent is {love_persent}')