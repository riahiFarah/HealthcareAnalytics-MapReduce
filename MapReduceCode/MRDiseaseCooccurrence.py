from mrjob.job import MRJob
from itertools import combinations
import csv

class DiseaseCoexistenceFrequency(MRJob):

    def mapper(self, _, line):
        reader = csv.reader([line], delimiter=';')
        row = next(reader)
        if row[0] != "PatientID":
            # Mapper la fréquence de coexistence de deux maladies
            diseases = [disease for disease in row[1:] if disease]
            for combination in combinations(diseases, 2):
                yield tuple(sorted(combination)), 1

    def reducer(self, diseases, counts):
        # Reducer pour chaque combinaison de deux maladies, somme des occurrences
        yield diseases, sum(counts)

if __name__ == '__main__':
    DiseaseCoexistenceFrequency.run()
