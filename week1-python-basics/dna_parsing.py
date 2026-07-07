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
rev_complement = dna[::-1].replace("A","T").replace("T","A").replace("C","G").replace("G","C")
print("The reverse complement of the sequence is:",rev_complement)

# Check the sequence for a specific motif

motif = "CGAT"
if motif in dna:
    print("The motif", motif, "is presenet in the sequence.")
else:
    print("The motif", motif, "is not present in the sequence")
