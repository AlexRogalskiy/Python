rain_percent = { 1980: '17%', 1981: '15%', 1982: '10%'}
print rain_percent
print rain_percent[1980]

pairs = [('California', 37253956), ('Colorado', 5029196), ('Connecticut', 3574097), ('Delaware', 897934)]
population = dict(pairs)
print population

print {x: x**2 for x in xrange(10, 20)}

print 1980 in rain_percent
print '1980' in rain_percent

print users.setdefault('firstname', 'Jane')
del users['age']
users.pop('foo', None)

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27, 'dob': '15-sep-1971'}
map(lambda x : users.pop(x, None),['age', 'foo', 'dob'])
print users

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
users.clear()
print users

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for k in users:
  print k, '=>', users[k]

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for k in users.iterkeys():
  print k, '=>', users[k]

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for k in iter(users):
  print k, '=>', users[k]

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for index, key in enumerate(users):
  print index, key, '=>', users[k]

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for k, v in users.iteritems():
  print k, '=>', v

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for value in users.itervalues():
  print value

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
for k, v in users.items():
  print k, '=>', v

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
print users.keys()
print users.values()
