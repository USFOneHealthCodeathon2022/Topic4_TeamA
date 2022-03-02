# Topic4_TeamA (Aquadocs)

# Title: Developing database and analysis tools for marine microbial diseases

## Purpose: 

1) Create an information and sequence database for bacterial and viral diseases in marine organisms
2) Provide a user-friendly GUI interface to gather information and scan for disease signatures based on user input

## Requirements
1) bash
2) conda 4.7.12
3) python 3.9.6
4) django 2.2.5
5) ncbi-blast-2.9.0+

## Installation instructions

## Download Project Aquadocs

https://github.com/USFOneHealthCodeathon2022/Topic4_TeamA.git

## Launching the web server

http://10.119.34.34:8004/Ocean/

## Examples

### Searching for information on a particular pathogen or host

1) Step 1: Launch the server http://10.119.34.34:8004/Ocean/
2) Step 2: Enter keywords such as 'Virus' or 'Bacteria'
3) Step 3: Once processing is completeted, click on 'download' to save the information

### Uploading your DNA sequence to search the database
The sequence should be in fasta format
Example:
>Seq1
TACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCG
GTCTGTCAAGTCGGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCATTCGAA
ACTGGCAGGCTAGAGTCTTGTAGAGGGGGGTAGAATTCCAGGTGTAGCGGTGAA
ATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCCCTGGACAAAGA
CTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGG
>Seq2
TACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCG
GTTTGTTAAGTCAGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCA
CTGATACTGGCAAGCTTGAGTCTCGTAGAGGGGGGTAGAATTCCAGGTGTAGC
GGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCCC
CTGGACGAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGG
>Seq3
TACGTAGGGTGCAAGCGTTATCCGGAATTATTGGGCGTAAAGGGCTCGTAGGCG
GTTCGTCGCGTCCGGTGTGAAAGTCCATCGCTTAACGGTGGATCCGCG
CCGGGTACGGGCGGGCTTGAGTGCGGTAGGGGAGACTGGAATTCCCGGTGTAA
CGGTGGAATGTGTAGATATCGGGAAGAACACCAATGGCGAAGGCAGGTC
TCTGGGCCGTTACTGACGCTGAGGAGCGAAAGCGTGGGGAGCGAACAGG
>Seq4
TACGGAGGGTGCAAGCGTTAATCGGAATTACTGGGCGTAAAGCGCACGCAGGCG
GTCTGTCAAGTCGGATGTGAAATCCCCGGGCTCAACCTGGGAACTGCA
TTCGAAACTGGCAGGCTGGAGTCTTGTAGAGGGGGGTAGAATTCCAGGTGTAGC
GGTGAAATGCGTAGAGATCTGGAGGAATACCGGTGGCGAAGGCGGCCC
CCTGGACAAAGACTGACGCTCAGGTGCGAAAGCGTGGGGAGCAAACAGG

### Perform Blastn

Your sequences will be examined for matches

### Download results:

You will be able to download and save the results

## Reference

If you use project Aquadocs for your research, please cite:

*Manuscript in preparation
