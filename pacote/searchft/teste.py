import searchft

from searchft import Searchft

resultados = Searchft.buscar('lofi', 5)

print(resultados)

Searchft.visitarLink(resultados[1])
