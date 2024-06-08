import pandas as pd
import matplotlib.pyplot as plt
import utils 


dados = pd.read_csv('derramamentos.csv')

# Converter a coluna 'Data' para o formato de data
dados['Data'] = pd.to_datetime(dados['Data'])

# Criar uma nova coluna para o ano
dados['Ano'] = dados['Data'].dt.year


# Menu
def menu():
    print("---------------")
    print('Menu')
    escolhaMenu =  utils.obrigarResposta("1) Frequencia de Derramamentos \n2) Total Derramado\n3) Causas dos Derramamentos\n4) Informações sobre o impacto do petróleo no meio ambiente.\n 5)Sair> ", ['1', '2', '3', '4', '5'])
    
    if(escolhaMenu == '1'):
      graficoFrequenciaDerramamentos()
    elif(escolhaMenu == '2'):
      graficoTotalDerramado()
    elif(escolhaMenu == '3'):
      graficoCausasDerramamentos()
    elif(escolhaMenu == '4'):
      utils.textoAnimado("O derramamento de petróleo é a liberação acidental ou intencional de petróleo líquido no ambiente, especialmente em áreas marítimas. Esses eventos ocorrem devido a falhas em equipamentos, erros humanos, desastres naturais ou atividades ilícitas, como furtos em oleodutos. Os impactos são devastadores, afetando a vida marinha, contaminando ecossistemas costeiros, prejudicando a pesca e o turismo, e causando danos econômicos e de saúde pública. Além disso, a poluição do petróleo pode persistir no ambiente por décadas, afetando a biodiversidade e a qualidade de vida das comunidades locais.")
      menu()
    else:
      exit()



def graficoFrequenciaDerramamentos():
    # Frequência de derramamentos por ano
    freq_por_ano = dados['Ano'].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    plt.bar(freq_por_ano.index, freq_por_ano.values)
    plt.xlabel('Ano')
    plt.ylabel('Número de Derramamentos')
    plt.title('Frequência de Derramamentos de Petróleo por Ano')
    plt.grid(True)
    plt.show()
    menu()

def graficoTotalDerramado():
    # Volume total derramado por ano
    volume_por_ano = dados.groupby('Ano')['Volume'].sum()
    plt.figure(figsize=(10, 5))
    plt.plot(volume_por_ano.index, volume_por_ano.values, marker='o')
    plt.xlabel('Ano')
    plt.ylabel('Volume Total Derramado (em barris)')
    plt.title('Volume Total de Petróleo Derramado por Ano')
    plt.grid(True)
    plt.show()
    menu()

def graficoCausasDerramamentos():
    causas_freq = dados['Causa'].value_counts()
    # Gráfico de pizza para causas dos derramamentos
    plt.figure(figsize=(8, 8))
    plt.pie(causas_freq, labels=causas_freq.index, autopct='%1.1f%%', startangle=140)
    plt.title('Causas dos Derramamentos de Petróleo')
    plt.show()
    menu()



menu()