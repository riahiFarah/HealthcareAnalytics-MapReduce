from mrjob.job import MRJob
import csv

class DiseaseFrequency(MRJob):

    def mapper(self, _, line):
        reader = csv.reader([line], delimiter=';')
        row = next(reader)
        if row[0] != "PatientID":
            # Mapper la fréquence de chaque maladie
            for disease in row[1:]:
                if disease:
                    yield disease, 1

    def reducer(self, disease, counts):
        # Reducer pour chaque maladie, somme des occurrences
        yield disease, sum(counts)

if __name__ == '__main__':
    DiseaseFrequency.run()
