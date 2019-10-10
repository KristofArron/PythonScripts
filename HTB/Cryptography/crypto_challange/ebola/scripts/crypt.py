import os, sys
from itertools import cycle

h = open('decimals.txt','rb')
line = h.readline()
while line:
 if os.path.exists(sys.argv[1]):
  data = open(sys.argv[1]).read()
  xored = [chr(ord(a) ^ ord(b)) for a,b in zip(data, cycle(line))]
 
  #open('out', 'w').write(''.join(xored))
  print ''.join(xored)

 line = h.readline()
