# HealthcareAnalytics-MapReduce
Health Data Analytics with MapReduce. This project analyzes patient records, identifying disease co-occurrences and frequencies to uncover insights into health trends.  

## Project Contents
The project is organized as follows:

- **MapReduceCode/ :** Contains Python scripts for MapReduce jobs.
  - `MRFrequentDiseases.py` : Computes the frequency of each disease.
  - `MRDiseaseCooccurrence.py` : Analyzes thefrequency of coexistence of two diseases.
  - `SymptomDiseaseMapping.py` : Maps symptoms associated with different diseases.

- **Data/ :** The data directory.
  - `donneesMedicales.csv` : Used for the first part.
  - `donneesMedicalesSymp.csv` : Used for the second part.

- **Results/ :** Contain Graphs .
  - Results of different jobs will be visualised here.

- **docs/ :** Additional documentation.
  - `RiahiFarah-projetMapReduce.docs` : Detailed project report.(french report only so far srry^^)
    These files were used (check report ) 
  - `outputCoexMaladies.txt`
  - `outputCoexMaladies_sorted.txt`
  - `sortFreqSymp.txt`
  - `sortingFreqSymp.py`

## Execution Instructions
1. Ensure Python is installed.
2. Install the `mrjob` library using the command: `pip install mrjob`.
3. follow the commands detailed in the report . 

## Notes
- The data used in this project is provided for testing purposes and does not come from an official medical source.
- This project was undertaken for experimentation and demonstration of MapReduce concepts in the healthcare domain.

Feel free to contact me for any questions or clarifications.

Riahi Farah
