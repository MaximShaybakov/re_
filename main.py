import csv
import re
from pprint import pprint


def open_csv():
    with open('phonebook_raw.csv') as f:
        rows = csv.reader(f, delimiter=',')
        cont_ls = list(rows)
        # print(cont_ls)
    return cont_ls

def data():
    initials_ = []
    for num,name in enumerate(open_csv()):
        text = ' '.join(name)
        initials_pattern = r'(^[А-Я]{1}[а-я]+)(\s?)([А-Я]{1}[а-я]+)(\s?)([А-Я]{1}[а-я]+)'
        init = re.search(initials_pattern, text)
        if init is not None:
            initials_.append(init.group(1, 3, 5))
    return initials_

def phone():
    phone_list = []
    for num,tel in enumerate(open_csv()):
        text = ' '.join(tel)
        phone_pattern = r'(\.?)([7|8]{1})(\s?)(\(?)(\d{3})(\s?)(\)?)(\W?)(\d{3})(\W?)(\d{2})(\W?)(\d*)'
        number = re.search(phone_pattern, text)
        if number is not None:
            tel_number = f'+7({number.group(5)}){number.group(9)}-{number.group(11)}-{number.group(13)}'
            phone_list.append(tel_number)
    done = [data() for name,num in data(),phone_list]
    return phone_list


def ls():
    done = []


if __name__ == '__main__':
    pprint(data())
    pprint(phone())


# (\W)(\(?)(доб.)(\W)(\d*)