#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    a = 'rock'
    b = 'paper'
    c = 'scissors'

    

    choices = [a, b, c]
    final = []

    if n == 1:
        for i in choices:
            final.append([i])
    else:
        for i in choices:
            final.append([i])
    
    return final
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')