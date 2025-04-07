import re
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







