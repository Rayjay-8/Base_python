
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
        print("Em uma velocidade de 500 senhas testadas por segundos levaria um total de :")
        segu = total/500
        minu = segu/60
        segu = segu%60
        hora = minu/60
        dia = hora/24
        ano = dia/365
        if (minu <= 59):
            print("%i minutos %i segundos" % (minu, segu))
        elif (minu > 59 and hora <24):
            minu = minu%60
            print("%i horas %i minutos %i segundos"% (hora, minu, segu))
        elif (hora >= 24 and dia<365):
            minu = minu%60
            hora = hora%24
            print("%i dia %i horas %i minutos %i segundos"% (dia, hora, minu, segu))
        elif (dia >= 365):
            minu = minu%60
            hora = hora%24
            dia = dia%365
            print("%i anos %i dias %i horas %i minutos %i segundos"% (ano, dia, hora, minu, segu))
        
    calculoDoTempo()
calcula()
input()
