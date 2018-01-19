#!/usr/bin/python -tt
def main():
  general()
  meths()
  
def general():
  colors = ['red', 'blue', 'green']
  print colors[0]    ## red
  print colors[2]    ## green
  print len(colors)  ## 3
  
  z = [1,2,3]
  y = [4,5,6]
  x = z + y
  print z
  x = y
  x[0] = 7
  print y[0]
  
  squares = [1, 4, 9, 16]
  sum = 0
  for num in squares: sum += num
  print sum
  
  list = ['larry', 'curly', 'moe']
  if 'curly' in list: print 'yay'
  
  ## print the numbers from 0 through 99
  for i in range(100): print i
    
  ## Access every 3rd element in a list
  a = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
  i = 0
  while i < len(a):
    print a[i]
    i = i + 3
    
def meths():
  list = ['larry', 'curly', 'moe']
  list.append('shemp')         ## append elem at end
  list.insert(0, 'xxx')        ## insert elem at index 0
  list.extend(['yyy', 'zzz'])  ## add list of elems at end
  print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
  print list.index('curly')    ## 2

  list.remove('curly')         ## search and remove that element
  print list.pop(1)            ## removes and returns 'larry'
  print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
  list = ['a', 'b', 'c', 'd']
  print list[1:-1]   ## ['b', 'c']
  list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
  print list         ## ['z', 'c', 'd']
    
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()