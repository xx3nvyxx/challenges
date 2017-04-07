#!/user/bin/env python
"""Google Code Jam 2008: Problem D. Shopping Plan"""

from __future__ import print_function
from builtins import input
from numpy import hypot

def main():
    N = int(input())
    if N < 1 or N > 100:
        raise RuntimeError("N is not within the valid range")
    for i in range(N):
        num_items,num_stores,price_of_gas = map(int, input().split())
        r = ShoppingPlan(num_items,num_stores,price_of_gas)
        print("Case #" + str(i + 1) + ": " + r)

def ShoppingPlan(num_items,num_stores,price_of_gas):
  items = input().split()
  stores = list()
  for i in range(num_stores):
    #python3: x_pos,y_pos,*items = input().split()
    store = input().split()
    stores.append( [(int(store[0]),int(store[1])),store[2:]] )
  return "{:.7f}".format(go((0,0), stores, items, price_of_gas, 0))

def go(start, stores, items, price_of_gas, perishable):
  gas_home = price_of_gas * hypot(0 - start[0], 0 - start[1])
  if len(items) == 0:
    return gas_home 
  if start == (0,0):
    perishable = 0
  
  costs = list()
 
  if perishable == 1:
    costs.append(gas_home + go((0,0), stores, items, price_of_gas, 0))
    filtered_stores = [x for x in stores if x[0] == start]
  else:
    filtered_stores = stores

  for i in range(len(items)):
    p = perishable
    if items[i][-1] == '!':
      p = 1
      item = items[i][:-1]
    else:
      item = items[i]

    for j in range(len(filtered_stores)):
      filtered_items = [x for x in filtered_stores[j][1] if item in x]
      if len(filtered_items) == 1:
        cost = int(filtered_items[0].split(":")[1])
        gas_here = price_of_gas * hypot(start[0] - filtered_stores[j][0][0], start[1] - filtered_stores[j][0][1])
        costs.append( cost + gas_here + go(filtered_stores[j][0], stores, [x for x in items if item not in x], price_of_gas, p))
  return min(costs)



if __name__=="__main__":
    main()
