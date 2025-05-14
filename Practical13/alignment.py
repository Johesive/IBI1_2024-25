#Length: 222
#subcellular localisation: Mitochondion matrix
#250 hits
#The range of the percentage identity of these retrieved alignments is 83.3% to 100%.
#90.09%

import blosum as bl
import os
os.chdir(r'C:\Users\15041\IBI1_2024-25\Practical13')

seq_human_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\P04179.fa','r')
seq_mouse_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\P09671.fa','r')
seq_random_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\random.fa','r')

def read_fasta(file):
    seq=''
    for line in file:
        if line.startswith('>'):
            continue
        seq += line.strip()

    return seq


def score_sum(seq1, seq2):
    score_list=[]
    #set initial score as an empty list

    for	i in range(len(seq1)):	#compare each amino acid	
        score_list.append(blosum[seq1[i]][seq2[i]])	#add score if amino acids are different
    
    score=0
    for i in range(len(score_list)):
        score+=score_list[i]
    return score

seq_human=read_fasta(seq_human_file)
seq_mouse=read_fasta(seq_mouse_file)
seq_random=read_fasta(seq_random_file)
blosum = bl.BLOSUM(62)


print(f"Human-Mouse alignment:",score_sum(seq_human,seq_mouse))
print(f"Human-Random alignment:",score_sum(seq_human,seq_random))
print(f"Mouse-Random alignment:",score_sum(seq_mouse,seq_random))

