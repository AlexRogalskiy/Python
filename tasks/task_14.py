'''This is my first solution on Coderbyte'''

def FirstReverse(str): 

  # code goes here
  ret_str = ''
  for l in range(len(str)-1,-1,-1):
    ret_str += str[l]
  return ret_str
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print FirstReverse(raw_input())           
