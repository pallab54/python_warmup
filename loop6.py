#write a program to print the multtiplication table of any number using a while loop

n = int(input("enter a number :"))
i = 1
while i <=10:
    print(f"{n} * {i}= {n*i}")    #formatted string
    i = i+1