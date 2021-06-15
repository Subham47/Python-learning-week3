def problem3_1(txtfilename):
    filein=open(txtfilename,'r')
    sum=0
    for line in filein:
        print(line,end="")
        sum=sum+len(line)
       
    filein.close()
    print("\n")
    print("There are",sum,"letters in the file.")