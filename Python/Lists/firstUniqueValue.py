from collections import Counter
from collections import OrderedDict
def find_first_unique(lst):
    counts = OrderedDict.fromkeys(lst, 0)

    for num in lst:
        counts[num] += 1
    
    for key, value in counts.items():
        if value == 1:
            return key