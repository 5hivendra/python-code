#leap year Program
year = int(input( "enter the starting year: "))
year2 = int(input ("enter the ending year: "))
s = []
b = []
for i in range (year,(year2)+1):
    if i % 4 == 0:
        #if i % 100 != 0:
        s.append (i)

    else:
        b.append(i)

print("leap year:\n", s) 
print("Non leap year:\n", b)