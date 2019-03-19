'''
JSON to CSV
	- Converts .json predictions file from BERT to the required .csv format for submission.

Andrew Ying

Variables:
	with open('hi.csv', 'w', newline {str} -- [description]
'''
import csv
import json
with open('test_submission.csv', 'w', newline='', encoding='utf-8') as csv_fh:
    csv_writer = csv.writer(csv_fh, delimiter=',')
    csv_writer.writerow(['Id', 'Predicted'])

    with open('predictions.json', 'r') as j:
    	data = json.load(j)
    	print(data)

    	for key in data:
    		csv_writer.writerow([key, data[key]])