num = int(input("Please write a number here: "))
n = num / 2
if n == int(n):
    print("your number is even !")
    c = num % 4
    if c == 0 :
        print(f"and {num} is a multiple of four")
    else :
        print(f"and {num} is not a multiple of four")
else :
    print("your number is odd !")


x = int(input ("put a number: "))
y = int(input ("put a number to devide: "))
z = x / y
a = z / 2

print(f"{x} / {y} = {z}")

if a == int(a) :
    print("your first number divides evenly into the second. ")
else :
    print("your first number doesn't devide evenly into the second. ")