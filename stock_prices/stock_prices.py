#!/usr/bin/python

import argparse

def find_max_profit(prices):
    profit_list = []
    list2 = []
    max_profit = 0
    
    for i in range(1, len(prices)):
        for x in range(0, len(prices)):
            profit_list.append(prices[i] + prices[x])
        
        
    
    list2.append(max(profit_list))
    print(profit_list)
    print(list2)
    max_profit = max(profit_list)
    return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))