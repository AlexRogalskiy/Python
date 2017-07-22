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

#List Methods
#------------------------------------------
Sample_List = [“Sample”, “List”]
Result = [item[0] for item in Sample_List]

List_of_lists = [ [1]*2 ] *5

Sample_List[:] = [“new”, “list”, “replaced”, “contents”]

Sample_List.extend([7.0,”append”]

Sample_List[:0] = [“workaround”, 8, 1.5]

Sample_list_New = [item for item in num_list if item <5]

