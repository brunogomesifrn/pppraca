# Praça da Paz Entre os Povos 

## Instalação:
1. Criar o ambiente virtual para instalar as bibliotecas (se o primeiro comando a seguir não funcionar, utilizar o segundo):
- virtualenv venv
- python -m venv venv

2. Instalar as bibliotecas necessárias para a execução do projeto:
- pip install django
- pip install Pillow
- pip install django-widget-tweaks

3. Clonar o projeto:
- git clone https://github.com/brunogomesifrn/pppraca

4. Executar comandos de criação e atualização do banco de dados:
- python manage.py makemigrations usuario core planta espaco
- python manage.py migrate

## Aplicações do Projeto:
- **core**: responsável pelas páginas públicas do projeto (inicial, lista de plantas, detalhes de plantas, lista de espaços, contato, login, cadastro de usuário, visitacao, producoes);
- **planta**: responsável pelo gerenciamento das plantas da praça;
- **espaco**: responsável pelo gerenciamento dos espaços da praça;
- **usuario**: responsável pelo gerenciamento de usuários e permissões de acesso ao projeto.

## Templates e Statics
- As pastas **templates** e **statics** na raiz do projeto servem apenas para as bases que serão exportadas nas demais páginas do projeto, ou seja, estará o layout modularizado;
- Cada aplicação possui suas próprias pastas **templates** e **static**, então as páginas com conteúdos e estilos específicos devem ser criados na própria aplicação;

## Trabalho em brachs:
- Quando for modificar alguma aplicação do projeto, deve usar a brach de mesmo nome. Por exemplo: Se for alterar algo na aplicação **planta**, usar a branch **planta**. A única exceção é se alterar algum arquivo de configuração geral, como settings.py ou o urls.py principal, então deve usar a brach **core**.
- Comandos (supondo que irá alterar algo na app planta):
    - Atualizar branchs do github no repositório local:
        - git pull
    - Verificar em qual branch está no momento (aparece um * do lado do nome):
        - git branch
    - Mudando para outra branch (são duas possibilidades, um comando ou outro):
        - git checkout planta
        - git switch planta
    - Verificar se houve atualizações na branch principal (main) e atualizar o branch atual (planta):
        - git pull origin main --rebase
    - Você está na branch planta, após as modificações, basta seguir os comandos normais de atualização:
        - git add .
        - git commit -m "comentário"
    - Enviar o branch para o repositório:
        - git push
