#input and open files
#divide the input into donor and acceptor sequences
#do the same thing as the TATA_box.py, except for the target gene with both TATA box and donor/acceptor sequence
#re.search TATA[AT]A[AT] and re.search {donor}.+{acceptor}
#count the number of TATA boxes: len+re.findal'TATA' 


input = input("input one of three possible splicedonor/acceptor combinations (GTAG, GCAG, ATAC)")

import re
import os
os.chdir('C:\\Users\\15041\\IBI1_2024-25\\Practical7')  #change the directory

input_file = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output_file = open(f'{input}_spliced_genes.fa','w')

donor = re.escape(input[:2])  #first two letter is the donor
acceptor = re.escape(input[2:])  #last two letter is the acceptor

gene = {}
count = 0
for line in input_file:
	line = line.rstrip()  #remove the whitespace from the right-hand side of the string
	if line.startswith('>'):
		gene_name_list = re.findall(r'gene:(\S+)',line)  #extract non-whitespace characters
		gene_name = gene_name_list[0]
		gene[gene_name]=''  #gene_name_list is a list, so we need to access the first element of the list
	else:
		gene[gene_name]+=line  #put the sequence of the gene together

target_gene={}
for gene_name,gene_seq in gene.items(): 
	if re.search(r'TATA[AT]A[AT]',gene_seq) and re.search(f'{donor}.+{acceptor}',gene_seq):
		target_gene[gene_name] = gene_seq  #store the target gene with both TATA box and donor/acceptor sequence
		tata_count = len(re.findall(r'TATA[AT]A[AT]', gene_seq))  #count the number of TATA boxes
		output_file.write(f'>{gene_name} {tata_count}\n{gene_seq}\n')  #output

input_file.close()
output_file.close()