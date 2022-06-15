from random import *
testseed=int(input("enter seed value"))

seed(testseed)
random_int=randint(0.,1)
if random_int==1:
    print("heads")
else:
    print("tail")

