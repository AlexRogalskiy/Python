import math

def LatticePath(down, right):
    
    if(down == 0 or right == 0):
        return 1
    
    else:
        return LatticePath(down -1, right) + LatticePath(down, right -1)
    
    
def LatticePath_v2(down, right):
	numPaths = 0
    
	return math.factorial(down + right) / (math.factorial(down)**2)
    
	
print LatticePath(3,3)


print LatticePath_v2(20,20)