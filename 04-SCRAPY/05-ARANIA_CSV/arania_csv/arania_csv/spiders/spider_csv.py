import scrapy
from scrapy.spiders import CSVFeedSpider

class VinosBlancosArania(CSVFeedSpider):
    name = 'vinos'
    
    urls = [
        "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"
    ]
    
    delimiter = ';'
    quotechar = '"'
    
    headers = [
    'chlorides',
    'free sulfur dioxide',
    'total sulfur dioxide',
    'density',
    'pH',
    'sulphates',
    'alcohol',
    'fixed density',
    'volatile acidity',
    'citric acid',
    'residual sugar',
    'quality'
    ]
    
    def parse(self, response, row):
        print(type(row))
        with open('vinos.txt', 'a+', encoding= 'utf-8') as archivo:
            archivo.write('Densidad:' + row['fixed density'] + 'Alcohol:' + row['alcohol'] + '\n')        