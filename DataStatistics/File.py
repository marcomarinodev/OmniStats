import csv

class File:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_csv_data(self):
        with open(self.file_name) as csv_file:
            votes = []
            hours = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[1]} pesa {row[2]}.')
                    votes.append(float(row[1]))
                    hours.append(float(row[2]))
                    line_count += 1
            print(f'Processed {line_count} lines.')
            return(votes, hours)
