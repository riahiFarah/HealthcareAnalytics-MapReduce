from mrjob.job import MRJob
from mrjob.step import MRStep

class SymptomDiseaseMapping(MRJob):

    def mapper(self, _, line):
        data = line.strip().split(';')
        diseases = data[1:4]
        symptoms = data[4:]
        for disease in diseases:
            for symptom in symptoms:
                yield (disease, symptom), 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    SymptomDiseaseMapping.run()
