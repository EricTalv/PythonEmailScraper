import csv

emails = {"em1", "em2", "em3"}

print("Starting")
# CSV Writer function
def write_csv(file_name, collection)
    print("Open writer")
    # Open writer, set file_name
    with open(file_name, 'w') as email_file:
        print("Pass Writer")
        # Pass email_file to writer
        writer = csv.writer(email_file)

        print("Writing throught collections:")
        # For every item inside the collection write a row
        for row in range(1, len(collection))
            print(row)
            writer.writerow(row)



