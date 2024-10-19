import csv
class GetData():
    def __init__(self,name:str):
        self.name = name 
    def get(self):
        with open(self.name, newline='') as csvfile:
            sours = csv.reader(csvfile, delimiter=' ', quotechar='|')

            return [el[0].split(',') for i,el in enumerate(sours) if i != 0]

                