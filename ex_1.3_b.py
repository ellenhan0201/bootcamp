#ex 1.3 b
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
    i=0;
    while i < len(seq):
    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement

        rev_seq += complement_base(base)

    return rev_seq
#or change all characters to lower case and then use replace function
