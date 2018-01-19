class mylist():
    def __init__(self,l):
        self.l = l
    def extend(self,index):
        diff = index + 1 - len(self.l)
        if diff > 0:
            self.l.extend([ None for x in range(diff) ] )
    def __getitem__(self,index):
        # self.extend(index) ## depending on your taste
        return self.l[index]
    def __setitem__(self,index,value):
        self.extend(index) 
        self.l[index] = value
    def __repr__(self):
        return self.l.__repr__()
    
a = mylist([0,1,2,3])
print 'List: %s' % a
# print a[5]  ### this will throw an 'list index out of range' unless 
              ### you comment out the bit in __getitem__
a[5] = 5
print 'List: %s' % a
print a[5]

