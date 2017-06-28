#coding: utf-8

from Aluno import aluno

class equipe:

    def all(self):

        self.listaAlunos = []

        while True:
            print ("\nbem vindo")
            print "Cadastrar Aluno: 1"
            print "Remover Aluno: 2"
            print "imprimir Aluno: 3"

            op = int(raw_input("\nOpcao: "))

            if op == 1:
                nome = raw_input("Informe o Nome do Aluno: ")
                cpf1 = raw_input("Informe o CPF: ")

                alun = aluno(nome,cpf1,self.listaAlunos)


                existe = False
                if len(self.listaAlunos) == 0:
                    self.listaAlunos.append(alun)
                    print ("Aluno Cadastrado")

                else:
                    for x in range(len(self.listaAlunos)):
                        if self.listaAlunos[x].getNome() == nome:
                            existe = True
                            print ("Já Cadastrado")
                    if existe == False:
                        self.listaAlunos.append(alun)
                        print ("Aluno Cadastrado")
            elif op == 2:
                nome2 = raw_input("Informe o Nome do Aluno: ")
                for x in range(len(self.listaAlunos)):
                    if self.listaAlunos[x].getNome() == nome2:
                        self.listaAlunos.remove(self.listaAlunos[x])
                        break

            elif op == 3:
                for x in range(len(self.listaAlunos)):
                    print ("\nNome: %s | Cpf: %s" %(self.listaAlunos[x].getNome(), self.listaAlunos[x].getCPF()))




escola = equipe()
escola.all()