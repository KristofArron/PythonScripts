garbled_flag="HTB{0KWkNGwWhjwWtoWcGnTrGlWEbGlM}"

sub = {'0':'W', 'K':'3', 'W':'_', 'G':'0', 'j':'O', 'M':'A'}

cpy_flag = '%s' % garbled_flag
rst = []
for i in list(cpy_flag):
    if i in sub.keys():
        rst += [sub[i]]
    else:
        rst += [i]

print(''.join(rst))
