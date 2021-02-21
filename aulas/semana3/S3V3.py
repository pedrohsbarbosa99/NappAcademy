"""
* S3V3 - Manipular arquivos CSV
"""
import csv

fieldname = ['name', 
            'username', 
            'credit_card', 
            'credit_card_expire', 
            'birthdate', 
            'gender'
]


with open('usernames.csv') as fp:
    csv_reader = csv.DictReader(fp)
    with open('new_file2.csv', 'w') as new_file:
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldname)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
