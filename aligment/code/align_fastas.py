"""
2. sends fasta files generated in step 1 to clustal omega to be aligned and saves nexus files to a folder (aligned_fastas)

Run loop_clustal(fasta_dir, output_dir, interval)
- fasta_dir = folder containing sorted fasta files (fasta_data)
- output_dir = folder containing aligned nexus files (aligned_fastas)
- interval = wait period before sending another request to clustalOmega (not used)

"""

from alignment_funcs.loop_clustal import loop_clustal

loop_clustal("C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/fasta_data", "C:/Users/ojmin/OneDrive/Documents/UNI/MPhil/Project/aligment/code/aligned_fastas", interval=30)

"""
2.5 Manually trim aligned nexus files for each gene (species/orientation) using mesquite
- save trimmed edit as new nexus file in new folder (edited_nexus)
- edit each nexus file by deleting the top and bottom sections mesquite adds to match nexus file format produced by clustalOmega
- edit each nexus file by replacing {top} with "begin data;", the {bottom} with "end;" and adding "NTAX=XY" and "NCHAR=WXYZ" to the dimensions line
"""