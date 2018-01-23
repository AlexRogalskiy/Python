from array import array
numbers = array('i', [2, 4, 6, 8])
print numbers[0]

for number in numbers:
    print number

for i in range(len(numbers)):
    print numbers[i]

cars = ['Ford', 'Austin', 'Lancia']
cars = ['Ford', 'Austin']
print cars
other_cars = ['Lotus', 'Lancia']
cars.extend(other_cars)
print cars


name = "Joel"
job = "Programmer"
title = "{} the {}".format(name, job)


availability = ["Monday", "Wednesday", "Friday", "Saturday"]
result = " - ".join(availability)

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for i, day in enumerate(weekdays):
    print("{} is weekday {}".format(day, i))

i = 0
for day in weekdays:
    print("{} is weekday {}".format(day, i))
    i = i + 1

for key, value in d.items():
	print(key, value)

#pip install oauth2client
#pip install PyOpenSSL
#pip install gspread

import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("MUO_Python_Sheet").sheet1 # open sheet

all_cells = sheet.range('A1:C6')
print all_cells

for cell in all_cells:
	print cell.value

A1 = sheet.acell('A2').value # this cell contains "Ford"
coord = sheet.cell(3, 0).value
row = sheet.row_values(1) # first row
col = sheet.col_values(2) # models
sheet.update_acell('C2', 'Blue')

if sheet.acell('B3') != 'SAFETY':
	# something has changed in the sheet, DO NOT PROCEED
	raise Exception("Oh My, I'm not ready for this.")
else:
	# continue with your writing
	sheet.update_acell('C2','Blue')

