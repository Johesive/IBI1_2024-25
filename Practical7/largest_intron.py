#re expression: GT.+AG
#largest_intron is a list, use [0] to get the first element, then use len()

import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT.+AG',seq)  #from GT to AG, use '+' for greedy matching
print(largest_intron)
print(len(largest_intron[0]))