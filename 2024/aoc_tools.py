from collections import deque, defaultdict, Counter
import re

def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def numsp(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]

def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

dq = _dq = deque
dd = _dd = defaultdict
ctr = _ctr = Counter
