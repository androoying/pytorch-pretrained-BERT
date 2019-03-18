# Ensembling Script

import csv
import json

with open('ensembled.csv', 'w', newline='', encoding='utf-8') as csv_fh:
    csv_writer = csv.writer(csv_fh, delimiter=',')
    csv_writer.writerow(['Id', 'Predicted'])

    one = csv.reader('dev_submission-baseline.csv', delimiter=',')
    two = csv.reader('dev_submission-new.csv', delimiter=',')


    for row in one:
    	ids.append(row[0])


    # for row in one:

    # with open('dev_submission-baseline.csv', 'r') as one:
    # 	with open('dev_submission-new.csv')
    # 	data = json.load(j)
    # 	print(data)

    # 	for key in data:
    # 		csv_writer.writerow([key, data[key]])