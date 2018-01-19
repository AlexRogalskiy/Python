def DFS(edges, s, t, skip = []):
   if(s == t):
      return [s]
   if s not in edges: return []
   skip.append(s)
   for x in edges[s]:
       if x in skip: continue
       res = DFS(edges, x, t, skip)
       if(res):
           way = [s]
           way.extend(res)
           return way
   return []


edges = {'a':['b','c'],
         'c':['d','e'],
         'd':['f'],
         'f':['c'],
         'e':['f','g']}

way = DFS(edges, 'g', 'a')
if way:
  print ', '.join(map(str, way))
else:
  print 'No way'