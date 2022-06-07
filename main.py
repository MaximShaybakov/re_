import csv
import re
from pprint import pprint


def open_csv():
    with open('phonebook_raw.csv') as f:
        rows = csv.reader(f, delimiter=',')
        cont_ls = list(rows)
    return cont_ls

def data():
    pattern = '\s'
    for num,data in enumerate(open_csv()):
        f_name = data[0] #.split()
        pprint(f_name)
        first_name = re.findall('')



data()