#define restriction
#use re.split to split the DNA sequence into a list of nucleotides, and check if each nucleotide is valid
#if the nucleotide is not valid, raise a ValueError
#count the length of the recognised sequence and the DNA length, and use for loop to traverse the DNA sequence
#for i in range(DNA_length-seq_length+1):
#if i to i+seq_length is the same as recognised_sequence:
#append(i+1)


def restriction(DNA_sequence, recognised_sequence):
    canonical_nucleotides = ['A', 'C', 'G', 'T']  #I want to use the re.split, and the output will include the space character, so I need to add it to the list of canonical nucleotides.
    for nucleotide in DNA_sequence:
        if nucleotide not in canonical_nucleotides:
            raise ValueError("Invalid nucleotide in DNA sequence.")  #there is only one return, so I use a raise statement instead of a return statement.

    DNA_length = len(DNA_sequence)
    seq_length = len(recognised_sequence)
    cut_sites = []
    for i in range(DNA_length-seq_length+1):  #i ranges from 0 to DNA_length-seq_length
        if DNA_sequence[i:i+seq_length] == recognised_sequence:
            cut_sites.append(i+1)  #the DNA_sequence[i] is the i+1 th when we count the position
    
    return cut_sites


DNA_sequence = "GATCGATCGATC"  #example and output
recognised_sequence = "GATC"
print(f"Cut sites in {DNA_sequence} for {recognised_sequence}: {restriction(DNA_sequence, recognised_sequence)}")
