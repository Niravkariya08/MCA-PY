# 5.Write a program to demonstrate the use of break continue and pass statements.
lst1 = [10,13,20,30,35,40,43,45,49,50,69,60,70,80,90,100]
i=0
for i in lst1:
    if i%2==0:
        continue

    if i == 35 and i == 45:
        pass

    if i==80:
        break

    print(i)
        