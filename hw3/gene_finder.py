# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 2014

@author: Dimitar Dimitrov (dimitdim)
"""

from amino_acids import aa, codons
from random import shuffle

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """

    amino=""
    for i in range(len(dna)//3):
        amino += {codon:aa[codons.index(codonn)] for codonn in codons for codon in codonn}[dna[i*3:(i+1)*3]]
    return amino


def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """

    nuc=["CACGACAGAGGAC","GGCTGTTCTGGTTGC","AGTTCCGGCGGACCCCGT"]
    ami=["HDRG","GCSGC","SSGGPR"]
    for n in range(len(nuc)):
        print "input: " + nuc[n] + ",\nexpected output: " + ami[n] + ",\nactual output: " + coding_strand_to_AA(nuc[n])


def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """

    reverse=""
    m=""
    for n in dna:
        if n in ('A', 'a'):
            m = 'T'
        elif n in ('T', 't'):
            m = 'A'
        elif n in ('G', 'g'):
            m = 'C'
        elif n in ('C', 'c'):
            m = 'G'
        reverse = m + reverse
    return reverse


def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """

    nuc=["CACGACAGAGGAC","GGCTGTTCTGGTTGC","AGTTCCGGCGGACCCCGT"]
    rev=["GTCCTCTGTCGTG","GCAACCAGAACAGCC","ACGGGGTCCGCCGGAACT"]
    for n in range(len(nuc)):
        print "input: " + nuc[n] + ",\nexpected output: " + rev[n] + ",\nactual output: " +  get_reverse_complement(nuc[n])


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """

    stop=len(dna) 
    for i in range(len(dna)//3):
        if dna[i*3:(i+1)*3] in codons[10]:
            stop=i*3
            break
    return dna[0:stop]


def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """

    nuc=["ATGACAGAGGACTAG","ATGTGTTAATCTGGTTGC","ATGTCCGGCGGACCCCGT"]
    cut=["ATGACAGAGGAC","ATGTGT","ATGTCCGGCGGACCCCGT"]
    for n in range(len(nuc)):
        print "input: " + nuc[n] + ",\nexpected output: " + cut[n] + ",\nactual output: " +  rest_of_ORF(nuc[n])


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    ORFs=[]
    i=0
    while i < len(dna)//3:
        if dna[i*3:(i+1)*3] in codons[3]:
            orf=rest_of_ORF(dna[i*3:len(dna)])
            ORFs.append(orf)
            i+=len(orf)/3
        i+=1
    return ORFs


def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    nuc=["CACGACATGGGACGGCTGTTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGATTAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGCCGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTGTGAGAAGCCCACCTGGGCCAGTTGAAGTTCGAGGATTCGGTGACGGACGACCACTGGGACCGGCGGGTGGAGGGGCGGCTCAAGTGGGGACGCCACGTGCGGAGGGACCTGTTCAAGGACCGAAGACACTCGTGGCACGACTGGATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAATAAATTTCAGACTCACCCGCC"]
    orf=[["ATGGGACGGCTGTTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGG","ATGCGGGTCCAATTCCCGGTGCCGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTG","ATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAA"]]
    for n in range(len(nuc)):
	print "input: " + str(nuc[n]) + ",\nexpected output: " + str(orf[n]) + ",\nactual   output: " +  str(find_all_ORFs_oneframe(nuc[n]))


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    return find_all_ORFs_oneframe(dna) + find_all_ORFs_oneframe(dna[1:len(dna)]) + find_all_ORFs_oneframe(dna[2:len(dna)])


def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """

    nuc=["CACGACATGGGACGGCATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGATGAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGACGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTGTGAGAAGCCCACCTGGGCCAGTTGAAGTTCGAGGATTCGGTGACGGACGACCACTGGGACCGGCGGGTGGAGGGGCGGCTCAAGTGGGGACGCCACGTGCGGAGGGACCTGTTCAAGGACCGAAGACACTCGTGGCACGACTGGATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAATAAATTTCAGACTCACCCGCC"]
    orf=[["ATGGGACGGCATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGG","ATGAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGACGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTG","ATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAA","ATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGA"]]
    for n in range(len(nuc)):
	print "input: " + str(nuc[n]) + ",\nexpected output: " + str(orf[n]) + ",\nactual   output: " +  str(find_all_ORFs(nuc[n]))


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """

    return find_all_ORFs(dna) + find_all_ORFs(get_reverse_complement(dna))


def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    nuc=["CACGACATGGGACGGCATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGATGAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGACGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTGTGAGAAGCCCACCTGGGCCAGTTCATGTTCGAGGATTCGGTGACGGACGACCACTGGGACCGGCGGGTGGAGGGGCGGCTCAAGTGGGGACGCCACGTGCGGAGGGACCTGTTCAAGGACCGAAGACACTCGTGGCACGACTGGATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAATAAATTTCAGACTCACCCGCC"]
    orf=[["ATGGGACGGCATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGG","ATGAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGACGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTG","ATGTTCGAGGATTCGGTGACGGACGACCACTGGGACCGGCGGGTGGAGGGGCGGCTCAAGTGGGGACGCCACGTGCGGAGGGACCTGTTCAAGGACCGAAGACACTCGTGGCACGACTGGATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAA","ATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGA","ATGGCTCCGAGGTCGAATTGCCATAAACATCCAGTCGTGCCACGAGTGTCTTCGGTCCTTGAACAGGTCCCTCCGCACGTGGCGTCCCCACTTGAGCCGCCCCTCCACCCGCCGGTCCCAGTGGTCGTCCGTCACCGAATCCTCGAACATGAACTGGCCCAGGTGGGCTTCTCACACGCGCACGTCCAGCGAGTCCCGCCTGTCGCGCAACCCGTACAGCAGGTGCACGCGGTGCCGCAACCAGTCGCGCAGCCGGTGGAAGAACGTCACCGGGAATTGGACCCGCATCGGCACCGAGTCCAGCTTCACGCCCTTCATCCAGAACTACCACCCCTTCCTGTCCTTGTAGGAGAGGTCCCGGAGGCGTGGTATGAGCGGTCGCACGCGCGGTTGGAACGGGGTCCGCCGGAACTGCAACCAGACATGCCGTCCCATGTCGTG","ATGAACTGGCCCAGGTGGGCTTCTCACACGCGCACGTCCAGCGAGTCCCGCCTGTCGCGCAACCCGTACAGCAGGTGCACGCGGTGCCGCAACCAGTCGCGCAGCCGGTGGAAGAACGTCACCGGGAATTGGACCCGCATCGGCACCGAGTCCAGCTTCACGCCCTTCATCCAGAACTACCACCCCTTCCTGTCCTTG","ATGAGCGGTCGCACGCGCGGTTGGAACGGGGTCCGCCGGAACTGCAACCAGACATGCCGTCCCATGTCGTG"]]
    for n in range(len(nuc)):
	print "input: " + str(nuc[n]) + ",\nexpected output: " + str(orf[n]) + ",\nactual   output: " +  str(find_all_ORFs_both_strands(nuc[n]))


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    return max(find_all_ORFs_both_strands(dna), key=len)


def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    nuc=["CACGACATGGGACGGCATGTCTGGTTGCAGTTCCGGCGGACCCCGTTCCAACCGCGCGTGCGACCGCTCATACCACGCCTCCGGGACCTCTCCTACAAGGACAGGAAGGGGTGGTAGTTCTGGATGAAGGGCGTGAAGCTGGACTCGGTGCCGATGCGGGTCCAATTCCCGGTGACGTTCTTCCACCGGCTGCGCGACTGGTTGCGGCACCGCGTGCACCTGCTGTACGGGTTGCGCGACAGGCGGGACTCGCTGGACGTGCGCGTGTGAGAAGCCCACCTGGGCCAGTTCATGTTCGAGGATTCGGTGACGGACGACCACTGGGACCGGCGGGTGGAGGGGCGGCTCAAGTGGGGACGCCACGTGCGGAGGGACCTGTTCAAGGACCGAAGACACTCGTGGCACGACTGGATGTTTATGGCAATTCGACCTCGGAGCCATCGTCAAGGAGGACGGTCTACCCGGAGGGTTGCCCGGGAGGAGGGGAGGAACGTGGCCGGGAAGGACCAGAAATAAATTTCAGACTCACCCGCC"]
    lon=["ATGGCTCCGAGGTCGAATTGCCATAAACATCCAGTCGTGCCACGAGTGTCTTCGGTCCTTGAACAGGTCCCTCCGCACGTGGCGTCCCCACTTGAGCCGCCCCTCCACCCGCCGGTCCCAGTGGTCGTCCGTCACCGAATCCTCGAACATGAACTGGCCCAGGTGGGCTTCTCACACGCGCACGTCCAGCGAGTCCCGCCTGTCGCGCAACCCGTACAGCAGGTGCACGCGGTGCCGCAACCAGTCGCGCAGCCGGTGGAAGAACGTCACCGGGAATTGGACCCGCATCGGCACCGAGTCCAGCTTCACGCCCTTCATCCAGAACTACCACCCCTTCCTGTCCTTGTAGGAGAGGTCCCGGAGGCGTGGTATGAGCGGTCGCACGCGCGGTTGGAACGGGGTCCGCCGGAACTGCAACCAGACATGCCGTCCCATGTCGTG"]
    for n in range(len(nuc)):
	print "input: " + str(nuc[n]) + ",\nexpected output: " + str(lon[n]) + ",\nactual   output: " +  str(longest_ORF(nuc[n]))


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    l=0
    for i in range(num_trials):
        lst=list(dna)
        shuffle(lst)
        l=max(l,len(longest_ORF(collapse(lst))))
    return l


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    orflst=find_all_ORFs_both_strands(dna)
    lon=[]
    for orf in orflst:
        if len(orf) > threshold:
            lon.append(coding_strand_to_AA(orf))
    return lon
