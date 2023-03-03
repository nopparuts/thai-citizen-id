import csv
import os


class AddressCode(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AddressCode, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.address_code = self.__readCodeData()

    def __readCodeData(self) -> dict[str, str]:
        # Read code list from csv file
        address_code = {}
        file = open(os.path.dirname(__file__) + '/code_list.csv')
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            address_code[row[0]] = row[1]
        file.close()
        return address_code
