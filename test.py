import csv
from itertools import groupby
import re
from pprint import pprint



rows_dict = []
with open('data_file/phonebook_raw.csv', 'r', encoding='utf-8') as csvfile:
    rows_dic_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for _, row1 in enumerate(rows_dic_reader):
        rows_dict.append(row1)


new_ls_rowdict = []
for index, new_key in enumerate(rows_dict):
    new_key['lastname'] = new_key['lastname'].split()[0]
    new_ls_rowdict.append(new_key)
pprint(new_ls_rowdict)


# list comprehension
# name_ls = set([ls['lastname'].split()[0] for ls in rows_dict])

new = {}
new_ls = []
for person_data in rows_dict:
    new.setdefault(person_data['lastname'].split()[0], [person_data['organization'], person_data['position'], person_data['phone'], person_data['email']])
    new_ls.append(person_data)
pprint(new)


