## Complementary DNA

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

def DNA_strand(dna):
    str_dna = ''
    switch = {
        'A': 'T',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }
    for x in dna:
        if x in switch:
            str_dna += switch[x]
    return str_dna
