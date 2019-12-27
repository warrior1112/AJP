a = int(input('enter 1st no :'))
b = int(input('enter 2nd no :'))
s = int(input('1.add 2.sub 3.mul 4.div 5.bitwise & 6.bitwise | 7.xor 8.logical and 9.logical or'))

t = {
	1 : (a+b),
	2 : (a-b),
	3 : (a*b),
	4 : (a/b),
	5 : (a&b),    
    6 : (a|b),
    7 : (a^b),
    8 : (a and b),
    9 : (a or b)
}
print(t[s])



























 

