# fasta_parser.py

def read_fasta(file_path):
    sequences = {}
    with open(file_path, "r") as f:
        name = ""
        seq = ""
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name:
                    sequences[name] = seq
                name = line[1:]
                seq = ""
            else:
                seq += line
        sequences[name] = seq
    return sequences


def stats(sequence):
    length = len(sequence)
    aa_counts = {aa: sequence.count(aa) for aa in set(sequence)}
    return length, aa_counts


if __name__ == "__main__":
    data = read_fasta("../data/sample.fasta")
    for name, seq in data.items():
        length, counts = stats(seq)
        print(f"{name} | Length: {length}")
        print(counts)
