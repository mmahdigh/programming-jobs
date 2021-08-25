# Reading an excel file using Python
import xlrd
import numpy as np
from scipy import optimize
from itertools import combinations

# Give the location of the file

loc = ('Book1.xls')
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# combinations = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
A = []
r = []

allCountries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
developedCountries = [1, 2, 3, 4, 5, 6, 7, 8] 
developingCountries = [9, 10, 11, 12, 13, 14]

for num in allCountries:
  list = []
  for i in range(2, 6):
    list.append(sheet.cell_value(num, i))
  r.append(sheet.cell_value(num, 1))
  A.append(list)


A = np.array(A)
w = optimize.nnls(A, r)
# w = np.linalg.lstsq(A, r)

print("w", w)
# rows = [1, 4, 5, 6, 7, 11, 8, 9, 10]
tests = []
names = []
for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
  list = []
  for i in range(2, 6):
    list.append(sheet.cell_value(num, i))
  names.append(sheet.cell_value(num,0))
  tests.append(list)

rc = np.matmul(tests, w[0])

for index, name in enumerate(names):
  print(name, rc[index])
