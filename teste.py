import pandas as pd

class questions:
    def __init__(self, df,idade, genero, nova_linha ):
         self.df = df
         self.idade = idade
         self.genero = genero
         self.nova_linha = nova_linha
    
    def pergunta(self):
            self.df = pd.DataFrame() # Criando um DataFrame vazio
            while True:
                self.idade = int(input('Digite sua idade (ou 0 para sair): '))
                if self.idade == 0:
                    self.df.to_csv('levantamento.csv', index=False)
                    print("Dados salvos com sucesso em 'levantamento.csv'.")
                    break
                elif self.idade > 0:
                    self.genero = input('Qual seu gênero? ').lower()
                    self.nova_linha = {'Idade': self.idade, 'Gênero': self.genero}
                    self.df = self.df._append(self.nova_linha, ignore_index=True)
                

questions()

