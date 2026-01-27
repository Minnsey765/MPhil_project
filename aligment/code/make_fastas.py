#check what venv is being used.
import sys
print(sys.executable)

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
from alignment_funcs.read_gbk import read_gbk
print(read_gbk("OZ208999.1", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_info"))

#from alignment_funcs.file_maker import file_maker

#file_maker("symbol", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/raw_fastas", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_info", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/newGenBank.csv", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_data")
