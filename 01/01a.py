import csv

a1 = 0
a2 = 0
iter = 0
input = []

with open('./in01a.txt') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

  for row in csv_reader:
    input.append(int(row[0]))

  for one in input:
    for two in input:

      sum = one + two
#      print(iter, one, two, sum)
      if sum == 2020:
        a1 = one
        a2 = two
      iter = iter + 1

print("number 1: ",a1)
print("number 2: ",a2)
print("product: ",a1*a2)
print("iterations: ",iter)
