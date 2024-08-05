import csv

# Path to the CSV file
csv_file_path = 'data/strings.csv'

# Read and print the contents of the CSV file
with open(csv_file_path, 'r') as csvfile:
    result = "Hello, world!"
    reader = csv.reader(csvfile)    
    for row in reader:
        print(', '.join(row))  # Print each row as a comma-separated string
        result += str(row)
    print(f"::set-output name=my_output::{result}")