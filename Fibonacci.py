n = int(input("Number of terms you want to print: "))
a = 0
b = 1
c = 0

if n <= 0:
    print("Enter valid positive number")
else:
    print(a,b,end= " ")
    for i in range(2,n):
        c = a + b
        print(c,end = " ")
        a = b
        b = c
