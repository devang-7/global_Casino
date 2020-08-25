import csv

with open('MA240820.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)

    with open('market_mom.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')

        for line in csv_reader:
            csv_writer.writerow(line)
            print(line)
            