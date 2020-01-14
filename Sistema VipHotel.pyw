from tkinter import *
from functools import partial

class Acomodacoes:
    def __init__(self):
        self.TV = "TV Led à cabo (NET)"
        self.Metros = "13 a 18 m²"
        self.Espelho = "corpo inteiro"
        self.Internet = "Wifi 5 Mb"
        self.estacionamento = "Grátis"
class Executivo_luxo(Acomodacoes):
    def __init__(self):
        Acomodacoes.__init__(self)
        self.TV = "Tv Led 32"
        self.Internet = "Wifi 15 Mb"
        self.adicional = "R$50"
class Premium(Executivo_luxo):
    def __init__(self):
        Executivo_luxo.__init__(self)
        self.Metros = "30 m²"
        self.TV = "Smart tv 40"
        self.adicional = "Secador no Banheiro"
        self.cama = "Cama Box Queen Size"
class Master(Premium):
    def __init__(self):
        Premium.__init__(self)
        self.Metros = "47 m²"
        self.TV = "Smart Tv 40 4K"
        self.sala = "Sala de estar e sala para eventos"
        self.cama = "Duas Cama Box Queen Size"
class strings():
    def __init__(self):
        self.diaria = ["SUÍTE EXECUTIVA","SUÍTE LUXO","SUÍTE PREMIUM","SUÍTE MASTER"]
        self.precos = [164,188,214,249]
        self.precosfixo = [164,164,280]
        self.precosfixo2 = [188,188,300]
        self.precosfixo3 = [214,214,322]
        self.precosfixo4 = [249,249,327,432]
        self.tarifa = ["individual: R$164,00\nDuplo: R$164,00\nTriplo: R$280,00"]
        self.tarifa2 = ["individual: R$188,00\nDuplo: R$188,00\nTriplo: R$300,00"]
        self.tarifa3 = ["individual: R$214,00\nDuplo: R$214,00\nTriplo: R$322,00"]
        self.tarifa4 = ["individual: R$249,00\nDuplo: R$249,00\nTriplo: R$347,00\nQuádruplo: R$432,00"]
        self.regras = """
Política de pagamento: Aceitamos somente dinheiro, cartões de débito e crédito para pagamentos de diárias e extras. Não aceitamos cheques.
Cobrança bancária somente com cadastro da empresa aprovado e após a segunda hospedagem.
O hotel se reserva o direito de cobrar o valor da hospedagem antecipado.
Cartões de Crédito/Débito: Aceitamos todas as bandeiras.
Garantia de Reserva: Reservas poderão ser garantidas por meio de depósito bancário integral da(s) diária(s), feito com 05 dias de antecedência da
data do check-in ou fornecendo os dados do cartão de crédito. Depósitos bancários deverão ter a cópia do comprovante enviada por e-mail.
O Hotel se reserva o direito de exigir garantia de hospedagem.
Política de Cancelamento de Reservas: Cancelamento em até 3 dias antes da data do check-in. O valor pago será restituído, menos taxas. Cancelamento
no período menor que 3 dias antes da data do check-in, não haverá devolução do valor pago, nem concedido qualquer tipo de crédito para hospedagem
posterior. A mesma política é aplicada para pagamento com cartão de crédito.
Check-In: 13h Check-Out: 12h.
Política de Animais: Não são permitidos nos apartamentos e nas demais dependências do hotel. Consulte-nos sobre locais em nossa cidade para acomodá-los.
Política de Criança: Uma criança, até cinco anos de idade, é cortesia no mesmo apartamento dos pais.
É proibido fumar dentro dos apartamentos, banheiros, restaurante e outras áreas internas, devendo o hóspede utilizar área externa para tal.
Caso houver identificação de cheiro de cigarro no apartamento, será cobrado multa no valor integral de uma diária, referente manutenção e higienização do apartamento.
"""

#class menu(strings):
class menu():
    def __init__(self):
        self.idade = 0
        self.sacou = False
        self.texto01 = ""
        nomeb = ["Cadastrar","Tarifário","Regras"]
        func = [self.run,self.run2,self.run3]
        logo = r"viphotel-logo.png"
        self.button(nomeb,self.texto01,func)
        self.label = Label( root, text=strings().regras,font=("", 9))
        self.labelimg = Label( root)
        self.img = PhotoImage(file=logo)
        self.show = False
        self.nome = Label(root, text="Nome:",fg="#B14B88",width=15,font=("Courier", 9))
        self.nomepass = Entry(root,width=85,font=("Courier", 9))
        self.email = Label(root, text="Email:",fg="#B14B88",width=15,font=("Courier", 9))
        self.emailpass = Entry(root,width=85,font=("Courier", 9))

        self.ddd = Label(root, text="Celular",fg="#B14B88",width=15,font=("Courier", 9))
        self.dddpass = Entry(root,width=15,font=("Courier", 9))
        
        self.adutos = Label(root, text="Adutos:",fg="#B14B88",width=8,font=("Courier", 9))
        self.adultospass = Entry(root,width=23,font=("Courier", 9))
        self.criancas = Label(root, text="Crianças:",fg="#B14B88",width=15,font=("Courier", 9))
        self.criancaspass = Entry(root,width=13,font=("Courier", 9))
        
        self.chechin = Label(root, text="Check-in:",fg="#B14B88",width=15,font=("Courier", 9))
        self.chechinpass = Entry(root,width=30,font=("Courier", 9))
        self.chechout = Label(root, text="Check-out:",fg="#B14B88",width=15,font=("Courier", 9))
        self.chechoutpass = Entry(root,width=30,font=("Courier", 9))

        self.nomeC = Label(root,bg="#343434", text="Nome:",fg="#B14B88",width=5,font=("Courier bold", 20))
        self.nomeCpass = Entry(root,width=35,font=("Courier", 20))
        #self.senhaC = Label(root, text="Senha:",fg="#B14B88",width=15,font=("Courier", 9))

        self.salv = self.button(["Salvar"],"Cadastrar",[self.salvar],400,400,25)
        self.agendar = Button(root, text="Planos", fg="#eeeeee",bg="#343434", activebackground="#454545",font=('', 32), border = "0",compound="center",command=self.agendar2)
        
        self.Carregar = Button(root, text="Carregar", fg="#eeeeee",bg="#343434", activebackground="#454545",font=('', 20), border = "0",compound="center",command=self.carregarc)

        self.exclusao = Button(root, text="Excluir", fg="#eeeeee",bg="#343434", activebackground="#454545",font=('', 20), border = "0",compound="center",command=self.excluir)

        self.calc2 = Button(root, text="Calcular", fg="#eeeeee",bg="#343434", activebackground="#454545",font=('', 30), border = "0",compound="center",command=self.calcular)

        self.salvartarifa = Button(root, text="Salvar", fg="#eeeeee",bg="#343434", activebackground="#454545",font=('', 30), border = "0",compound="center",command=self.salvarca)
        #self.CarregarCod = Entry(root,width=35,font=("Courier", 10))
        #self.agendar = self.button(["Agendar"],"Salvar",[self.agendar2],399,399)
        self.carregarVazio = Label(root, text="Para Carregar dados do cliente, deve-se informar o nome do cliente no campo nome.",fg="#44ee44",width=80,font=("Courier", 10))

        self.tarifario = Label(root,fg="#44ee44",width=18,font=("Courier bold", 15))
        self.tarifario2 = Label(root,fg="#44ee44",width=18,font=("Courier bold", 15))
        self.tarifario3 = Label(root,fg="#44ee44",width=18,font=("Courier bold", 15))
        self.tarifario4 = Label(root,fg="#44ee44",width=18,font=("Courier bold", 15))

        self.v = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()
        self.v4 = IntVar()
        self.RR = Checkbutton(root,bg="#343434",fg="#B14B88", text=strings().diaria[0], variable=self.v, onvalue=1,offvalue = 0)
        self.RR2 = Checkbutton(root,bg="#343434",fg="#B14B88", text=strings().diaria[1], variable=self.v2, onvalue=2,offvalue = 0)
        self.RR3 = Checkbutton(root,bg="#343434",fg="#B14B88", text=strings().diaria[2], variable=self.v3, onvalue=3,offvalue = 0)
        self.RR4 = Checkbutton(root,bg="#343434",fg="#B14B88", text=strings().diaria[3], variable=self.v4, onvalue=4,offvalue = 0)
        
        self.dados = []
        self.ssalve = False
        self.ulti = False
        self.clienteEncontrado = False
        self.jaatribu = False
        self.calculoadultos = 0
        self.calculocriancas = 0

        self.adultoquantidade = 1
        self.criancasquantidade = 1
        
        self.ENTRES = [self.nomepass,
        self.emailpass,self.dddpass,
        self.adultospass,self.criancaspass,
        self.chechinpass,self.chechoutpass]
    def salvarca(self):
        #for i in range(2,5):
        #print(self.v.get())
        self.calcular()
        dado = self.nomeCpass.get()
        
        if self.v.get() == 1:
            dadoo = dado+"\n"+strings().diaria[0]
            self.RR.config(bg="#34dd34")
            self.RR2.config(bg="#fff")
            self.RR3.config(bg="#fff")
            self.RR4.config(bg="#fff")
            #self.calculoadultos = strings().precos[0]*int(self.adultoquantidade)
        elif self.v2.get() == 2:
            dadoo = dado+"\n"+strings().diaria[1]
            self.RR2.config(bg="#34dd34")
            self.RR.config(bg="#fff")
            self.RR3.config(bg="#fff")
            self.RR4.config(bg="#fff")
            #self.calculoadultos = strings().precos[1]*int(self.adultoquantidade)
        elif self.v3.get() == 3:
            dadoo = dado+"\n"+strings().diaria[2]
            self.RR3.config(bg="#34dd34")
            self.RR.config(bg="#fff")
            self.RR2.config(bg="#fff")
            self.RR4.config(bg="#fff")
            #self.calculoadultos = strings().precos[2]*int(self.adultoquantidade)
        elif self.v4.get() == 4:
            dadoo = dado+"\n"+strings().diaria[3]
            self.RR.config(bg="#fff")
            self.RR2.config(bg="#fff")
            self.RR3.config(bg="#fff")
            self.RR4.config(bg="#34dd34")
            #print(self.calculoadultos)
            #self.calculoadultos = strings().precos[3]*int(self.adultoquantidade)
            #print("valor multiplicado "+str(strings().precos[3]))
            #print("qauntidade de adultos "+str(self.adultoquantidade))
        else:
            dadoo = ""
        #print(dadoo)
        #print("-"*30)
        
        #print("valor pelas criancas == {}".format(self.calculocriancas))
        #print("valor pelos adultos == {}".format(self.calculoadultos))
        dadoo = ("\n{}\n{}\n{}\n{}\n{}\n".format(dadoo,self.criancasquantidade,self.calculocriancas,self.criancasquantidade,self.calculoadultos))
        if dadoo != "":
            #print("-"*30)
            #print(dadoo)
            #print("-"*30)
            with open("Agenda.txt","a") as yk:
                #yk.write(("- "*5)+"\n"+dadoo+"\n")
                yk.write(("- "*5)+dadoo)
        else:
            print("nenhum plano selecionado")


            
    def calcular(self):
        self.jaatribu = False
        nome = self.nomeCpass.get()
        with open("dados_cliente.txt","r") as kk:
            dados = kk.readlines()
        for i in range(0,len(dados)):
            if dados[i] == nome+"\n":
                #print("Adultos = {} e criancas = {}".format(dados[i+3],dados[i+4]))

                #verificar essas variaveis pois vao modificar o label do calculo
                #self.adultoquantidade = dados[i+3].replace("\n","")
                #self.criancasquantidade = dados[i+4].replace("\n","")
                if self.jaatribu == False:
                    self.adultoquantidade = dados[i+3].replace("\n","")
                    if self.v.get() == 1:
                        print("o valor foi atribuido")
                        print(self.calculoadultos)
                        if int(self.adultoquantidade) > 3:
                            self.calculoadultos = strings().precos[0]*int(self.adultoquantidade)
                        elif int(self.adultoquantidade) == 3:
                            self.calculoadultos = strings().precosfixo[2]
                        elif int(self.adultoquantidade) == 2:
                            self.calculoadultos = strings().precosfixo[1]
                        elif int(self.adultoquantidade) == 1:
                            self.calculoadultos = strings().precosfixo[0]
                        print(self.calculoadultos)
                        self.RR.config(bg="#34dd34")
                        self.RR2.config(bg="#fff")
                        self.RR3.config(bg="#fff")
                        self.RR4.config(bg="#fff")
                    elif self.v2.get() == 2:
                        print("2")
                        #self.calculoadultos = strings().precos[1]*int(self.adultoquantidade)
                        if int(self.adultoquantidade) > 3:
                            self.calculoadultos = strings().precos[1]*int(self.adultoquantidade)
                        elif int(self.adultoquantidade) == 3:
                            self.calculoadultos = strings().precosfixo2[2]
                        elif int(self.adultoquantidade) == 2:
                            self.calculoadultos = strings().precosfixo2[1]
                        elif int(self.adultoquantidade) == 1:
                            self.calculoadultos = strings().precosfixo2[0]
                        self.RR2.config(bg="#34dd34")
                        self.RR.config(bg="#fff")
                        self.RR3.config(bg="#fff")
                        self.RR4.config(bg="#fff")
                    elif self.v3.get() == 3:
                        print("3")
                        #self.calculoadultos = strings().precos[2]*int(self.adultoquantidade)
                        if int(self.adultoquantidade) > 3:
                            self.calculoadultos = strings().precos[2]*int(self.adultoquantidade)
                        elif int(self.adultoquantidade) == 3:
                            self.calculoadultos = strings().precosfixo3[2]
                        elif int(self.adultoquantidade) == 2:
                            self.calculoadultos = strings().precosfixo3[1]
                        elif int(self.adultoquantidade) == 1:
                            self.calculoadultos = strings().precosfixo3[0]
                        self.RR3.config(bg="#34dd34")
                        self.RR.config(bg="#fff")
                        self.RR2.config(bg="#fff")
                        self.RR4.config(bg="#fff")
                    elif self.v4.get() == 4:
                        print("4")
                        #self.calculoadultos = strings().precos[3]*int(self.adultoquantidade)
                        if int(self.adultoquantidade) > 4:
                            self.calculoadultos = strings().precos[3]*int(self.adultoquantidade)
                        elif int(self.adultoquantidade) == 4:
                            self.calculoadultos = strings().precosfixo4[3]
                        elif int(self.adultoquantidade) == 3:
                            self.calculoadultos = strings().precosfixo4[2]
                        elif int(self.adultoquantidade) == 2:
                            self.calculoadultos = strings().precosfixo4[1]
                        elif int(self.adultoquantidade) == 1:
                            self.calculoadultos = strings().precosfixo4[0]
                        self.RR.config(bg="#fff")
                        self.RR2.config(bg="#fff")
                        self.RR3.config(bg="#fff")
                        self.RR4.config(bg="#34dd34")
                    else:
                        print(self.v.get())
                        
                    #self.adultoquantidade = dados[i+3].replace("\n","")
                    self.criancasquantidade = dados[i+4].replace("\n","")
                    self.jaatribu = True
                self.calculocriancas = int(dados[i+4])*60
                #print("valor pelas criancas == {}".format(self.calculocriancas))
                break
        #print("valor pelas {} criancas == {} valor pelos {} adultos == {} ".format(self.criancasquantidade,self.calculocriancas,self.adultoquantidade,self.calculoadultos))
        self.carregarVazio.config(width=70,font=("Courier", 15),bg="#343434",text="valor por {} criancas = R${},00\n valor por {} adultos = R${},00\n                TOTAL = R${},00".format(self.criancasquantidade,self.calculocriancas,self.adultoquantidade,self.calculoadultos,(self.calculocriancas+self.calculoadultos)))
        self.carregarVazio.place(x=120,y=110)
    def limpafile(self):
        with open("dados_cliente.txt","w") as bb:
                        bb.write("")
    def excluir(self):
        if self.nomepass.get() != "":
            with open("dados_cliente.txt","r") as kk:
                clie = kk.readlines()
            try:
                #print("olhar 0x99213")
                print("antes no try:")
                print(clie)
                self.limpafile()
                self.ulti = False
                for i in range(0,len(clie)):
                    #print("olhar 0x99213")
                    if clie[i] == self.nomepass.get()+"\n" and self.ulti == False:
                        self.carregarVazio.config(width=70,font=("", 15),bg="#343434",text="O Cadastro do cliente {} foi excluido".format(clie[i].strip("\n")))
                        self.carregarVazio.place(x=120,y=165)
                        for e in range(-1,7):
                            clie.pop(i)
                        self.ulti = True
                        self.limpafile()
                        #print("olhar 0x99213")
                    else:
                        #print("valor "+clie[i]+"eh diferente da entrada")
                        pass
            except:
                print("depois no except:")
                print(clie)
                self.clienteEncontrado = False
                #self.clientetagult = False
                if clie[-1] == "_____Cliente_____\n":
                    clie.pop(-1)
                with open("dados_cliente.txt","a") as ba:
                    for i in range(0,len(clie)):
                        if len(clie) != 1:
                            ba.write(clie[i])                                              
                        else:
                            print("ultimo valor foi excluido")
            self.nomepass.delete(0, END)
            self.emailpass.delete(0, END)
            self.dddpass.delete(0, END)
            self.adultospass.delete(0, END)
            self.criancaspass.delete(0, END)
            self.chechinpass.delete(0, END)
            self.chechoutpass.delete(0, END)
        
    def insertcli(self,v1,v2,v3,v4,v5,v6):    
        self.emailpass.delete(0, END)
        self.emailpass.insert(END,v1.replace("\n",""))
        self.dddpass.delete(0, END)
        self.dddpass.insert(END,v2.replace("\n",""))
        self.adultospass.delete(0, END)
        self.adultospass.insert(END,v3.replace("\n",""))
        self.criancaspass.delete(0, END)
        self.criancaspass.insert(END,v4.replace("\n",""))
        self.chechinpass.delete(0, END)
        self.chechinpass.insert(END,v5.replace("\n",""))
        self.chechoutpass.delete(0, END)
        self.chechoutpass.insert(END,v6.replace("\n",""))
        
    def carregarc(self):
        self.clienteEncontrado = False
        if self.nomepass.get() != "":
            with open("dados_cliente.txt","r") as kk:
                cli = kk.readlines()
            if len(cli) == 0:
                    self.carregarVazio.config(bg="#343434",text="Cadastro não encontrado!!")
                    self.carregarVazio.place(x=200,y=170)
            for i in range(0,len(cli)):
                if cli[i] == self.nomepass.get()+"\n" and self.clienteEncontrado == False:
                    self.insertcli(cli[i+1],cli[i+2],cli[i+3],cli[i+4],cli[i+5],cli[i+6])
                    self.clienteEncontrado = True
                    self.carregarVazio.place_forget()
                    break
                    
                elif i == len(cli)-1 and self.clienteEncontrado == False :
                    self.carregarVazio.config(bg="#343434",text="cadastro não encontrado")
                    self.carregarVazio.place(x=200,y=170)
                else:
                    pass
        else:
            self.carregarVazio.config(bg="#343434")
            self.carregarVazio.place(x=200,y=170)
    def isshow(self):
        self.show = True
    def tosalve(self):
        self.ssalve = True
    def agendar2(self):
        try:
            with open("dados_cliente.txt","r") as kk:
                dados = kk.readlines()
        except:
            print("arquivos com os clientes não encontrado!!")
        if self.nomeCpass.get() != "" and self.nomeCpass.get()+"\n" in dados :
            self.carregarVazio.place_forget()
            self.nomeCpass.config(bg="#fff")
            print("Calculando...")
            self.tarifario2.config(fg="#33aaaa",text=strings().diaria[1]+"\n"+strings().tarifa2[0],bg="#343434")
            self.tarifario2.place(x=370,y=270)
            self.tarifario3.config(fg="#33aaaa",text=strings().diaria[2]+"\n"+strings().tarifa3[0],bg="#343434")
            self.tarifario3.place(x=570,y=270)
            self.tarifario4.config(fg="#33aaaa",text=strings().diaria[3]+"\n"+strings().tarifa4[0],bg="#343434")
            self.tarifario4.place(x=770,y=270)
            self.tarifario.config(fg="#33aaaa",text=strings().diaria[0]+"\n"+strings().tarifa[0],bg="#343434")
            self.tarifario.place(x=170,y=270)
            self.calc2.place(x=200,y=400)
            self.salvartarifa.place(x=700,y=400)
            self.RR.place(x=200,y=245)
            self.RR2.place(x=420,y=245)
            self.RR3.place(x=600,y=245)
            self.RR4.place(x=800,y=245)

        elif self.nomeCpass.get()+"\n" not in dados and self.nomeCpass.get() != "":
            self.carregarVazio.config(bg="#343434",text="cliente não cadastrado!!!")
            self.carregarVazio.place(x=200,y=170)
        else:
            self.nomeCpass.config(bg="#dd3333")
            self.carregarVazio.config(bg="#343434",text="o campo não pode ser vazio!!")
            self.carregarVazio.place(x=180,y=170)
    def salvar(self,n,local="dados_cliente.txt"):
        ad = []
        for i in self.ENTRES:
            if i.get() != "":
                i.config(bg="#fff")
                ad.append(i.get()+"\n")
            else:
                i.config(bg="#dd3333")
        if len(ad) == 7:
            self.carregarVazio.config(bg="#343434",text="Cadastro Salvo com sucesso!!",font=("",15))
            self.carregarVazio.place(x=120,y=165)
            with open(local,"a") as dd:
                dd.write(("_"*5)+"Cliente"+("_"*5)+"\n")
            for i in self.ENTRES:
                with open(local,"a") as dd:
                    dd.write(i.get()+"\n")
        else:
            print(len(ad))
        
    def dell(self):
            self.label.place_forget()
            self.labelimg.place_forget()
            self.nome.place_forget()
            self.nomepass.place_forget()
            self.email.place_forget()
            self.emailpass.place_forget()
            self.ddd.place_forget()
            self.dddpass.place_forget()
            self.adutos.place_forget()
            self.adultospass.place_forget()
            self.criancas.place_forget()
            self.criancaspass.place_forget()
            self.chechin.place_forget()
            self.chechinpass.place_forget()
            self.chechout.place_forget()
            self.chechoutpass.place_forget()
            self.nomeC.place_forget()
            self.nomeCpass.place_forget()
            self.carregarVazio.place_forget()
            self.tarifario.place_forget()
            self.tarifario2.place_forget()
            self.tarifario3.place_forget()
            self.tarifario4.place_forget()
            self.RR.place_forget()
            self.RR2.place_forget()
            self.RR3.place_forget()
            self.RR4.place_forget()
            self.salvartarifa.place_forget()
            self.calc2.place_forget()
            self.buttonn[n].place_forget() 
            
    def limpa(self,n):
        try:
            self.dell()
        except:
            self.buttonn[0].place_forget()
            self.agendar.place_forget()
            self.Carregar.place_forget()
            self.exclusao.place_forget()
            
    def showhide(self,n,g=1):
        #funcao responsavel por decidir se os elementos da tela devem ou nao ser exibidos.
        if self.show == False and g == 1:
            self.label.place(x=40,y=200)
            self.isshow()
            
        elif self.show == True and g == 1:
            self.show = False
            print(n)
            self.buttonn[n-2].config(bg="#343434")
            self.limpa(n)
        elif g == 2 and self.show == False:
            self.labelimg.place(x=0,y=200)
            self.nome.place(x=200,y=200)
            self.nomepass.place(x=320,y=200)
            self.email.place(x=200,y=230)
            self.emailpass.place(x=320,y=230)
            self.ddd.place(x=200,y=260)
            self.dddpass.place(x=320,y=260)
            self.adutos.place(x=450 ,y=260)
            self.adultospass.place(x=520 ,y=260)
            self.criancas.place(x=700,y=260)
            self.criancaspass.place(x=820 ,y=260)
            self.exclusao.place(x=790,y=385)
            self.Carregar.place(x=200,y=390)
            
            self.chechin.place(x=200,y=290)
            self.chechinpass.place(x=320,y=290)
            self.chechout.place(x=560,y=290)
            self.chechoutpass.place(x=700,y=290)
            self.buttonn[-1].place(x=500,y=385)
            self.isshow()
        elif g == 3 and self.show == False:
            self.labelimg.place(x=0,y=200)
            self.nomeC.place(x=200,y=200)
            self.nomeCpass.place(x=300,y=200)
            self.isshow()
        elif g != 1 and self.show == True:
            self.show = False
            self.limpa(n)
        else:
            print("não faz nada")

    def run(self,n):
        ##Botao de cadastro de cliente
        ##Aqui apenas deve-se configurar os objetos da tela
        ##a funcao showhide esta responsavel por mostrar ou nao os objetos
        self.labelimg.config(image=self.img)
        self.chechinpass.delete(0, END)
        self.dddpass.delete(0, END)
        self.chechoutpass.delete(0, END)
        self.chechinpass.insert(END,"dd/mm/aaaa")
        self.chechoutpass.insert(END,"dd/mm/aaaa")
        self.dddpass.insert(END,"(44)0000-0000")
        self.showhide(n,2)
    def run2(self,f):
        ##Botao de Check-in
        self.labelimg.config(image=self.img)
        self.agendar.place(x=450,y=400)
        self.showhide(f,3)
    def run3(self,f):
        #botao 3 
        self.label.config(bg="#dddddd",text=strings().regras)
        self.showhide(f)

    #Funcao responsavel por criar botao em loop e passar o texto e funcao a executar
    def button(self,textoBotao,info,funcao,vv=100,ww=0,sal=32):
        self.x = vv
        self.y = ww
        self.buttonn = []
        for i in range(0,len(textoBotao)):
            self.buttonn.append(Button(root, text=textoBotao[i],
                           fg="#eeeeee",bg="#343434",
                           activebackground="#454545",
                           font=('', sal), border = "0",
                           compound="center",command=partial(funcao[i],i)))
            if ww == 0:
                self.buttonn[-1].place(x=self.x,y=self.y )
            elif ww == 399:
                self.run2(i)
            else:
                pass
            self.x += 300
        

root = Tk()
root.title("Vip Hotel")
root.geometry("1000x600+300+300")
root.wm_attributes('-topmost','true')
#root.tk_focusFollowsMouse()
root.config(bg="#343434")

mein = menu()
root.mainloop()
