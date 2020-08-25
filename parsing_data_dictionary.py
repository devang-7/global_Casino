import csv

with open('MA240820.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('market_mom.csv', 'w') as new_file:
        fieldnames = ['INDEX', 'PREVIOUS CLOSE', 'OPEN', 'HIGH', 'LOW',	'CLOSE', 'GAIN/LOSS']

        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:

            csv_writer.writerow(line)
            print(line)
        