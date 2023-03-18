import os
import sys
from datetime import datetime
import Functions_String_HW   # import module to apply case normalization functionality
import StatCSV  # import module to collect words and letters statistic to csv files
import json
import xml.etree.ElementTree as ET


def file_json(filepath):

    input_file = json.load(open(filepath))
    content_item = []
    for i in input_file:
        for values in i.values():
            content_item.append(values)
        content_item.append('---------------------------\n\n')
    content_items = '\n'.join(content_item)
    return content_items


def file_xml(filepath):
    xml_file = ET.parse(open(filepath))
    root = xml_file.getroot()
    content_items = ''
    for item in root.iter('item'):
        content_item = []
        for data in item:
            content_item.append(data.text)
        content_item.append('---------------------------\n\n')
        content_items = content_items+'\n'.join(content_item)
    return content_items


class AllNews:
    def __init__(self, type1=None, text=None, city=None, exp_date=None, days_left=None, news_date=None):
        self.type1 = type1
        self.city = city
        self.text = text
        self.exp_date = exp_date
        self.days_left = days_left
        self.news_date = news_date

    def set_data(self):
        self.type1 = int(input("Enter news type\n1 - for News\n2 - for Private ad\n3 - for Event announcement\n"
                               "4 - to provide News by text file\n5 - to provide News by JSON file\n"
                               "6 - to provide News by XML file\n0 - to exit the program\nPlease do the choice: "))
        if self.type1 == 1:
            self.text = input("Enter news text: ")
            self.city = input("Enter city related to the news: ")
            self.news_date = datetime.now().strftime("%d/%m/%Y %H:%M")
            return f"\nNews -------------------\n{self.text}\n{self.city}, {self.news_date}\n" \
                   f"------------------------\n\n"
        if self.type1 == 2:
            self.text = input("Enter advertisement text: ")
            self.exp_date = str(input("Enter expiration date for the advertisement in the format dd/mm/yyyy: "))
            self.days_left = datetime.strptime(self.exp_date, "%d/%m/%Y") - datetime.now()
            return f"\nPrivate Ad ---------------\n{self.text}\nActual until: {self.exp_date}, " \
                   f"{self.days_left.days} days left\n--------------------------\n\n"
        if self.type1 == 3:
            self.text = input("Enter event title and date: ")
            self.city = input("Enter city where the event is organised: ")
            self.news_date = datetime.now().strftime("%d/%m/%Y %H:%M")
            return f"\nEvent announcement-----------\n{self.text}\n{self.city}, {self.news_date}" \
                   f"\n---------------------------\n\n"
        if self.type1 == 4:
            self.text = input("\nEnter path to the news source file: ")
            filepath = os.path.join(sys.path[0], self.text)
            fromfile = Functions_String_HW.normalize_case(open(filepath).read())
            os.remove(filepath)    # remove source file after processing
            return f"\n\n{fromfile}\n\n"
        if self.type1 == 5:
            self.text = input("\nEnter path to the news source file: ")
            filepath = os.path.join(sys.path[0], self.text)
            file_json(filepath)
            fromfile = Functions_String_HW.normalize_case(file_json(filepath))
            os.remove(filepath)    # remove source file after processing
            return f"\n\n{fromfile}\n\n"
        if self.type1 == 6:
            self.text = input("\nEnter path to the news source file: ")
            filepath = os.path.join(sys.path[0], self.text)
            file_xml(filepath)
            fromfile = Functions_String_HW.normalize_case(file_xml(filepath))
            os.remove(filepath)    # remove source file after processing
            return f"\n\n{fromfile}\n\n"
        if self.type1 == 0:
            print('\n-----Exit the program-----')
            sys.exit()  # method to exit the program
        else:
            print('\nWrong news type was entered')
            sys.exit()


# declare and set main function
def main():
    path = os.path.join(sys.path[0], 'output_news_file.txt')
    mode = 'a'
    with open(path, mode) as f:
        news = AllNews()
        f.write(news.set_data())
        f.close()
        StatCSV.txt_to_csv(path)   # collect statistic for output file to csv files
        print("\n"+"News is published to " + path + " at: " + datetime.now().strftime("%d/%m/%Y %H:%M") + "\n")


if __name__ == "__main__":
    main()

