1.  # Análise de Derramamentos de Petróleo

Este projeto oferece uma solução em Python para analisar dados de derramamentos de petróleo, gerando gráficos e explorando os dados de forma interativa. Utilizamos a biblioteca `pandas` para manipulação de dados e `matplotlib` para visualização.
    
    ## Funcionalidades
    
    O script permite ao usuário:
    
    1.  Visualizar a frequência de derramamentos de petróleo por ano.
    2.  Visualizar o volume total de petróleo derramado por ano.
    3.  Visualizar as causas dos derramamentos de petróleo.
    4.  Obter informações sobre o impacto ambiental do petróleo.
    
    ## Requisitos
    
    -   Python 3.x
    -   pandas
    -   matplotlib
    
    ## Instalação
    
    1.  Clone este repositório ou faça o download dos arquivos.
    2.  Instale as dependências necessárias:
    
     `pip install pandas matplotlib` 
    
    3.  Certifique-se de que o arquivo `derramamentos.csv` esteja no mesmo diretório do script Python.
    
    ## Estrutura dos Dados
    
    O arquivo `derramamentos.csv` deve conter as seguintes colunas:
    
    -   `Data`: Data do derramamento (formato `AAAA-MM-DD`).
    -   `Volume`: Volume de petróleo derramado (em barris).
    -   `Causa`: Causa do derramamento.
    
    ## Uso
    
    Execute o script Python para iniciar o menu interativo no seu terminal/prompt de comando: python derramamentos.py
    
3.  ###    Menu Interativo 
	O menu apresenta as seguintes opções: Frequência de Derramamentos: Exibe um gráfico de barras mostrando o número de derramamentos por ano. Total Derramado: Exibe um gráfico de linha mostrando o volume total de petróleo derramado por ano. Causas dos Derramamentos: Exibe um gráfico de pizza mostrando a distribuição das causas dos derramamentos. Informações sobre o Impacto Ambiental: Exibe informações adicionais sobre o impacto do petróleo no meio ambiente. Sair: Encerra o programa. Exemplo de Uso Após iniciar o script, você verá um menu como este: Copiar código --------------- Menu 1) Frequencia de Derramamentos 2) Total Derramado 3) Causas dos Derramamentos 4) Informações sobre o impacto do petróleo no meio ambiente. 5) Sair
    
    Digite o número da opção desejada e pressione Enter para visualizar o gráfico correspondente ou obter informações. Estrutura do Código O script está organizado em funções para facilitar a leitura e manutenção: 
   * **menu():** Exibe o menu interativo e aguarda a escolha do usuário. 
   * **graficoFrequenciaDerramamentos():** Gera e exibe o gráfico de frequência de derramamentos por ano. 
   * **graficoTotalDerramado():** Gera e exibe o gráfico de volume total derramado por ano.
   *  **graficoCausasDerramamentos():** Gera e exibe o gráfico de causas dos derramamentos. 
   * **informacoesImpacto():** Exibe informações sobre o impacto ambiental dos derramamentos de petróleo.

**

## Desenvolvedores:

> **Gustavo do Espírito Santo - RM 559034** <br>
> **Heitor Prestes - RM 554823**
