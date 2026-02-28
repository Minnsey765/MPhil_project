#check what venv is being used.
import sys
#print(sys.executable)
#print(sys.path)
import bioinf_packages

"""
Generates fasta files of sequences corresponding to a gene, species, or orientation

Run file_maker(sort_crit, raw_file, meta_file, csv_path, output)
- sort_crit = dictionary key to generate fasta files by: symbol, orientation, species (sequence & accession)
- raw_file = raw fasta data folder (aligment/raw_fastas)
- meta_file = meta data folder (aligment/code/fasta_info)
- csv_path = path to csv containing accession numbers as str (project/newGenBank.csv)
- output = output directory path as str (aligment/code/fasta_data)

"""

"""
DELETE ALL PRESENT ITEMS IN FASTA DATA

otherwise they will be overwritten with duplicates and clustalOmega will not work!
"""
from bioinf_packages.alignment_funcs._overlord import overlord_function

print(overlord_function("C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/raw_fastas", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_info", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/newGenBank.csv", "C:/Users/ojmin/OneDrive/Documents/UNI/Python_Packages/tests/bioinf_packages/alignment_funcs/test_glossary.csv"))

#from alignment_funcs.file_maker import file_maker

#file_maker("symbol", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/raw_fastas", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_info", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/newGenBank.csv", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_data")
