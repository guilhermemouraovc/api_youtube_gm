# F1 Highlights 2024 - Dashboard Interativo com YouTube API

Este projeto consome dados da YouTube Data API v3 para exibir estatísticas dos vídeos de highlights da temporada 2024 da Fórmula 1. Os dados são exibidos em um dashboard interativo e estilizado com as cores da F1.

![Dashboard](https://i.imgur.com/amIHjRz.png) 

![Tutorial](https://youtu.be/2PypUh8Ma-A?si=JeRW5lMJLYtaKFSr)
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

### Decisões técnicas
- Organização do projeto: separei o código em dois arquivos principais:
  - youtube_api.py para a coleta e tratamento dos dados
  - dashboard.py para exibição visual dos dados
 
- Uso do .env para segurança: armazenei a chave da API em um arquivo .env e usei a biblioteca python-dotenv para carregá-la no código. Isso garante que a chave não seja exposta publicamente no GitHub, seguindo boas práticas de segurança.
  
- Ferramentas Escolhidas: utilizei o Dash (Plotly) para construção do dashboard por sua simplicidade, flexibilidade e capacidade de gerar visualizações responsivas e interativas com poucos comandos, além de permitir personalização estética com CSS embutido e temas escuros.

- Visual do Dashboard: personalizei o dashboard com cores da identidade visual da F1 (fundo escuro e vermelho), adicionei ícone e logotipo da F1, e linkei o repositório do GitHub no rodapé para facilitar o acesso e compartilhamento.

### Maiores desafios encontrados
- Limitações da API (quota e paginação): Precisei lidar com a paginação da API para obter todos os vídeos da playlist (limitados a 50 por requisição). Além disso, a API tem limites de uso por dia (quota), então precisei testar com cuidado para não ultrapassá-los.
- Padronização dos Dados: os vídeos têm formatos variados de títulos e publicações. Foi necessário organizar os dados para garantir que gráficos e análises fossem coerentes, como conversão de datas e tratamento de números ausentes (ex: likes ou comentários desabilitados).
- Estilização e Integração Visual: ajustar o layout visual do dashboard para que ficasse com identidade própria (F1 style) exigiu várias tentativas com CSS inline e ajustes de cores no Plotly. Adicionar o logotipo e o ícone no navegador também exigiu conhecer a estrutura assets/ do Dash.
- Evitar exposição da chave da API: garantir que o .env não fosse enviado ao repositório e configurar o código para funcionar com variáveis de ambiente foi essencial para manter o projeto seguro.


### Repositório
https://github.com/guilhermemouraovc/api_youtube_gm

#### Desenvolvido por Guilherme Mourão
