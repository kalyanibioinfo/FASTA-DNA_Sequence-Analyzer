# ============================================
# FASTA DNA Sequence Analyzer
# Author: Kalyani Bedkihalkar
# Reads a FASTA file and performs basic DNA sequence analysis.
# ============================================

# Project Summary Variables
total_genes = 0
total_gc = 0
longest_gene = 0
shortest_gene = 999999

# Read FASTA File
with open("fasta.txt", "r") as file:
    
    # Read file line by line
    for line in file:
        line = line.strip()
        
        # Skip empty line
        if line == "":
            continue
         
             # Step 1: Read Gene Name
        if line.startswith(">"):
            print("Gene Name:", line)

        else:
            # Step 2: Read DNA Sequence
            print("DNA Sequence:", line)
            
            # Step 3: Calculate Sequence Length
            length = len(line)
            print("Length:", length)
            
            # Step 4: Calculate GC Content
            gc = line.count("G") + line.count("C")
            gc_percent = (gc / length) * 100
            print("GC Content:", round(gc_percent, 2), "%")
           
            # Update Project Summary 
            total_genes += 1
            total_gc += gc_percent
            
            if length > longest_gene:
            	longest_gene = length
            	
            if length < shortest_gene:
            	shortest_gene = length
            
            # Step 5: Count Nucleotides	
            a = line.count("A")
            t = line.count("T")
            g = line.count("G")
            c = line.count("C")
            
            # Print Nucleotide Counts
            print("A:", a)
            print("T:", t)
            print("G:", g)
            print("C:", c)
            
            # Step 6: Generate Complement DNA
            complement = ""

            for base in line:
                if base == "A":
                    complement += "T"
                elif base == "T":
                    complement += "A"
                elif base == "G":
                    complement += "C"
                elif base == "C":
                    complement += "G"

            print("Complement:", complement)

            reverse_complement = ""

            for base in line:
                if base == "A":
                    reverse_complement += "T"
                elif base == "T":
                    reverse_complement += "A"
                elif base == "G":
                    reverse_complement += "C"
                elif base == "C":
                    reverse_complement += "G"
                    
            # Step 7: Generate Reverse Complement
            reverse_complement = reverse_complement[::-1]

            print("Reverse Complement:", reverse_complement)
            
            # Step 8: DNA to RNA Transcription (T → U)
            rna = line.replace("T", "U")
            
            print("RNA Sequence:", rna)
            
            # Step 9: Protein Translation
            
            # Standard Genetic Code
            codon_table = {
                    "AUG": "M",
                    
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L",         "CUA": "L", "CUG": "L",

    "AUU": "I", "AUC": "I", "AUA": "I",

    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "AGU": "S",
    "AGC": "S",

    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",

    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",

    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

    "UAU": "Y", "UAC": "Y",

    "CAU": "H", "CAC": "H",

    "CAA": "Q", "CAG": "Q",

    "AAU": "N", "AAC": "N",

    "AAA": "K", "AAG": "K",

    "GAU": "D", "GAC": "D",

    "GAA": "E", "GAG": "E",

    "UGU": "C", "UGC": "C",

    "UGG": "W",

    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGA": "R", "AGG": "R",

    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",

    "UAA": "Stop",
    "UAG": "Stop",
    "UGA": "Stop"
     }
            
            protein = ""
            
            for i in range(0, len(rna), 3):
            	codon = rna[i: i+3]
            	
            	if len(codon) == 3:
            		amino_acid = codon_table.get(codon, "")
            		
            		if amino_acid == "Stop":
            			break
            			
            		protein += amino_acid
            		
            print("Protein Sequence:", protein)

            print()

# ============================================
# Project Summary
# ============================================        
print("========== PROJECT SUMMARY ==========")
print("Total Genes:", total_genes)
print("Average GC Content:", round(total_gc / total_genes, 2), "%")
print("Longest Gene Length:", longest_gene)
print("Shortest Gene Length:", shortest_gene)

print()
print("Analysis Completed Successfully!") 
print("=" * 45)