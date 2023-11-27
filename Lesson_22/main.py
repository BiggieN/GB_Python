var1 = '5 5'
var2 = '10 20 30 40 50'
var3 = '10 20 30 40 50'

length1 = len(var2)
integers1 = []
i = 0  # индекс текущего символа
 
while i < length1:
    s_int = ''  # строка для нового числа
    while i < length1 and '0' <= var2[i] <= '9':
        s_int += var2[i]
        i += 1
    i += 1
    if s_int != '':
        integers1.append(int(s_int))

length2 = len(var3)
integers2 = []
i = 0  # индекс текущего символа
 
while i < length2:
    s_int = ''  # строка для нового числа
    while i < length1 and '0' <= var3[i] <= '9':
        s_int += var3[i]
        i += 1
    i += 1
    if s_int != '':
        integers2.append(int(s_int))

a = set(integers1)
b = set(integers2)

c = a.intersection(b)

#c.discard(' ')
c = list(c)
c.sort()
for i in c:
    print(i, end=' ')