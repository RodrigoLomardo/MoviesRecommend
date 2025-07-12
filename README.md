# Sistema de Recomendação de Filmes - Flask + Python

## Descrição

Este projeto implementa um sistema simples de recomendação de filmes utilizando Python e Flask. Baseado em similaridade de gêneros usando TF-IDF e similaridade do cosseno, o sistema oferece recomendações inteligentes a partir de um título informado pelo usuário.

O frontend foi desenvolvido com Bootstrap 5 e possui busca com autocomplete e requisições AJAX para carregar recomendações dinamicamente sem recarregar a página.

---

## Tecnologias utilizadas

- Python 3.x
- Flask
- Pandas
- Scikit-learn (TF-IDF Vectorizer e Cosine Similarity)
- Bootstrap 5
- JavaScript (Fetch API para AJAX)

---

## Estrutura do projeto

/
├── main.py # Aplicação Flask
├── templates/
│ └── index.html # Template HTML com Bootstrap e JS
├── ml-latest-small/
│ ├── movies.csv # Dataset de filmes
│ └── ratings.csv # Dataset de avaliações (não usado diretamente)
└── README.md # Documentação do projeto


Funcionalidades
- Cálculo da similaridade entre filmes baseado nos gêneros usando TF-IDF e similaridade do cosseno

- Interface web responsiva com Bootstrap 5

- Busca com autocomplete via AJAX (rota /autocomplete)

- Requisições AJAX para obter recomendações (rota /recommend)

- Atualização dinâmica dos resultados sem reload da página

Detalhes técnicos
Backend (Flask)
- Carregamento e pré-processamento do dataset usando Pandas

- Vetorização dos gêneros com TfidfVectorizer(stop_words='english')

- Cálculo da matriz de similaridade do cosseno entre filmes

- Rota /autocomplete: recebe parâmetro q e retorna até 10 títulos correspondentes

- Rota /recommend: recebe JSON com movie e retorna lista de recomendações

- Rota /: serve a página HTML

Frontend
- HTML + Bootstrap 5 para layout e estilização

JavaScript para:

- Capturar evento de input e fazer fetch para autocomplete

- Capturar submit do formulário para buscar recomendações via fetch



