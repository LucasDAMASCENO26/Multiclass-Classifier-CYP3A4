---

# Previsão de Atividade Molecular - CYP3A4

Este projeto é uma aplicação web desenvolvida em Python usando Flask, projetada para prever a atividade molecular de compostos em relação à enzima CYP3A4. A aplicação permite que o usuário desenhe moléculas ou insira a estrutura molecular em formato SMILES, utilizando o EPAM Ketcher, e obtenha uma previsão de atividade baseada em um modelo de aprendizado de máquina previamente treinado.


## Versão do Python Utilizada
       Python 3.10.5

## Configuração do Ambiente Virtual
Para garantir a correta instalação das dependências e isolar o ambiente de desenvolvimento, siga os passos abaixo:

1. Clone o repositório:

Primeiro, clone o repositório do projeto para o seu ambiente local:
       (https://github.com/LucasDAMASCENO26/Multiclass-Classifier-CYP3A4)


2. Crie o ambiente virtual:

Crie um ambiente virtual para o projeto. Isso garante que todas as dependências sejam instaladas em um ambiente separado:
```python3.10 -m venv venvv```


3. Ative o ambiente virtual:

Antes de instalar as dependências, ative o ambiente virtual:

  No Windows:
  ```venv\Scripts\activate
```

  No macOS/Linux:
  ```source venv/bin/activate 
```

4. Instale as dependências:

O arquivo requirements.txt lista todas as bibliotecas necessárias para rodar o projeto.



## Estrutura do Repositório
O projeto está organizado da seguinte forma:

  app.py: Arquivo principal que contém a aplicação Flask e define as rotas da aplicação.
  static/: Contém arquivos estáticos como CSS e JavaScript.
  lgbm_model.pkl: Arquivo com o modelo de aprendizado de máquina LightGBM treinado para previsão da atividade molecular.
  label_encoder.pkl: Arquivo com o LabelEncoder utilizado para transformar as classes de saída (ativadores, inibidores, inativos) em labels numéricas.

## Como Funciona

1. Desenho da Molécula:

  O usuário desenha a molécula ou insere uma string SMILES na interface Ketcher, que é embutida na página HTML através de um iframe.

  A molécula desenhada é convertida para o formato SMILES (Simplified Molecular Input Line Entry System), que é um formato textual que descreve a estrutura química da molécula.

2. Envio da Molécula:

Ao clicar em "Enviar Molécula", o SMILES é capturado via JavaScript e enviado para o servidor Flask usando uma requisição POST.

3. Geração de Descritores Moleculares:

  No servidor, o RDKit é utilizado para gerar descritores moleculares a partir do SMILES enviado. Esses descritores são usados como features (características) para o modelo de aprendizado de máquina.

4. Preprocessamento dos Dados:

  O label_encoder.pkl é utilizado para converter os labels das classes de saída (ativadores, inibidores, inativos) em valores numéricos.

5. Predição de Atividade:

  O modelo de aprendizado de máquina (um LightGBM treinado) recebe os descritores moleculares e faz a predição de atividade da molécula.

  O resultado é convertido de volta para sua classe original usando o label_encoder.pkl e é enviado de volta para o cliente, sendo exibido na página.

## Rodando a Aplicação Web

Para rodar a aplicação web localmente:

  Inicie o servidor o script app.py:

O comando iniciará o servidor de desenvolvimento Flask. Por padrão, a aplicação estará disponível no endereço 
http://127.0.0.1:5000/.


## Contato

Sinta-se à vontade para entrar em contato caso tenha alguma dúvida ou sugestão.

- LinkedIn: [Lucas Santos](https:// www.linkedin.com/in/lucas-santos-0245482b2)
- Email: lucas.damasceno.santos@icen.ufpa.br


---
