import csv

emails = {"very@cool.net", "not@cool.eu", "email@cool.com"}

directory = r'C:\Users\Eric\Desktop\emailcsvs\'

print("Starting")
# CSV Writer function
def write_csv(dirpath, file_name, collection):
    print("Open writer")
    # Open writer, set file_name and path
    with open(dirpath + file_name + '.csv', 'w') as email_file:
        print("Pass Writer")
        # Pass email_file to writer
        writer = csv.writer(email_file,
                            delimiter=' ',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)

        print("Writing throught collections:")
        # For every item inside the collection write a row
        for row in collection:
            print(row)
            writer.writerow([row])

write_csv(directory,'cool2', emails)
print("End.")
