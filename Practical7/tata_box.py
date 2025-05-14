#open files
#remove the whitespace from the right-hand side of the string 
#extract non-whitespace characters: gene:(\S+)
#save to a dictionary with gene name as key and sequence as value
#search for TATA box: re.search TATA[AT]A[AT]
#save the target gene to a new dictionary with gene name as key and sequence as value
#output the target gene to a new file: output.write('>'+gene_name[0]+'\n'+gene[gene_name[0]]+'\n')


import re
import os
os.chdir('C:\Users\15041\IBI1_2024-25\Practical7')  #change directory

input = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
output = open('TATA_genes.fa','w')
gene={}

for line in input:
	line = line.rstrip()  #remove the whitespace from the right-hand side of the string 
	if re.search(r'^>',line):
		gene_name = re.findall(r'gene:(\S+)',line)  #extract non-whitespace characters
		gene[gene_name[0]]=''  #gene_name is a list, so we need to access the first element of the list
	else:
		gene[gene_name[0]]+=line  #put the sequence of the gene together

target_gene={}
for gene_name[0],gene[gene_name[0]] in gene.items(): 
	if re.search(r'TATA[AT]A[AT]',gene[gene_name[0]]):
		target_gene[gene_name[0]] = gene[gene_name[0]]  #gene_name[0] is the gene name, gene[gene_name[0]] is the sequence

for gene_name[0],gene[gene_name[0]] in target_gene.items(): 
	output.write('>'+gene_name[0]+'\n'+gene[gene_name[0]]+'\n')  #output

input.close()
output.close()







