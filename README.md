# Descrição
A SearchForThis é uma biblioteca que efetua pesquisas em motores de busca na web.

# Funcionalidade
* Realizar buscas por conteúdos desejados

# Biblioteca
### Instalação
```python
pip install searchft
```

### Importar
```python
import Searchft
```

### Uso
Faca uma instância da classe, dessa forma:
```python
search = Searchft()
```
Assim você poderá acessar os metodos da classe. Não é preciso nenhum argumento na hora de instanciar a classe.

### Realizando buscas:
Use o metodo buscar da classe, da seguinte forma:
```python
resultado = search.buscar('conteúdo da busca', size)
```
A variável size, armazena a quantidade de links que você deseja bucsar

