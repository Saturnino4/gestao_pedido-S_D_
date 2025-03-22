# Sistema de Gerenciamento de Pedidos

## Participantes
 - JÉSSICA CUNHA
 - MICHELA FURTADO
 - SATURNINO MENDES 

Sistema de gerenciamento de pedidos baseado em microserviços construído com Django, PostgreSQL e WSO2 Micro Integrator.

## Arquitetura

- **Backend**: Django REST Framework
- **Banco de Dados**: PostgreSQL
- **Gateway API**: WSO2 Micro Integrator 4.2.0
- **Containerização**: Docker & Docker Compose (parcial)

## Configuração

### Pré-requisitos

- Docker e Docker Compose
- WSO2 Integration Studio (para desenvolvimento)
- WSO2 Micro Integrator (instalação standalone)

### Executando a Aplicação

1. Clone este repositório
2. Crie um arquivo `.env` com as variáveis necessárias
3. Inicie os serviços de backend e banco de dados:
   ```
   docker compose up -d postgres backend
   ```
4. Inicie o WSO2 Micro Integrator manualmente (devido a problemas com a versão Docker)

### Acessando os Serviços

- **API Django**: http://localhost:8000/api/v1/pedido/
- **Gateway WSO2**: http://localhost:8290/pedido/
- **Console de Gerenciamento WSO2**: http://localhost:9201/

## Endpoints da API

Todos os endpoints são acessíveis através do WSO2 Micro Integrator em http://localhost:8290/pedido/

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | / | Listar todos os pedidos |
| POST   | /registrar/ | Criar um novo pedido |
| PUT    | /{id}/atualizar/ | Atualizar um pedido existente |
| DELETE | /{id}/eliminar/ | Excluir um pedido |
| POST   | /{id}/aprovar/ | Aprovar um pedido |
| POST   | /{id}/reprovar/ | Rejeitar um pedido |
-----------------------------------------------
## Fluxo de Desenvolvimento

### Modificando o Middleware WSO2

1. Abra o projeto no WSO2 Integration Studio
2. Modifique as definições de API
3. Construa o arquivo CAR (Exporte como Composite Application)
4. Implante o arquivo CAR no WSO2 Micro Integrator standalone
   - Copie o arquivo CAR para a pasta `<MI_HOME>/repository/deployment/server/carbonapps`
   - Ou use o Management Console para fazer o upload do arquivo

### Modificando o Backend Django

1. Faça alterações no código Django no diretório `backend`
2. As alterações serão refletidas automaticamente devido à montagem de volume

## Solução de Problemas

### API WSO2 Não Encontrada

Se receber erros "main sequence executed for call to non-existent":

1. Verifique se o arquivo CAR foi implantado corretamente
2. Verifique os logs do Micro Integrator em `<MI_HOME>/repository/logs`
3. Certifique-se de que os endpoints correspondem exatamente aos definidos no XML da API

### Problemas com o WSO2 Micro Integrator no Docker

Devido a dificuldades com o WSO2 Micro Integrator no Docker, estamos usando a versão standalone:

1. Baixe o WSO2 Micro Integrator do site oficial
2. Instale e configure conforme a documentação
3. Implante o arquivo CAR manualmente

### Problemas de Conexão com o Banco de Dados

Se o Django não conseguir se conectar ao PostgreSQL:

1. Verifique os logs do PostgreSQL: `docker compose logs postgres`
2. Confirme as variáveis de ambiente no arquivo `.env`
3. Certifique-se que o serviço de banco de dados está em execução: `docker compose ps`
