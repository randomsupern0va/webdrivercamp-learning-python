#!/usr/bin/python3
import calculation as c

if __name__=="__main__":
	c1 = c.add
	c2 = c.sub
	c3 = c.mul 
	c4 = c.div

	a = 4
	b = 2

	print(c1(a,b))
	print(c2(a,b))
	print(c3(a,b))
	print(c4(a,b))


