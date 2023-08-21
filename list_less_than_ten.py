a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for number in a :
    
    if number <= 5 :
        
        b.append(number)  
    else :
        continue

print(b)

c = int(input("write a number :").strip())
d = []
for number in a :
    
    if c >= number :
        
        d.append(number)
        
    else :
        
        continue
print(d)
        

