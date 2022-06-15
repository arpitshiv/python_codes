row1=[' 😄',' 😄',' 😄']
row2=[' 😄',' 😄',' 😄']
row3=[' 😄',' 😄',' 😄']
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
x=int(input("enter row no in which treasure is located"))
y=int(input("enter colomn in which treasure is present"))
map[x][y]="b"
print(f"{row1}\n{row2}\n{row3}")