from random import *
nameascsv=input("enter your names")
name=nameascsv.split(", ")
testseed=int(input("enter seed value"))

seed(testseed)
x=len(name)
random_int=randint(0,x-1)
print(f"{name[random_int]} is going to pay the bill")