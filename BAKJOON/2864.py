#a = '555'
#b = '666'
#
#def find_max(c):
#    temp = []
#    for i in range(len(c)):
#        if c[i] == '5':
#            temp += '6'
#        else:
#            temp += c[i]
#    return temp
#max_a = find_max(a)
#max_b = find_max(b)
#print(max_a,max_b)

a = input()
a, b = a.split(' ')
minmax = [0,0]
def MinMax(a,b,c):
    d = ''
    for i in range(len(a)):
        if a[i] == b:
            d += c
        else:
            d += a[i]
    d = int(d)
    return d
minmax[0] += MinMax(a,'6','5')
minmax[0] += MinMax(b,'6','5')
minmax[1] += MinMax(a,'5','6')
minmax[1] += MinMax(b,'5','6')
for i in range(len(minmax)):
    print(minmax[i], end=' ')