import json
import csv
import re
from mrjob.job import MRJob
from mrjob.step import MRStep
from pymongo import MongoClient


def tidy_fuerte(line):
    devuelve=[]
    try:
        idioma=line['lang'] == 'en'
    except:
        idioma = None
    if idioma is not None:
        try:
            place = line['place']
        except:
            place = None
        if place is not None:
            code = place['country_code']
            if code == "US":
                location = place['full_name']
                s = []
                s = location.split(",")

                if s[0] in provincias:
                    provincia = provincias[s[0]]
                    tweet = line['text']
                    devuelve.append([provincia, tweet])
                    return devuelve
                else:
                    return None

def value2(line):

    tweet = line.strip().lower()
    for word in tweet.split():
        if word in diccionario:
            final=0
            final += diccionario[word]
    return final



def hastag(line):

    ht1 = line['entities']['hashtags']
    try:
        idioma=line['lang'] == 'en'
    except:
        idioma = None
    if idioma is not None:
        try:
            place = line['place']
        except:
            place = None
        if place is not None:
            code = place['country_code']
            if code == "US":
                location = place['full_name']
                s = []
                s = location.split(",")

                if s[0] in provincias:
                    for i in ht1:
                        ht = i['text']
                        return ht
                else:
                    return None



class MRtw(MRJob):


    def steps(self):
        return [MRStep(mapper=self.mapper,
                       reducer=self.reducer),
                MRStep(reducer=self.reducer_top)
                ]

    def mapper(self, _, line):
        try:
            data = json.loads(line)
            origen2 = hastag(data)
            origen = tidy_fuerte(data)
            if origen is not None:
                for i in origen:
                    valor = value2(i[1])
                    yield (i[0], valor)
            if origen2 is not None:
                has = '#' + origen2
                yield (has, 1)
        except:
            pass


    def reducer(self, key, value):
        mat2 = re.match(r"^(#)", key)
        if  mat2 != None:
            pair1=[sum(value),key]
            yield ('has', pair1)
        else:
            total = 0
            suma = 0
            for v in value:
                total += 1
                suma += v
                mean=(float(suma) / total)
                pair4=[mean,total]

            yield ('estado', (mean, key))
            yield (key, pair4)



    def reducer_top(self, dif, pair):
        client = MongoClient('db', 27017)
        db = client.tw

        if dif == 'has':
            g = list(pair)
            top3=[]
            for hast in g:
                top3.append(hast)
                top3.sort()
                top3=top3[-10:]
            for hast in top3:
                item = {
                        'hastag':hast[1],
                        'valor':hast[0]
                       }
                insertar=db.tw.insert_one(item)
                yield (hast)
                

             

        elif dif == 'estado':
            yield ('maximo', max(pair))
            g7=list(pair)
            for num3 in g7:
                item = {
                       'localizacion':num3[1],
                       'valor':num3[0]
                        }
                insertar=db.tw.insert_one(item)
                
     
        else:
            g3 = list(pair)
            for num2 in g3:
                yield (num2, dif)
                
############# MAIN CLASS ##############
if __name__ == '__main__':

     diccionario = {}
     with open('AFINN-111.txt', 'r') as tx:
         readertx = csv.reader(tx, delimiter='\t')
         for row in readertx:
             diccionario.setdefault(row[0], int(row[1]))

     provincias = {}
     txt = open('States-Usa.txt', 'r')
     for line in txt:
         line = line.strip('\n')
         line = line.strip('\r')
         keyValue2 = line.split(',')
         provincias[keyValue2[0]] = (keyValue2[(1)])


     MRtw.run()
