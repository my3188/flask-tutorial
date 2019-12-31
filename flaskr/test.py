import json
import sqlite3

def mayue(*arr):
  print('type:',type(arr),len(arr))
  for i in arr[0]:
    print('--',i)



a = (4,5,6,70)
b = [4,5,6,70]
mayue(a)
mayue(b)


print(json.dumps(a))

# for i in b:
#     print('-->',i)


conn = sqlite3.connect('test.sqlite')