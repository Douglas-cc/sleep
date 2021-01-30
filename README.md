# Sleep data app
Se trata de uma ferramenta de analise de dados do comportamento do corpo durante o sono (respiração, batimentos cardíaco, pressão etc..) que foi catalogado com Xiaomi Mi Band 4. A ferramenta foi desenvolvida usando lib streamlit que transforma scripts de dados Python em aplicativos web compartilháveis. 

## Requisitos

Você precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais
com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes de dependências
do Projeto:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

## Como executar localmente?
```
baixe o repositório e execute no terminal: 
streamlit run sleep.py

```
## Confira o resultado no link aplicação:
https://sleep42.herokuapp.com/?fbclid=IwAR3furqoeCr0SGZjg2JGEJnwsqORdJAyJrHdbOTSy5wXi95XvI3rg1OnhhU
