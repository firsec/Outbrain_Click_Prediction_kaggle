import csv

with open("train_orig_test_shift.csv", "r") as csvfile:
  datareader = csv.reader(csvfile, delimiter=',')
  for row in datareader:
    print (row[0])
    cnt = 0;
    for index in range(1,len(row)):
      cnt +=1
      if int(row[index]) > 0:
        print ('1', end='')
      else:
        print ('0', end='')
      if cnt==28:
        print ()
        cnt=0



