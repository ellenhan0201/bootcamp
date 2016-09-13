def ratio(x, y):
    """The ratio of `x` to `y`."""
    return x / y

def answer_to_the_ultimate_question_of_life_the_universe_and_everything():
    """Simpler program than Deep Thought's, I bet."""
    return 42
def think_too_much():
    """Express Caesar's skepticism about Cassius"""

    print("""Yond Cassius has a lean and hungry look,
He thinks too much; such men are dangerous.""")

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

    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)

    return rev_seq
def reverse_complement(seq):
    """Compute reverse complement of a sequence."""

    # Initialize reverse complement
    rev_seq = ''

    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)

    return rev_seq

    def display_complements(seq):
    """Print sequence above its reverse complement."""

    # Compute the reverse complement
    rev_comp = reverse_complement(seq)

    # Print template
    print(seq)

    # Print "base pairs"
    for base in seq:
        print('|', end='')

    # Print final newline character after base pairs
    print()

    # Print reverse complement
    for base in reversed(rev_comp):
        print(base, end='')

    # Print final newline character
    print()
