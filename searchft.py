from googlesearch import search

class Searchft:
    def __init__(self):
        item = None
        link = None
    
    def buscar(item, size = 10):
        resultado = []
        for url in search(item, size):
            print(url)
            resultado.append(url)
        
        return resultado
    
    def visitarLink(self, link):
        
        pass
    



