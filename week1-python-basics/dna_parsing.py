# A DNA sequence is just a string of A, T, C, G
dna = "ATGCGATACGGATCG"

# Length of sequence
print("The length of the sequenceis:", len(dna))

# count how many types each bases present
print("The number of A's in the sequence is:", dna.count("A"))
print("The number of G's in the sequence is:", dna.count("G"))
print("The number of T's in the sequence is:", dna.count("T"))
print("The number of C's in the sequence is:", dna.count("C"))

# GC content is the percentage of G and C bases in the sequence
gc_count = dna.count("G") + dna.count("C")
gc_content = (gc_count / len(dna)) * 100
print(f"GC content: {gc_content:.2f}%")

# reverse complement of the sequence is obtained by reversing the sequence and replacing A with T, T with A, C with G, and G with C
complement_map = str.maketrans("ATCG", "TAGC")
rev_complement = dna[::-1].translate(complement_map)
print("The reverse complement of the sequence is:",rev_complement)

# Check the sequence for a specific motif

motif = "CGAT"
if motif in dna:
    print("The motif", motif, "is presenet in the sequence.")
else:
    print("The motif", motif, "is not present in the sequence")


# Transcription of DNA to RNA is done by replacing T with U

rna = dna.replace("T","U")
print("the transcribed RNA sequence is:", rna)

# Codon splitting: A codon is a sequence of three nucleotides that corresponds to a specific amino acid or stop signal during protein synthesis. We can split the DNA sequence into codons.

codons = [dna[i:i+3] for i in range(0, len(dna), 3)]
print("The codons in the sequence are:", codons)

# Input validation: Check if the sequence contains only valid nucleotides (A, T, C, G)

valid_nucleotides = {"A","T","C","G"}
is_valid = True

for base in dna:
    if base not in valid_nucleotides:
        is_valid = False
        break
print("The sequence contains only valid nucleotides:", is_valid)

valid_nucleotides = set("ATCG")
check_validity = all(base in valid_nucleotides for base in dna)
print("The sequence contains only valid nucleotides:", check_validity)
