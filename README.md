# PosTechChallenge3

## 💻 Execute o Projeto

### 1. Clone o repositório

```
git clone https://github.com/KaiqueBM/PosTechChallenge3
```

### 2. Instale a versão do Python 3.13.3

```
https://www.python.org/ftp/python/3.13.3/python-3.13.3-amd64.exe
```

### 3. Ative a venv e instale as bibliotecas

```cmd
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

## Base

Modelo supervisionado -> Regressão
CO2 Emissions(g/km) é uma variavel contínua

Possíveis problemas que dá para prever com a base:
-Dado um carro novo (com ficha técnica conhecida), prever sua emissão de CO₂.
-Identificar quais características do carro mais influenciam as emissões (ex: motor maior = mais CO₂).
-Cenários específicos (exemplo: Qual o efeito de escolher transmissão manual vs automática?)

Features numéricas:
-Engine Size(L)
-Cylinders
-Fuel Consumption City (L/100 km)
-Fuel Consumption Hwy (L/100 km)
-Fuel Consumption Comb (L/100 km)
-Fuel Consumption Comb (mpg)

Features categórias:
-Make
-Model
-Vehicle Class
-Transmission
-Fuel Type

Essas precisam ser convertidas para numéricas
