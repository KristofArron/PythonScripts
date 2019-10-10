from collections import defaultdict

f2 = open('encrypted.bin','rb')
l = len(f2.read())
f2.close()

sub = {0:'a', 129:'b', 131:'c', 133:'d', 7:'e', 136:'f', 9:'g', 145:'h', 238:'i', 155:'j', 158:'k', 31:'l', 35:'m', 164:'n', 38:'o', 40:'p', 41:'q', 171:'r', 172:'s', 174:'t', 47:'u', 27:'v', 178:'w', 179:'x', 183:'y', 188:'z', 191:'A', 194:'B', 195:'C', 68:'D', 72:'E', 74:'F', 203:'G', 77:'H', 79:'I', 80:'J', 81:'K', 211:'L', 84:'M', 214:'N', 215:'O', 216:'P', 218:'Q', 220:'R', 93:'S', 223:'T', 96:'U', 230:'V', 103:'W', 233:'X', 234:'Y', 92:'Z', 237:'1 ', 110:'2', 240:'3', 243:'4', 117:'5', 119:'6', 249:'7', 21:'8'}



f = open('encrypted.bin','rb')
b = f.read(1)
t = []
d = defaultdict(int)
out = open('out','wb')
while b:
    print(b)
    if b == '\t':
        out.write(' ')
    else:
        t += [b]
        out.write(b)
    b = f.read(1)

print(t)
f.close()
