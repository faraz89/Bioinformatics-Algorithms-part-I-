def DNA_RC(DNA_seq):
   seq1=[]
   j=0
   for i in DNA_seq:
     seq1.append(i)
   while j<len(seq1):
    if seq1[j]=='A':
        seq1[j]='B'
    if seq1[j]=='T':
        seq1[j]='A'
    if seq1[j]=='B':
        seq1[j]='T'
    if seq1[j]=='C':
        seq1[j]='D'
    if seq1[j]=='G':
        seq1[j]='C'
    if seq1[j]=='D':
        seq1[j]='G'
    j+=1
   seq1.reverse()
   return ''.join(seq1)