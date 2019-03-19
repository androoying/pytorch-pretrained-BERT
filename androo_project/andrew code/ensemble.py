'''Script to ensemble BiDAF and BERT models

Andrew Ying [partying@stanford.edu]

This script takes the .csv prediction files from the BiDAF and BERT models and 
ensembles them in a variety of ways. 

The one I settled on was a stochastic model where when there is disagreement,
BERT prevails 0.98 of the time and BiDAF prevails 0.02 of the time. Obviously,
this is more of a makeshift method. However, I viewed it as an approximation of the
fact that occasionally, the BiDAF model does yield a better answer than the BERT model.

Further work could fine-tune this script to attempt to get to the ``sweet spot'' 
for when BiDAF should prevail and when BERT should prevail. 
'''

import csv
import json
import random

baseline_file_name = 'test_submission_baseline.csv'
model_file_name = 'test_submission_model.csv'

with open('ensembled.csv', 'w', newline='', encoding='utf-8') as csv_fh:
    csv_writer = csv.writer(csv_fh, delimiter=',')
    csv_writer.writerow(['Id', 'Predicted'])

    with open(baseline_file_name) as baseline:
        with open(model_file_name) as model:
            # read_baseline = sorted(csv.reader(baseline, delimiter = ','), key = lambda row: row[0])
            # read_model = sorted(csv.reader(model, delimiter = ','), key = lambda row: row[0])

            read_baseline = csv.reader(baseline, delimiter=',')
            read_model = csv.reader(model, delimiter=',')
            print('hi')

            baseline_dict = {}
            model_dict = {} 

            for row in read_model:
                model_dict[row[0]] = row[1]

            for row in read_baseline:
                baseline_dict[row[0]] = row[1]

            for key in model_dict:
                if key in baseline_dict:
                    if baseline_dict[key] == model_dict[key]:
                        csv_writer.writerow([key, baseline_dict[key]])
                    else:
                        if random.random() <= 0.02:
                            csv_writer.writerow([key, baseline_dict[key]])
                        else:
                            csv_writer.writerow([key, model_dict[key]])


            # count = 0
            # for model_row in read_model:
            #     for baseline_row in read_baseline:
            #         if str(baseline_row[0]) == str(model_row[0]):
            #             print('match')

            #             if str(baseline_row[1]) == str(model_row[1]):
            #                 csv_writer.writerow([str(baseline_row[0]), str(baseline_row[1])])
            #             else: # stochastic approach
            #                 if random.random() <= 0.25:
            #                     csv_writer.writerow([str(baseline_row[0]), str(baseline_row[1])])
            #                 else: 
            #                     csv_writer.writerow([str(baseline_row[0]), str(model_row[1])])