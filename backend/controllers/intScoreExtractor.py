import os
import json

from backend.controllers.fileConverter import fileConverter
from backend.controllers.fileIndexer import fileIndexer
from backend.entities import country as c


class intScoreExtractor(fileIndexer):
    def __init__(self):
        fileIndexer.__init__(self, in_fn=in_fn, out_fld=out_fld)
        self.outFile(file_type=".json")
        self.c_list = []
        self.coun = []
        self.nationalIntScore = []
        #self.jsonRead()

    def jsonRead(self):
        with open(self.in_fn, 'r', encoding='utf8') as f:
            self.data = json.load(f)
            self.countries_data = self.data['countries']
            for i in self.data['countries']:
                self.c_list.append(i)

            for i in range(len(self.c_list)):
                self.coun.append(c.country(self.c_list[i], self.countries_data[self.c_list[i]]))

            for i in range(len(self.c_list)):
                if self.coun[i].check_intScore() != None and self.coun[i].check_intScore() > 0:
                    dictionary = {"tag": self.coun[i].tag,
                                  "score": self.coun[i].check_intScore()
                                  }
                    self.nationalIntScore.append(dictionary)

    def jsonDump(self):
        with open(self.out_fn, 'w') as f:
            json.dump(self.nationalIntScore, f, indent=1)

    def playerDump(self):
        for i in range(len(self.nationalIntScore)):
            print(f'Nazione: {self.nationalIntScore[i]["tag"]}, IntScore: {self.nationalIntScore[i]["score"]}')

if __name__ == "__main__":
    out_fld = 'C:/Users/diego/PycharmProjects/intscore/backend/saves/extendedJson'
    in_fn = 'C:/Users/diego/PycharmProjects/intscore/backend/saves/mp_Siam1551_01_01.json'
    #f = intScoreExtractor(in_fn, out_fld)
    f = intScoreExtractor()
    f.jsonRead()
    f.jsonDump()
    f.playerDump()

