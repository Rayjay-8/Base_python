import labelfacil

texto01 = "botao usado para abrir arquivos que foram marcados como legiveis."

nomeb = ["open", "Login","Senha","exit","open", "Login","Senha","exit"]

#funcoes
def run():
    print("Rodando funcao run1!!!")
def run2():
    print("Rodando funcao run2!!!")
def run3():
    print("Rodando funcao run3!!!")
def run4():
    print("Rodando funcao run4!!!")
    #quit()
#insere as funcoes em uma lista    
func = [run,run2,run3,run4,run,run2,run3,run4]

labelfacil.button(nomeb,texto01,func)

