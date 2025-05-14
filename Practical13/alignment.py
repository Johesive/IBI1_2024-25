#Length: 222
#subcellular localisation: Mitochondion matrix
#250 hits
#The range of the percentage identity of these retrieved alignments is 58.1% to 100%.
#90.09%


#import blosum matrix 62
#function 1: read_fasta(file) to read fasta file
#in order to recognize the sequence, we need to skip the hearder line, and add the following lines with += line.strip()
#function 2: score_sum(seq1, seq2) to calculate the score of two sequences using blosum matrix
#score_list.append(blosum[seq1[i]][seq2[i]]), and then sum up the score_list
#function 3: similarity_comparison(seq1, seq2) to calculate the similarity of two sequences using edit distance
#compare each amino acid, if they are not the same, edit_distance += 1, and then calculate similarity using (1 - (edit_distance / len(seq1)))

import blosum as bl
import os
os.chdir(r'C:\Users\15041\IBI1_2024-25\Practical13')

def read_fasta(file):
    seq=''
    for line in file:
        if line.startswith('>'):
            continue #skip header line
        seq += line.strip()

    return seq


def score_sum(seq1, seq2):
    score_list=[] #set initial score as an empty list

    for	i in range(len(seq1)):	#compare each amino acid	
        score_list.append(blosum[seq1[i]][seq2[i]])	#add the score to the list
    
    score=0
    for i in range(len(score_list)):
        score+=score_list[i] #sum up

    return score


def similarity_comparison(seq1, seq2):
    edit_distance =	0		
    for	i	in	range(len(seq1)): #compare each amino acid	
        if	seq1[i]!=seq2[i]:				
            edit_distance += 1
    
    return (1 - (edit_distance / len(seq1))) #calculate similarity


seq_human_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\P04179.fa','r')
seq_mouse_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\P09671.fa','r')
seq_random_file=open(r'C:\Users\15041\IBI1_2024-25\Practical13\random.fa','r')
seq_human=read_fasta(seq_human_file)
seq_mouse=read_fasta(seq_mouse_file)
seq_random=read_fasta(seq_random_file)
blosum = bl.BLOSUM(62)

print(f"Human-Mouse alignment:",score_sum(seq_human,seq_mouse))
print(f"Human-Random alignment:",score_sum(seq_human,seq_random))
print(f"Mouse-Random alignment:",score_sum(seq_mouse,seq_random))

print(f"Human-Mouse similarity:",similarity_comparison(seq_human,seq_mouse))
print(f"Human-Random similarity:",similarity_comparison(seq_human,seq_random))
print(f"Mouse-Random similarity:",similarity_comparison(seq_mouse,seq_random))