import requests, bs4

res = requests.get('httos://books.toscrape.com/')

soup = bs4.BeautifulSoup(res.text, "html.parser")
type(soup)

soup.title.string #carregar o titulo da pagina

titulos_livros = [] #lista para amarzenar os titulos dos livros 

# itera sobre cada livros encontrado
for livro in soup.select('.product_pod'):
    h3 = livro.find('h3')
    # vericando se o h3 nao possui atributos "class"
    titulo = h3.a["title"]
    titulos_livros.append(titulo)

    print(soup.title.string) #carrega o titulo da pagina
    print(titulos_livros) #exibe todos os titulos dos livros