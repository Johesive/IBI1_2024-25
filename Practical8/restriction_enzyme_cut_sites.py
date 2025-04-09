def restriction(DNA_sequence, recognised_sequence):
    import re
    canonical_nucleotides = ['A', 'C', 'G', 'T','']  #I want to use the re.split, and the output will include the space character, so I need to add it to the list of canonical nucleotides.
    DNA_split = re.split('', DNA_sequence)
    for nucleotides in DNA_split:
        if nucleotides not in canonical_nucleotides:
            raise ValueError("Invalid nucleotide found in DNA sequence")  #there is only one return, so I use a raise statement instead of a return statement.

    DNA_length = len(DNA_sequence)
    seq_length = len(recognised_sequence)  #count the length, and use for loop to traverse the DNA sequence
    cut_sites = []
    for i in range(DNA_length-seq_length+1):  #i ranges from 0 to DNA_length-seq_length
        if DNA_sequence[i:i+seq_length] == recognised_sequence:
            cut_sites.append(i+1)  #the DNA_sequence[i] is the i+1 th when we count the position
    
    return cut_sites


DNA_sequence = "GATCGATCGATC"  #example and output
recognised_sequence = "GATC"
print(f"Cut sites in {DNA_sequence} for {recognised_sequence}: {restriction(DNA_sequence, recognised_sequence)}")
