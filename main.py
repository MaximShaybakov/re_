import csv
import re
from pprint import pprint

with open('phonebook_raw.csv', 'r') as f:
    rows = csv.reader(f, delimiter=',')
    cont_ls = list(rows)
for num,date in enumerate(cont_ls):
    first_name = date[0]
    pprint(first_name)
    if re.match('')