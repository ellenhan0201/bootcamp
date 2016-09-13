#ex 1.3 a
def complement_base(base):
    """Returns the Watson-Crick complement of a base."""

    if base == 'A' or base == 'a':
        return 'T'
    elif base == 'T' or base == 't':
        return 'A'
    elif base == 'G' or base == 'g':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''
    rev_sequence= seq[::-1]
    # Loop through and populate list with reverse complement
    for base in rev_sequence:
        rev_seq += complement_base(base)

    return rev_seq
