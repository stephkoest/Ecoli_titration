import sys
import random

def read_fasta(fasta_file):
    """
    Reads a fasta file and returns a list of sequences.
    """
    sequences = []
    with open(fasta_file, "r") as f:
        sequence = ""
        for line in f:
            if line.startswith(">"):
                if sequence:  # Save the previous sequence before starting a new one
                    sequences.append(sequence)
                sequence = ""
            else:
                sequence += line.strip()  # Append sequence lines, removing newline characters
        if sequence:  # Append the last sequence
            sequences.append(sequence)
    return sequences

def shuffle_nucleotides(sequences, n_iterations):
    """
    Shuffles the nucleotides within each sequence for a specified number of iterations.
    Returns a list of shuffled nucleotide sequence sets.
    """
    shuffled_sequences = []
    for i in range(n_iterations):
        shuffled_set = []
        for sequence in sequences:
            nucleotides = list(sequence)  # Convert the sequence into a list of nucleotides
            while list(sequence) == nucleotides: # Make sure that the out sequence is different from in
                random.shuffle(nucleotides)  # Shuffle the nucleotides
            shuffled_sequence = ''.join(nucleotides)  # Rejoin the shuffled nucleotides into a string
            shuffled_set.append(shuffled_sequence)
        shuffled_sequences.append((i+1, shuffled_set))
    return shuffled_sequences

def write_fasta(shuffled_data, output_file):
    """
    Writes the shuffled sequences to a fasta file with appropriate headers.
    """
    with open(output_file, "w") as f:
        for iteration, shuffled_set in shuffled_data:
            for idx, sequence in enumerate(shuffled_set):
                header = f">shuffled_box_{idx+1}_{iteration}\n"
                f.write(header)
                f.write(sequence + "\n")

def main():
    if len(sys.argv) != 4:
        print("Usage: python shuffleBox.py <input_fasta> <n_iterations> <output_fasta>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    n_iterations = int(sys.argv[2])
    output_fasta = sys.argv[3]

    #Read in the box sequences from the input fasta file
    boxes = read_fasta(input_fasta)

    #Shuffle the nucleotides in each sequence for the specified number of iterations
    shuffled_data = shuffle_nucleotides(boxes, n_iterations)

    #Write the shuffled sequences to the output fasta file
    write_fasta(shuffled_data, output_fasta)

if __name__ == "__main__":
    main()

