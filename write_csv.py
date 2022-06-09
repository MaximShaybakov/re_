import csv
from pprint import pprint
from read_csv import correction_data

def csv_write():
    with open('data_file/phonebook_raw1.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(correction_data()[0].keys()),
                                                    delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for data in correction_data():
            writer.writerow(data)



if __name__ == '__main__':
    csv_write()