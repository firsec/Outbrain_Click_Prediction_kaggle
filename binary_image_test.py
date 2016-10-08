
import csv

binary_image_f_train = open("test.csv", 'w+')
with open("test_orig.csv", "r") as csvfile:
  datareader = csv.reader(csvfile, delimiter=',')
  for row in datareader:
    cnt = 0
    if int(row[0]) > 127:
      binary_image_f_train.write('1')
      print ('1', end='')
    else:
      binary_image_f_train.write('0')
      print ('0', end='')
    cnt+=1
    for index in range(1,len(row)):
      cnt +=1
      if int(row[index]) > 127:
        print ('1', end='')
        binary_image_f_train.write(',1')
      else:
        print ('0', end='')
        binary_image_f_train.write(',0')
      if cnt==28:
        print ()
        cnt=0

    binary_image_f_train.write('\n')
    print ()


