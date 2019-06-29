import csv
import os

path = os.path.dirname(os.path.abspath(__file__)) + "\\"


def show_csv_content(file):
    csv_name = file + ".csv"
    with open(path + csv_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
                print(f'\t{row[0]} has a duration of {row[1]} , '
                      f'and it\'s a {row[2]} show. That I\'m currently {row[4]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
    csv_file.close()


def add_entry_csv(file, data):
    csv_name = file + ".csv"
    with open(path + csv_name, 'a', newline='') as csv_file:
        csv_append = csv.writer(csv_file)
        csv_append.writerow(data)
    csv_file.close()


def retrieve_data_csv(file, name):
    animeDataList = []
    csv_name = file + '.csv'
    with open(path + csv_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if name in row[0].lower():
                animeDataList.append(row)
    j = 0
    index = 0
    if len(animeDataList) != 1:
        for j in range(0, len(animeDataList)):
            print("[" + str(j) + "] " + (animeDataList[j])[0])
        try:
            index = input('\n[Animu-san] Ara ara, which of those you\'re refering to?\n[Kanna-chan] ')
            print(animeDataList[int(index)])
        except IndexError:
            print('[Animu-san] Ara ara, that didn\'t exist! ')

retrieve_data_csv('Anime register', 'idolm@ster')
