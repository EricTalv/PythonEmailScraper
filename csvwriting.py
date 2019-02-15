import csv

emails = {"very@cool.net", "not@cool.eu", "email@cool.com"}

dir1 = r'C:\Users\Eric\Desktop\emailcsvs'
dir2 = r''

print("Starting")
# CSV Writer function
def write_csv(dirpath, file_name, collection):
    print("Open writer")
    # Open writer, set file_name and path
    def writer():
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

    # check Dir Path
    if len(dirpath) is 0:
         with open(file_name + '.csv', 'w') as email_file:
            writer() 
                    
    else:
        with open(dirpath + '\\' + file_name + '.csv', 'w') as email_file:
            writer()
            
write_csv(dir1,'', emails)
print("End.")
