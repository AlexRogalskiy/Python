def findleft(s, left, right, t):
    l = left - 1 # s[l] < t
    r = right + 1 # s[r] >= t
    p = -1
    
    while l+1 != r:
        #invariant:s[l]<t and s[r]>=t
        m = l + (r - l)/2
        if s[m] >= t: # =
            r = m
        else:
            l = m
            
    if r < right and s[r] == t:
        p = r
    return p   
        
s = [7,7,7,9,12,12,12,27,38,38]

print findleft(s, 0, 9, 9)