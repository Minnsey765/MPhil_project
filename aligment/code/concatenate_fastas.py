"""
3. Concatenate all aligned sequences into a single sequence for each species (gene, or orientation)

Run big_fat_file_maker(raw_fol, csv_path, output, datatype)
- raw_fol = folder containing nexus alignments (aligned_fastas or edited_nexus)
- csv_path = path to csv file containing accession numbers (Project/newGenBank.csv)
- output = folder to output concatenated alignment (usually same as raw_fol - aligned_fastas or edited_nexus)
- datatype = datatype to align by (dna)

"""


from alignment_funcs.big_fat_file_maker import big_fat_file_maker

(big_fat_file_maker("C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/edited_nexus", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/newGenBank.csv", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/edited_nexus", "dna"))
