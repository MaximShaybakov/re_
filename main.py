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
        phone_pattern = r'(\d{3})(\s?)(\)?)(\W?)(\d{3})(\W?)(\d{2})(\W?)(\d*)((\s?)(\(?)(доб?\.?)(\s?)(\d{4}?))*'
        phone_num = re.search(phone_pattern, text)
        if phone_num is not None:
            phone_list.append(f'+7({phone_num.group(1)}){phone_num.group(5)}-{phone_num.group(7)}-{phone_num.group(9)} {phone_num.group(13)}{phone_num.group(15)}')
    return phone_list


def ls():
    done = []


if __name__ == '__main__':
    # pprint(data())
    pprint(phone())


# (\W)(\(?)(доб.)(\W)(\d*)