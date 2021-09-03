import json


class AASequence():
    def __init__(self, AAsequence: str): #Paramter AASequence for a string of 
        self.AAsequence = AAsequence


    
    def NitrogenCount(self):
        '''
        A function that, when called, will scan over a string and using values in AminoAcids.json will return the total # of Nitrogens
        in the entire sequence.
        '''
        NCount = 0
        with open('AminoAcids.json') as json_file:
            data = json.load(json_file)
        for i in self.AAsequence:
            for key in data: #Iterates over every amino acid in AminoAcids.json
                if i == key in data: #Iterates over each value in a submitted sequence 
                    NCount = NCount + data[key][2]
                else:
                    pass
        return(NCount)

    def PFromRNA(self):
        '''
        Takes an RNA Sequence and returns the Phosphorus count.
        '''

seq = input("Enter your sequence. (Check README for example of a valid sequence).")
Nitrogen = AASequence(seq).NitrogenCount()
print("There are " + str(Nitrogen) + " Nitrogens in your sequence.")
input("")
