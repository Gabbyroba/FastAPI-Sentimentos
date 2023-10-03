# Feeling You - Backend

Este é o repositório do backend da aplicação Feeling You, que oferece uma API para analisar sentimentos e sugerir músicas com base nos sentimentos selecionados pelos usuários. Este README fornece uma documentação completa sobre o backend do projeto.

## Conteúdo

- [Introdução](#introducao)
- [Demonstração](#demonstracao)
- [Configuração do Ambiente](#configuracao-do-ambiente)
- [Autenticação Spotify](#autenticacao-spotify)
- [Rotas da API](#rotas-da-api)
  - [GET /](#get-root)
  - [POST /analisar-sentimento](#post-analisar-sentimento)
- [Executando o Backend](#executando-o-backend)
- [Contribuição](#contribuicao)
- [Licença](#licenca)

## Introdução

O backend do projeto Feeling You é desenvolvido com o framework FastAPI e tem como objetivo fornecer uma API que aceita solicitações de análise de sentimentos. Ele se integra com a API do Spotify para buscar músicas relacionadas aos sentimentos selecionados.

## Demonstração

A API Feeling You está hospedada em: [https://fastapisentimentos.onrender.com](https://fastapisentimentos.onrender.com)

## Configuração do Ambiente

Para configurar o ambiente de desenvolvimento local, siga estas etapas:

1. Clone o repositório do backend:

   ```shell
   git clone https://github.com/Gabbyroba/FastAPI-Sentimentos.git
   ```

2. Navegue até o diretório clonado:

   ```shell
   cd FastAPI-Sentimentos
   ```

3. Instale as dependências usando o gerenciador de pacotes Python (pip):

   ```shell
   pip install -r requirements.txt
   ```

## Autenticação Spotify

O backend se autentica na API do Spotify para obter informações sobre as músicas sugeridas. A autenticação é realizada usando o fluxo de autenticação de credenciais de cliente. As credenciais do cliente (client_id e client_secret) devem ser definidas nas variáveis `client_id` e `client_secret` no código.

## Rotas da API

### GET /

Esta rota de raiz fornece uma mensagem de boas-vindas à API Feeling You.

**Exemplo de solicitação:**

```shell
GET /
```

**Exemplo de resposta:**

```json
{
  "message": "Boas vindas à API Feeling You!"
}
```

### POST /analisar-sentimento

Esta rota permite aos usuários enviar um JSON com sentimentos selecionados e recebe como resposta uma lista de músicas sugeridas com base nos sentimentos.

**Exemplo de solicitação:**

```json
{
  "sentimento": "Tristeza, Nostalgia"
}
```

**Exemplo de resposta:**

```json
{
  "sentimentos": ["Tristeza", "Nostalgia"],
  "musicas_sugeridas": [
    "Tristeza: Nome da Música 1",
    "Nostalgia: Nome da Música 2"
  ]
}
```

## Executando o Backend

Para iniciar o servidor FastAPI localmente, execute o seguinte comando a partir do diretório raiz do projeto:

```shell
uvicorn main:app --reload
```

Isso iniciará o servidor na porta 8000 por padrão. Você pode acessar a API em [http://localhost:8000](http://localhost:8000).

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar ou adicionar recursos ao backend do projeto Feeling You, siga estas etapas:

1. Faça um fork deste repositório.

2. Clone seu fork:

   ```shell
   git clone https://github.com/seu-usuario/FastAPI-Sentimentos.git
   ```

3. Crie uma branch para suas alterações:

   ```shell
   git checkout -b minha-alteracao
   ```

4. Faça as alterações desejadas no código.

5. Commit e faça push para o seu fork:

   ```shell
   git commit -m "Minha alteração"
   git push origin minha-alteracao
   ```

6. Abra um pull request neste repositório para revisão.

Este README fornece informações detalhadas sobre o backend do projeto Feeling You. Use-o como referência para configurar, executar e contribuir para o projeto.
