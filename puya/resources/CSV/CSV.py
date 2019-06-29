import csv
import os

path = os.path.dirname(os.path.abspath(__file__))


def show_csv_content(file):
    csv_name = file + ".csv"
    with open("\\" + path + file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
                print(f'\t{row[0]} has a duration of {row[1]} , and it\'s a {row[2]} show. That I\'m currently {row[4]}')
                line_count += 1
        print(f'Processed {line_count} lines.')


def add_entry_csv(file, data):
    csv_name = file + ".csv"
    with open("\\" + path + file, 'a') as csv_file:
        csv_append = csv.writer(csv_file)
        csv_append.writerow(data)


show_csv_content("Anime register")
