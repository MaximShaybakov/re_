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
    # pprint(rows_list)
    return (rows_list, rows_dict)

rows_list, rows_dict = open_file()


def names():
    cp_rows_dict = rows_dict.copy()
    new_row_dict = []
    count = 0
    for initials in rows_dict[1:]:
        if initials['lastname'].split()[0] == cp_rows_dict[count]['lastname'].split()[0] or (cp_rows_dict[count]['position'] or cp_rows_dict[count]['phone'] or cp_rows_dict[count]['email'] is not None):
            initials['position'] = cp_rows_dict[count]['position']
            initials['phone'] = cp_rows_dict[count]['phone']
            initials['email'] = cp_rows_dict[count]['email']
        new_row_dict.append(initials)
        count += 1
    pprint(new_row_dict)
    return new_row_dict


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
        if _['lastname'] not in names()[count][0]:
            try:
                _['lastname'] = names()[count][0]
                _['firstname'] = names()[count][1]
                _['surname'] = names()[count][2]
                _['phone'] = phone()[count]
                count += 1
            except IndexError:
                _['surname'] = ''
            data_correct.append(_)
    return data_correct

if __name__ == '__main__':
    # open_file()
    names()
    # pprint(correction_data())
    # print(rows_dict[0].values())
