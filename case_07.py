#String Methods
#------------------------------------------
s.split(',')

pieces = [x.strip() for x in s.split(',')] #rstrip, lstrip work similarly

one, two, thr = pieces
print '::'.join(list([one, two, thr]))
print '--'.join(pieces)

print 'steady' in s
print 'set' in s

s.index('go')

s.count(',')

s.startswith('rea') #similarly .endswith()


