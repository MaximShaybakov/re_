import csv
from itertools import groupby
import re
from pprint import pprint



rows_dict = []
with open('data_file/phonebook_raw.csv', 'r', encoding='utf-8') as csvfile:
    rows_dic_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for _, row1 in enumerate(rows_dic_reader):
        rows_dict.append(row1)

# list comprehenshion
name_ls = set([ls['lastname'].split()[0] for ls in rows_dict])


new = {}
ls = []
for person_data in rows_dict:
    new.setdefault(person_data['lastname'].split()[0], \
        [person_data['organization'], person_data['position'], person_data['phone'], person_data['email']])

pprint(new)

