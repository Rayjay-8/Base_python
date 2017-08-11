
#calculador de possibilidades de quebra de senha
#Password break calculator
#caracter: abcdefghijklmnopqrstuvwxyz1234567890
#caracter especiais: "!@#$%&*()_+=-'/;.>:?}^~][´`{ºª§\|
def calcula():    
    # m = numero de caracter
    #
    # n = soma de caracter + caracter expeciais 
    Hard = 86
    Medium = 62
    Easy = 36
    print ("""
    levando como base os niveis de complexidade da senha:
        Fraco : caracteres normais + numeros sem maiusculas.
        Medio : Fraco + com maiusculas
        Forte : Medio + caracter especiais
    """)
    Nivel = input("nivel de complexidade: ")
    if (Nivel == "fraco" or Nivel == "Fraco"):
        n = Easy
    elif (Nivel == "medio" or Nivel == "Medio"):
        n = Medium
    elif (Nivel == "forte" or Nivel == "Forte"):
        n = Hard
    m = int(input("informe a quantidade de caracter usado na senha:"))
    i = 1
    total = 1
    while i <= m: 
        total = total*n
        i +=1
    print ("total de senhas a ser testadas ", total,"\n") if i > m else ("erro!!")
    
    def calculoDoTempo():
        
        pass
    calculoDoTempo()
calcula()
input()
