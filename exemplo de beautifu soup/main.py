import bs4

examplefile = open("index3.html")
examplesoup = bs4.BeautifulSoup(examplefile.read(), "html, parser")

elems = examplesoup.select('#author') #identificador author
sl = examplesoup.select('.slogan') #classe slogan


print(elems[0]) #imprimir o valor da id author 
print(sl)  #imprimir o valor da classe slogann 