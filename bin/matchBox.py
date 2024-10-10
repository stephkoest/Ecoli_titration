import sys


def rev_comp_st(seq):
    '''Returns the reverse complement of a DNA strand'''
    complement_table = str.maketrans("ACGTacgt", "TGCAtgca")
    return seq.translate(complement_table)[::-1]


def make_boxes(boxf):
    '''Reads the file with DnaA boxes and returns a unique list'''
    boxel = set()
    with open(boxf, 'r') as boxes:
        for line in boxes:
            linestr = line.strip()
            if not linestr.startswith('>'):
                boxel.add(linestr)  # Directly add unique sequences to set
    return list(boxel)


def check_box(ID, outseq, boxel, gen_len, start):
    '''Compares a sequence in forwards and reverse complement against the list of boxes'''
    outseq = outseq.upper()
    rev_outseq = rev_comp_st(outseq)

    if outseq in boxel:
        print(f"{ID}\t{start}\t{gen_len}\t{outseq}\t1")
    elif rev_outseq in boxel:
        print(f"{ID}\t{start}\t{gen_len}\t{rev_outseq}\t-1")


def process_sequence(ID, sequence, boxel, circular, chunksize):
    '''Processes sequences in chunksize steps, handling circular sequences'''
    seqlen = len(sequence)
    startseq = sequence[:chunksize] if circular else ""  # Get start chunk if circular

    # Process the sequence in chunks
    for start in range(seqlen - chunksize + 1):
        outseq = sequence[start:start + chunksize]
        check_box(ID, outseq, boxel, seqlen, start)

    # Handle circularity by wrapping around the sequence
    if circular == 1:
        for start in range(1, chunksize):
            outseq = (sequence + startseq)[start:start + chunksize]
            check_box(ID, outseq, boxel, seqlen, seqlen + start)


def read_fasta(genomef, boxel, circular, chunksize):
    '''Reads in the target sequences with identifiers and hands them over to the processing function'''
    with open(genomef, 'r') as genome:
        sequence = ''
        ID = ''
        for line in genome:
            linestr = line.rstrip('\n')
            if linestr.startswith('>'):
                if sequence:
                    process_sequence(ID, sequence, boxel, circular, chunksize)
                header = linestr
                ID = linestr.split(" ")[0].lstrip(">")
                sequence = ''
            else:
                sequence += linestr
        if sequence:
            process_sequence(ID, sequence, boxel, circular, chunksize)


def main():
    if len(sys.argv) != 3:
        print("Usage: python matchBox.py <box_fasta> <input_fasta>")
        sys.exit(1)
    chunksize = 9  # Size of processed chunks, in this case 9 for the length of DnaA boxes
    circular = 1  # 1 if circular, 0 if not
    boxel = make_boxes(sys.argv[1])
    read_fasta(sys.argv[2], boxel, circular, chunksize)


if __name__ == '__main__':
    main()
