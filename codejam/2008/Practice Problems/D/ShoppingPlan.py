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
  return "{:.6f}".format(go((0,0), stores, items, price_of_gas))

def go(start, stores, items, price_of_gas):
  if len(items) == 0:
    return price_of_gas * hypot(0 - start[0], 0 - start[1])
   
  costs = list()
  
  for i in range(len(items)):
    if items[i][-1] == '!':
      item = items[i][:-1]
    else:
      item = items[i]

    for j in range(len(stores)):
      filtered_items = [x for x in stores[j][1] if item in x]
      if len(filtered_items) == 1:
        cost = int(filtered_items[0].split(":")[1])
        #print("cost=",cost)
        gas_here = price_of_gas * hypot(start[0] - stores[j][0][0], start[1] - stores[j][0][1])
        #print("here=",gas_here)
        if items[i][-1] == '!':
          gas_home = price_of_gas * hypot(0 - stores[j][0][0], 0 - stores[j][0][1])
          #print("home=",gas_home)
          costs.append( cost + gas_here + gas_home + go((0,0), stores, [x for x in items if item not in x], price_of_gas))
        else:
          costs.append( cost + gas_here + go(stores[j][0], stores, [x for x in items if item not in x], price_of_gas))
  return min(costs)



if __name__=="__main__":
    main()
