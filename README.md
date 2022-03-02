# Topic4_TeamA (Aquadocs)

## AquaPathoPedia, a sequence database with analysis tools for marine microbial diseases

We created <b>AquaPathoPedia</b>, a sequence database for host-associated viral and bacterial pathogens in marine environments

AquaPathoPedia contains
- 2,681 viral genome records
- 542 bacterial genome records
- 226 full-length bacterial 16S rRNA gene records

AquaPathoPedia is useful for 
- Bacterial/viral marine pathogen evolutionary/phylogenetic analysis
- Analysis of host distribution of specific marine diseases
- Sequence analysis of pathogenic signatures in marine hosts


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
The sequence should be in fasta or multi-fasta format 

### Perform Blastn

Your sequences will be examined for matches against the database based on default parameters

### Download results:

You will be able to download and save the results in your local computer

## Reference

If you use project Aquadocs for your research, please cite:

*Manuscript in preparation
