import pandas as pd
import numpy as np

import itertools
import datetime
import csv
import sys


filename = 'TRD1.csv'
with open(filename, 'r') as f:
	fieldnames = ['Time', 'PRICE', 'SIZE', 'EXCHANGE']
	reader = csv.DictReader(f, fieldnames=fieldnames)
	#reader = csv.reader(f, delimiter=',', quotechar='"')
	next(reader, None)
	try:
		#base = datetime.datetime.today()
		time_list = []#[row['Time'] for row in reader]
		price_list = []#[row['PRICE'] for row in reader]
		size_list = []#[row['SIZE'] for row in reader]
		exchange_list = []#[row['EXCHANGE'] for row in reader]
		for row in reader:
			time_list.append(pd.to_datetime(row['Time'], unit='ms'))
			price_list.append(float(row['PRICE']))
			size_list.append(int(row['SIZE']))
			exchange_list.append(row['EXCHANGE'])

		df = pd.DataFrame()
		df['datetime'] = time_list
		df['price'] = price_list
		df['size'] = size_list
		df['exchange'] = exchange_list

		groupByExchange = []
		sorted_df = df.sort_values(['datetime']).reset_index()
		for key, value in sorted_df['datetime'].iteritems():
			index = key
			length = len(sorted_df['datetime'])
			while(index < length and abs(value.timestamp() - sorted_df['datetime'][index].timestamp()) < 1):
				index = index + 1
			groupByExchange.append((key, index - key, value, sorted_df['datetime'][index-1]))
		maxTuple = max(groupByExchange, key=lambda item:item[1])
		#print(maxTuple)

		#roupByExchange = sorted_df.groupby(["exchange"], as_index=True).size().reset_index(name='count')
		#print(roupByExchange)

		#mergedcsvgroup = sorted_df.groupby('exchange')[sorted_df.columns].apply(lambda y: y.tolist())
		#print(mergedcsvgroup)

		#mergedcsvgroup = sorted_df.apply(lambda y: y.tolist())
		#print(mergedcsvgroup)

		#for key, group in itertools.groupby(sorted_df, lambda x: x[0]):
		#	print(key)
		#beer_map = {
		#	key: [ex for ex in sorted_df['exchange']] 
		#	for key, group in itertools.groupby(sorted_df['datetime'], lambda item: item)
		#}

		beer_map = {}  
		for key, group in itertools.groupby(sorted_df, lambda item: item):  
			beer_map[key] = [item for item in group]
		print(beer_map)

	except csv.Error as e:
		sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))



def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')