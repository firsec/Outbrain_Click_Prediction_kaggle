
import csv

binary_image_f_train = open("train.csv", 'w+')
with open("train_orig.csv", "r") as csvfile:
  datareader = csv.reader(csvfile, delimiter=',')
  for row in datareader:
    binary_image_f_train.write('%d' % (int(row[0])))
    print (row[0])
    cnt = 0;
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


