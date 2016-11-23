#!/usr/bin/env python

import re
from .libs.bandit import Bandit

if __name__ == "__main__":
    bandit = Bandit()
    print("input 0 - {last_num}, or q".format(last_num=bandit.size - 1.0))
    while True:
        line = input()
        if re.match(r"[0-9]+", line):
            print(bandit.select(int(line)))
        elif "q" == line:
            print(line)
            break
        else:
            print("input 0 - {last_num}, or q".format(last_num=bandit.size - 1.0))
    print("expected value")
    print(bandit.reward_exp)
