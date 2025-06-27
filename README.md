# 🎬 Classificação de Sentimentos em Reviews de Filmes — IMDB

Este projeto implementa uma rede neural simples em Python, utilizando **TensorFlow/Keras**, para classificar automaticamente críticas de filmes do dataset **IMDB** como **positivas** ou **negativas**.

---

## 📌 Objetivo

Desenvolver um modelo de aprendizagem profunda (rede neural) capaz de identificar o **sentimento** (positivo ou negativo) de uma crítica textual de filmes com base em dados reais.

---

## 📂 Estrutura do Projeto

rede_imdb/

│
├── .env # Dependências necessárias

├── main.py # Código principal com o modelo e execução

├── requirements.txt # Lista de bibliotecas necessárias

├── README.md # Este ficheiro

└── .gitignore # Arquivos ignorados pelo Git


---

## ⚙️ Requisitos

- Python 3.9 ou superior
- pip

---

## 📥 Instalação e Execução

1. **Clona o repositório** no teu computador:

```bash
git clone https://github.com/Dongo-28/rede_imdb.git
cd rede_imdb

2. Cria e ativa um ambiente virtual (opcional mas recomendado):
python -m venv .venv
# No Windows
.venv\Scripts\activate
# No macOS/Linux
source .venv/bin/activate

3. Instala as dependências:
pip install -r requirements.txt

4. Executa o projeto:
python main.py

📊 Resultado Esperado
O modelo treina durante 10 épocas e apresenta a acurácia final nos dados de teste (ex: Acurácia nos dados de teste: 0.8675).


🧠 Tecnologias Usadas
- Python 3
- TensorFlow / Keras
- Dataset IMDB (incluído via tensorflow.keras.datasets)


🛠️ Personalização
Podes modificar:
- O número de épocas (epochs)
- A arquitetura da rede (Dense, Dropout, etc.)
- O pré-processamento dos dados
- A visualização de resultados com matplotlib


🤝 Autor
Amadeu Dongo Rocha
📧 Email: amadeudongo@gmail.com
📍 São Vicente, Cabo Verde


📝 Licença
Este projeto é livre para fins académicos e educacionais. Licença MIT ou outra à tua escolha.

---

### ⚠️ Nota

- Queres que te ajude a **criar um repositório GitHub** e fazer *push* do projeto?
- Posso também incluir uma **versão do README em inglês**, se quiseres tornar o projeto mais internacional.

Posso agora gerar o ficheiro `README.md` para colocares diretamente na pasta. Confirmas?