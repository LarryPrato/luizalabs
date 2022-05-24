CONTENTS OF THIS FILE
---------------------
1-. Introdução
 Seviço web (app) criado para visualização de grafos. Desenvolvido em python usando a framework Flask, 
 seguindo os princípios REST. Para o analise  do grafo foi usada a biblioteca NetworkX. 
 A app  vem pré-carregada com uma grafo inicial, no entanto, novos vértices (nomes de pessoas) e novas 
 conexões poderão ser cadastrados, criando, em consequência, modificações a forma do grafo original.

2-. Requerimentos
    - Python 3
    - Flask
    - NetworkX
    - Pandas
    - Matplotlib

3-. Estrutura do projeto
O app foi desenvolvido seguindo uma divisão do tipo estrutural da seguinte forma:
   + projeto
   |- app/
   |     |- __init__.py
   |     |- controller/
   |     |     |-  __init__.py
   |     |- database/
   |     |     |-  __init__.py
   |     |     |- schema.sql
   |     |- logic
   |     |     |-  __init__.py
   |     |- static/
   |     |     |- favicon.ico
   |     |- templates/
   |     |     |- index.html
   |     |     |- page1.html
   |     |     |- page2.html
   |     |     |- page3.html
   |     |     |- page4.html
   |     |     |- database.html
   |     |     |- 404.html
   |- run.py
   |- env/
   |- Dockerfile
   |- .gitingnore
   |- Readme.txt

A pasta 'app/' contem o código para criar o app, o objeto principal do projeto. Dentro da mesma 
tambem estão contidas as seguintes pastas:
    * 'controller/' -> contem o código com todas as funções de vista do app.
    * 'database/' -> contem o código para criar o banco de dados e o 'schema.sql' que define a estrutura 
    da tabela do banco.
    * 'logic/' -> contem o código com a lógica para gerar a informação que será disponibilizada no app (
    o equivalente as regras do negocio).
    * 'static/' -> contem o favicon.ico
    * 'templates/' -> contem os arquivos html que serão renderizados quando recibam uma chamada das funções 
    de vista.
O arquivo 'run.py' serve para executar o app.
A pasta 'env/' representa o ambiente virtual criado para desenvolver o app. Inclui todos os pacotes 
requeridos para a execução do mesmo. 
O Dockerfile contem as instruções requeridas para executar o app desde um contêiner (docker)
O arquivo '.gitingnore/' especifica os aruivos que Git deve ignorar.
O 'requirements.txt' indica que pacotes ou libs, com as respectivas versoes, são requeridas para poder
 executar o app.

4- Pattern usado.
O app foi desenvolvido seguindo o design pattern "Lazy Loading" pois ajuda as páginas a exibirem seus 
conteúdos de maneira mais ágil e eficiente.

5-. Banco de dados. Foi implementado um banco de dados usando sqlite3. O mesmo serve como exemplo de suporte 
para fazer a persistência dos dados.

6-. Dockerfile. O serviço docker deve ser executado com a seguinte linha de comando:
"docker run -it --publish 7000:4000 web_service". Onde 'web_service' representa o nome da imagen.
O app será executado no localhost no porto 7000 (localhost:7000)

7-. Blueprint. Foi usado o recurso do blueprint para modularizar o app.

8-. O app pode ser executado com a seguinte linha de comando:'python run.py' e deve-se seguir a rota 
inidicada após a execução para poder visualizar o webservice.

