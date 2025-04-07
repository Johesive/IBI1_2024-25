input = input("input one of three possible splicedonor/acceptor combinations (GTAG, GCAG, ATAC)")

import re
input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open(f'{input}_spliced_genes.fa','w')

donor = re.escape(input[:2])  #first two letter is the donor
acceptor = re.escape(input[2:])  #last two letter is the acceptor

gene = {}
count = 0
for line in input_file:
	line = line.rstrip()  #remove the whitespace from the right-hand side of the string 
	if re.search(r'^>',line):
		gene_name = re.findall(r'gene:(\S+)',line)  #extract non-whitespace characters
#gene_name is a list, so we need to access the first element of the list
		gene[gene_name[0]]=''
	else:
		gene[gene_name[0]]+=line  #store the sequence of each gene

target_gene={}
for gene_name,seq in gene.items(): 
	if re.search(r'TATA[AT]A[AT]',seq) and re.search(f'{donor}.+{acceptor}',seq):
		target_gene[gene_name] = seq  #store the target gene with both TATA box and donor/acceptor sequence
		tata_count = len(re.findall(r'TATA', seq))  #count the number of TATA boxes
		output_file.write(f'>{gene_name} {tata_count}\n{seq}\n')  #output

input_file.close()
output_file.close()