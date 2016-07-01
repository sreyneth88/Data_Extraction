#!/usr/bin/python

# def invert_key_value(d):

# 	inverted_d={}
# 	tmp=[]

# 	for i in d:
# 		a= (d[i],i)
# 		tmp.append(a)
# 		print 'here'
# 	inverted_d = dict(tmp)

# 	return inverted_d

def new_function(l):
	tmp=[]
	for i in l:
		tmp.append(i)

	first = tmp[0]
	last = tmp[len(tmp)-1]

	return first,last

l=[1,'A',4,5,'B']

print new_function(l)