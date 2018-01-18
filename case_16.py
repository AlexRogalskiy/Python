import json

with open('sample.json', 'r') as fp:
    obj = json.load(fp)

import urllib2, json
url = urllib2.urlopen('http://site.com/sample.json')
obj = json.load(url)

try:
    obj = json.loads("""{
    "firstName": "Alice",
    "lastName: "Hall",
    "age": 35
    }""")
except ValueError:
    print "error loading JSON"

firstName = obj["firstName"]
lastName = obj["Hall"]
age = obj["age"]

print type(obj["firstName"]), type(obj["lastName"]), type(obj["age"])

class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return '{{"firstName" = "{0}","lastName" = "{1}", "age" = {2}}}'.format(self.firstName, self.lastName, self.age)

def obj_creator(d):
    	return Person(d['firstName'], d['lastName'], d['age'])

with open('sample.json', 'r') as fp:
    obj = json.load(fp, object_hook = obj_creator)

print obj

person = Person("Crystal", "Newell", 27)


#python -mjson.tool glossary.json
#python -c 'import json; fp = open("glossary.json", "r"); obj = json.load(fp); fp.close(); print obj["glossary"]["title"]'