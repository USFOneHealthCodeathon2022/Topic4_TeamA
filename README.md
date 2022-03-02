# Topic4_TeamA (Aquadocs)

## AquaPathoPedia, a sequence database with analysis tools for marine microbial diseases

We created <b>AquaPathoPedia</b>, a sequence database for host-associated viral and bacterial pathogens in marine environments

AquaPathoPedia (`aquapathopedia_dataset.tsv`) contains data from:
- 2,681 viral genome records
- 542 bacterial genome records
- 226 full-length bacterial 16S rRNA gene records

Data collection and curation pipeline is described [here](https://github.com/USFOneHealthCodeathon2022/Topic4_TeamA/blob/main/DataCuration.MD). All data (metadata, sequence data, and BLAST-formatted databaes) is available at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6323302.svg)](https://doi.org/10.5281/zenodo.6323302)

## Usage

AquaPathoPedia is useful for: 
- Bacterial/viral marine pathogen evolutionary/phylogenetic analysis
- Analysis of host distribution of specific marine diseases
- Sequence analysis of pathogenic signatures in marine hosts

Note:
> - Currently, the AquaPathoPedia web server http://10.119.34.34:8004/Ocean/ can only be accessed from University of South Florida's in-campus network 
> - Users can clone this github repository or download `website.zip` from this repository to run the web server locally

### Local installation requirements
1) bash
2) conda 4.7.12
3) python 3.9.6
4) django 2.2.5
5) ncbi-blast-2.9.0+

### Keyword search 

- Launch the server http://10.119.34.34:8004/Ocean/ or local server
- Enter keywords such as 'Virus' or 'Bacteria'
- A results page will show up once the search is completeted, click on 'download' to save the information

### BLAST search against AquaPathoPedia (coming soon)
- Upload sequence(s) in fasta or multi-fasta format 
- Sequence(s) will be searched against the database based on default BLAST parameters
- Download and save results

## Reference

If you use project AquaPathoPedia for your research, please cite:

*Manuscript in preparation
