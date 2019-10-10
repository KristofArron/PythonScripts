from collections import defaultdict

f2 = open('encrypted.bin','rb')
l = len(f2.read())
f2.close()

sub = {}



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
