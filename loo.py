# Reading an excel file using Python
import xlrd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from itertools import combinations

# Give the location of the file

loc = ('Book1.xls')
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
# combinations = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


allCountries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
developedCountries = [1, 2, 3, 4, 5, 6, 7, 8] 
developingCountries = [9, 10, 11, 12, 13, 14]

loo_arr = []

def train(allCountries, leaveIndex):
  A = []
  r = []

  for num in allCountries:
    if num == leaveIndex: continue
    list = []
    for i in range(2, 6):
      list.append(sheet.cell_value(num, i))
    r.append(sheet.cell_value(num, 1))
    A.append(list)


  A = np.array(A)

  w = optimize.nnls(A, r)

  print("w", w)

  tests = []
  names = []
  for num in [leaveIndex]:
    list = []
    for i in range(2, 6):
      list.append(sheet.cell_value(num, i))
    names.append(sheet.cell_value(num,0))
    tests.append(list)

  rc = np.matmul(tests, w[0])

  loo_arr.append([sheet.cell_value(leaveIndex, 1), rc[0]])
  # for index, name in enumerate(names):
  #   print(name, rc[index])

# print(loo_arr)
for i in range(1, 15):
  train(allCountries, i)

xs = []
ys = []

print(loo_arr)
for i in range(0, 14):
  xs.append(loo_arr[i][0])
  ys.append(loo_arr[i][1])

print(xs)
print(ys)

# print(np.linspace(0, 1, 1000))
colors=["#0000FF", "#00FF00", "#FF0066", "#45ad65", "#879aaa", "#ababab", "#ffaabb", "#bbFFaa", "#FF6666"
, "#aaffdd", "#fffb00", "#ffbbaa", "#aa00FF", "#aaFF66", "#0066FF"]


for i in range(0, 14):
    plt.scatter(xs[i], ys[i], color=colors[i])

# plt.scatter(xs, ys)
plt.plot(np.linspace(0, 0.02, 1000), np.linspace(0, 0.02, 1000))

plt.xlabel("Real Value")
plt.ylabel("Predicted Value")
plt.show()