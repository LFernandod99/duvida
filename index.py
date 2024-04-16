import pandas as pd
def questions():
    df = pd.DataFrame() # Criando um DataFrame vazio
    while True:
        idade = int(input('Digite sua idade (ou 0 para sair): '))
        
        if idade == 0:
            df.to_csv('levantamento.csv', index=False)
            print("Dados salvos com sucesso em 'levantamento.csv'.")
            break
            
        elif idade > 0:
            genero = input('Qual seu gênero? ').lower()
            nova_linha = {'Idade': idade, 'Gênero': genero}
            df = df._append(nova_linha, ignore_index=True)
                

questions()


