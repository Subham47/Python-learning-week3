import csv
def problem3_7(csv_pricefile, flower):
    infile = open(csv_pricefile)
    for row in csv.reader(infile):
        if(row[0]==flower):
            print(row[1])
    infile.close()
