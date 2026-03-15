import sys
import time
import os
os.system('cls' if os.name == 'nt' else 'clear') #<-- LIMPA A TELA ANTES DE COMEÇAR O KARAOKÊ
#CORES
vermelho   = "\033[31m"    # 🔴 Vermelho
vermelho_negrito = "\033[1;31m"  # Vermelho Negrito
branco     = "\033[37m"    # ⚪ Branco
branco_negrito = "\033[1;37m"  # Branco Negrito  
azul       = "\033[34m"    # 🔵 Azul
azul_negrito    = "\033[1;34m"   # Azul Negrito
verde      = "\033[32m"    # 🟢 Verde
verde_negrito       = "\033[1;32m"   # Verde Negrito
amarelo    = "\033[33m"    # 🟡 Amarelo
amarelo_negrito = "\033[1;33m"   # Amarelo Negrito
roxo       = "\033[35m"    # 🟣 Roxo
roxo_negrito        = "\033[1;35m"   # Roxo Negrito
ciano      = "\033[36m"    # 🟦 Ciano
laranja    = "\033[38;5;208m" # 🧡 Laranja
reset      = "\033[0m"     # ❌ Reset

#CORES DAS PALAVRAS
palavras_verde = [
    "limão",
    "limoeiro",
]
palavras_roxas  = [
    "jacarandá",
]

#FUNÇÕES
def digitar(texto, velocidade=0.080): #<-- VELOCIDADE DE DIGITAÇÃO
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)

def colorir(texto): #<-- COR DAS PALAVRAS
    for palavra in palavras_verde:
        texto = texto.replace(palavra, verde + palavra + reset)
    for palavra in palavras_roxas:
        texto = texto.replace(palavra, roxo + palavra + reset)
    return texto

#MÚSICA
digitar(branco + "Meu Limão, Meu Limoeiro\n" + reset) #<-- NOME DA MÚSICA
digitar(branco + "Wilson Simonal\n\n" + reset) #<-- ARTISTAS

time.sleep(0.5) #<-- TEMPO DE ESPERA ANTES DE COMEÇAR A MÚSICA

musica = [ #<-- LETRA DA MÚSICA
    "Meu limão, meu limoeiro",
    "Meu pé, meu pé de jacarandá",
    "Uma vez esquindolêlê, iê iê",
    "Outra vez esquindolálá",
    "", #<-- SEPARAÇÃO DOS TRECHOS
    "Meu limão, meu limoeiro",
    "Meu pé, meu pé de jacarandá",
    "Uma vez esquindolêlê, iê iê",
    "Outra vez esquindolálá"
]

for trecho in musica: #<-- PARA CADA TRECHO DA MÚSICA, ELE VAI DIGITAR E COLORIR AS PALAVRAS
    digitar(colorir(trecho))
    input() #<-- ESPERA O USUÁRIO PRESSIONAR ENTER PARA CONTINUAR PARA O PRÓXIMO TRECHO