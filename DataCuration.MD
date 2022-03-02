# Data collection

### NCBI virus
- Download metadata (7,884,766 records) from [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/) database 
```sh
wget https://ftp.ncbi.nlm.nih.gov/genomes/Viruses/AllNuclMetadata/AllNuclMetadata.csv.gz
```
- Filter off human and other obvious non-marine viruses to decrease database size based on [NCBI's host distribution graph](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/)
- Map host metadata to marine taxonomic names in [World Register of Marine Species (WORMS) database](https://www.marinespecies.org/usersrequest.php) - not done yet
- Use case-insensitive keywords to extract marine data
```
marine
aqua
ocean
white spot syndrome virus
white sturgeon
Vibrio coralliilyticus
```
- Manually review and filter out irrelevant records 
```
uncultured
environmental
primer
vaccine
```

### NCBI genome (for bacterial genomes)
- Start with keyword search on [NCBI Genome](https://www.ncbi.nlm.nih.gov/genome) 
```
marine pathogen
fish pathogen
marine disease
```
- Download assembly and biosample metadata 
- Manually review and filter out irrelevant records from non-marine hosts
- Download sequence data

### MarRef
- Download metadata (1,271 records) from [MarRef](https://mmp2.sfb.uit.no/marref/) database 
- `MarRef_1.6.tsv` downloaded by clicking on Download -> Contextual TSV
- Identify marine pathogens (n=73) from metadata fields `host:disease`, `host:health_stage`, `host:other_clinical`, `host:pathogenicity`
- Map and download assembly, biosample, and sequence data from NCBI

### Creating BLAST databases

Use [NCBI BLAST+ software](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download). For example:

``` sh
makeblastdb -in virus.genomes.fasta -dbtype nucl -out virus -title virus
```
