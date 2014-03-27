def sum_squares_even(n):
    s=0
    for i in range(int(n/2+1)):
        s+=(i*2)**2
    return s

def pair_list_to_dictionary(lst):
    dct=dict()
    for i in range(int(len(lst)/2)):
        dct[lst[2*i]]=lst[2*i+1]
    return dct

def split_dictionary(odct):
    udct=dict()
    ldct=dict()
    for key in odct:
        if key[0].isupper():
            udct[key]=odct[key]
        elif key[0].islower():
            ldct[key]=odct[key]
        else: raise NameError('Key does not start with letter')
    return [udct,ldct]

def in_language(strn):
    state=True
    sect=0
    numA=0
    numB=0
    for i in strn:
        if i=='a' and sect==0:
            numA+=1
        elif i=='b':
            sect=1
            numB+=1
        else: state=False; break
    if numA!=numB: state=False
    return state

class DNASequence:
    def __init__(self, nucleotides):
        self.nucleotides=list()
        for nucleotide in nucleotides:
            if nucleotide in ['A','a','C','c','G','g','T','t']:
                self.nucleotides.append(nucleotide)
    def get_reverse_complement(self):
        rev=[]
        for i in range(len(self.nucleotides)):
            n=self.nucleotides[len(self.nucleotides)-1-i]
            if n in ['A','a']: n='T'
            elif n in ['T','t']: n='A'
            elif n in ['G','g']: n='C'
            elif n in ['C','c']: n='G'
            rev.append(n)
        return DNASequence(rev)
    def get_proportions_ACGT(self):
        A=0.0; C=0.0; G=0.0; T=0.0
        l=len(self.nucleotides)
        for n in self.nucleotides:
            if n in ['A','a']: A+=1
            elif n in ['T','t']: T+=1
            elif n in ['G','g']: G+=1
            elif n in ['C','c']: C+=1
        A=A/l; C=C/l; G=G/l; T=T/l
        return {'A':A,'C':C,'G':G,'T':T}
 
