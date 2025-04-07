import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
largest_intron = re.findall(r'GT.+AG',seq)  #from GT to AG, use '+' for greedy matching
print(largest_intron)

split_intron = re.split('',largest_intron[0])#in this way, the split_intron will contain 2 whiteblanks, so the length is split_intron-2
print(len(split_intron)-2)