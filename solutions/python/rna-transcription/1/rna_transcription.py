def to_rna(dna_strand):
    dna = 'GCTA'
    rna = 'CGAU'
    rna_strand = ''
    for i in dna_strand:
        idx = dna.index(i)
        rna_strand+=rna[idx]
    return rna_strand
