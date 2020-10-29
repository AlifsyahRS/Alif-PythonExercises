my_dna = ('AA AT AC AG TA TT TC TG CA CT CC CG GA GT GC GG')


def kmer_finder(dna, k):
    list_kmer = dna.split()
    kmer_count = {'k-mer(s)': 0}
    for i in list_kmer:
        if len(i) == k:
            kmer_count['k-mer(s)'] += 1
    return (kmer_count, k)


print("Original DNA:", my_dna)
print(kmer_finder(my_dna, 2)[0], "wherein k =", kmer_finder(my_dna, 2)[1])
