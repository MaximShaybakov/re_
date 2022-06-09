import csv
import re
from pprint import pprint

def open_file():
    with open('data_file/phonebook_raw.csv', 'r', encoding='utf-8') as csvfile:
        rows_list_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows_list = []
        for index, row in enumerate(rows_list_reader):
            rows_list.append(row)
    with open('data_file/phonebook_raw.csv', 'r', encoding='utf-8') as csvfile:
        rows_dic_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        rows_dict = []
        for index1, row1 in enumerate(rows_dic_reader):
            rows_dict.append(row1)
    return (rows_list, rows_dict)


def names():
    person_list = []
    for person_data in open_file()[0]:
        data = ' '.join(person_data)
        initials_pattern = r'([А-У]{1}\w*)\W([А-У]{1}\w*)(\W([А-У]{1}\w*))*'
        initials = re.match(initials_pattern, data)
        if initials is None:
            person_list.append('')
        else:
            person_list.append(initials.group().split())
    person_list.remove('')
    return person_list


def phone():
    phone_list = []
    for person_data in open_file()[0]:
        data = ' '.join(person_data)
        phone_pattern = r'(\d{1})\s?\(?(\d{3})\s?\)?\W?(\d{3})\W?(\d{2})\W?(\d+)(\s?\(?(доб\.)\s?(\d*))*'
        phones = re.search(phone_pattern, data)
        if phones is None:
            phone_list.append('')
        else:
            tel = f'+7({phones.group(2)}){phones.group(3)}-{phones.group(4)}-{phones.group(5)} {phones.group(7)}{phones.group(8)}'
            phone_list.append(tel.replace('NoneNone', '').strip())
    phone_list.remove('')
    return phone_list


def correction_data():
    count = 0
    data_correct = []
    for index,_ in enumerate(open_file()[1]):
        if _['lastname'] not in data_correct:
            try:
                _['lastname'] = names()[count][0]
                _['firstname'] = names()[count][1]
                _['surname'] = names()[count][2]
                _['phone'] = phone()[count]
                count += 1
            except IndexError:
                _['surname'] = ''
            data_correct.append(_)
    data_correct[3].pop(None)
    return data_correct

if __name__ == '__main__':
    pprint(correction_data())
