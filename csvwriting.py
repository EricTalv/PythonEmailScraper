import csv

emails = {"very@cool.net", "not@cool.eu", "email@cool.com"}

print("Starting")
# CSV Writer function
def write_csv(file_name, collection):
    print("Open writer")
    # Open writer, set file_name
    with open(file_name + '.csv', 'w') as email_file:
        print("Pass Writer")
        # Pass email_file to writer
        writer = csv.writer(email_file)

        print("Writing throught collections:")
        # For every item inside the collection write a row
        for row in collection:
            print(row)
            writer.writerow(row)

write_csv('cool', emails)
print("End.")
