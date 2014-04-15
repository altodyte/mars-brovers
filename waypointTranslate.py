import string
s = '$,R,10,100,G,500,1000,B,90,270,V,0,0,W,0,0,X,0,55,Y,0,0,Z,10,0,S,19,29,122\r'

def getSymbols(data):
	syms = [];
	for c in string.letters:
		if c in data: syms.append(c)
	return syms

def parseString(data,target):
	d = data[string.find(data,target)+2:].split(',')
	p = (int(d[0]),int(d[1]))
	return p

def getWayPoints(data):
	sym = [i for i in getSymbols(data) if i >= 'T']
	way = sorted(parseString(data,s) for s in sym)
	return way

def getOurPosition(data):
	name = 'G'
	return parseString(data,name)

print(getWayPoints(s))
print(getOurPosition(s))