import base64

f = open('hexes.txt','r')

line = f.readline()
while line != '':
    dec = line.lower().replace('\n','')
    b = base64.b64encode(dec.encode())
    print( b )
    print( '\n--------------------------------------\n' )
    line = f.readline()
