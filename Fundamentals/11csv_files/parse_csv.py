import csv

# Opening the csv file for reading
""" with open('employees.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file) # a delimiter can also be used on a reader

    # Creating a csv file to write into
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t') # contents of the csv lists will be separated by '\t'

        # Writing each line of the csv_file into new_file
        for line in csv_reader:
            csv_writer.writerow(line) """

# ~~~~~~~~~~ With dictionary reader

""" with open('employees.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)   # Turns each line of the csv file into a dictionary

    # Printing only the email key values
    for line in csv_reader:
        print(line['email']) """

with open('employees.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'company_name', 'address', 'city', 'county', 'state', 'zip', 'phone1', 'phone', 'email']
        
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        # writing the first line with the field names
        csv_writer.writeheader()

        # Writing each line of the csv_file into new_file
        for line in csv_reader:
            # Since I only want certain fieldnames to be written, I'll delete the unwanted ones
            del line['company_name']
            del line['address']
            del line['city']
            del line['county']
            del line['state']
            del line['zip']
            del line['phone1']
            del line['phone']
            csv_writer.writerow(line)