with open('artigos.txt', 'r') as database:
  corpus = database.read()

palavras_separadas = nltk.tokenize.word_tokenize(corpus)

import nltk
nltk.download('punkt')

def separa_palavras(tokens):
  lista_palavras = []
  for token in tokens:
    if token.isalpha():
      lista_palavras.append(token)
  return lista_palavras

def get_palavras(palavras_separadas):
  for palavra in palavras_separadas:
    print(palavra)


def normalizacao(tokens):
  tokens = [token.lower() for token in tokens]
  return tokens

palavras_separadas = separa_palavras(palavras_separadas)
palavras_separadas = normalizacao(palavras_separadas)

def gerador_de_palavras(palavra):
  fatias = []
  for i in range(len(palavra) + 1):
    fatias.append((palavra[:i],palavra[i:] ))
  palavras_geradas = insere_letras(fatias)
  print(palavras_geradas)

gerador_de_palavras("golng")

def insere_letras(fatias):
  novas_palavras = []
  letras = "abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç"
  for E, D in fatias:
    for letra in letras:
      if E + letra + D in palavras_separadas:
        novas_palavras.append(E + letra + D)
  return novas_palavras

def corretor(palavras_separadas):
  palavras_separadas = separa_palavras(palavras_separadas)
  palavras_separadas = normalizacao(palavras_separadas)
  gerador_de_palavras("golng")

frequencia = nltk.FreqDist(palavras_separadas)
frequencia.most_common(10)