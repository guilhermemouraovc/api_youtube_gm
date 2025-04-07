# F1 Highlights 2024 - Dashboard Interativo com YouTube API

Este projeto consome dados da YouTube Data API v3 para exibir estatísticas dos vídeos de highlights da temporada 2024 da Fórmula 1. Os dados são exibidos em um dashboard interativo e estilizado com as cores da F1.

![Dashboard](https://i.imgur.com/amIHjRz.png) 


---

## Objetivos

- Acessar a playlist oficial da F1 no YouTube via API
- Extrair dados como visualizações, curtidas e comentários
- Organizar os dados em um CSV
- Exibir tudo em um dashboard visual com gráfico de barras e dispersão

---

## Tecnologias utilizadas

- Python 3.x  
- google-api-python-client  
- pandas  
- Dash (Plotly)  
- plotly-express  
- python-dotenv  

---

### Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/guilhermemouraovc/api_youtube_gm.git
cd seu-repo
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
### 3. Configure sua chave de API 
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave da API do YouTube
```env
YOUTUBE_API_KEY=sua_chave_aqui 
```
### 4. Coleta dos dados
Execute o script para buscar os dados da playlist:
```bash
python src/youtube_api.py
```
Esse comando irá gerar o arquivo dados_f1.csv

### 5. Inicie o dashboard
```bash
python src/dashboard.py
```
Abra o navegador e acesse:
http://127.0.0.1:8050/

### Resultado
- Visual com tema escuro e cores da Fórmula 1
- Gráficos interativos:
 - Visualizações por vídeo
 - Curtidas vs Comentários

### Repositório
https://github.com/guilhermemouraovc/api_youtube_gm

#### Desenvolvido por Guilherme Mourão
