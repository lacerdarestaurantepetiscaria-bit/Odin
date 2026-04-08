<<<<<<< HEAD
# Odin
Sistema SaaS completo para gestão de restaurante (PDV, Delivery, Estoque, Financeiro e IA integrada)
=======
# Odin MVP | Render Ready

Base inicial do Odin preparada para:
- rodar localmente
- testar em servidor gratuito
- servir de fundação do sistema

## Já vem neste pacote
- Django configurado
- PostgreSQL via DATABASE_URL no deploy
- SQLite local
- WhiteNoise
- Gunicorn
- render.yaml para deploy no Render
- dashboard inicial
- cadastro de produtos
- cadastro de clientes
- criação de pedidos
- registro de pagamentos
- módulo inicial de IA por texto

## Como rodar localmente
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

Acesse:
- Sistema: http://127.0.0.1:8000
- Admin: http://127.0.0.1:8000/admin

## Celular na mesma rede
Rode:
```bash
python manage.py runserver 0.0.0.0:8000
```
Depois abra no celular o IP do PC, por exemplo:
`http://192.168.0.15:8000`

## Render
1. Envie para GitHub
2. Crie um Blueprint no Render
3. O `render.yaml` cria o serviço web e o Postgres

## Comandos de teste na tela Odin IA
- cliente pagou 60 no cartão
- desabilitar arroz branco
- habilitar arroz branco
- quanto vendeu hoje



## Correção para Windows / Python 3.14
Esta versão foi ajustada para **não exigir `psycopg2-binary` localmente**.
No PC, o sistema usa **SQLite** para teste local.
No Render, o PostgreSQL entra via `DATABASE_URL`.

Se você já criou um `venv` com erro, apague e recrie:
```bash
deactivate
rmdir /s /q venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```


## Upgrade visual V2
Esta versão recebeu uma interface mais forte, com sidebar, cards, atalhos rápidos e layout inspirado em sistemas modernos de restaurante.


## Odin V3 | PDV Operacional
Nova tela adicionada em `/pdv/` com:
- visual forte estilo frente de caixa
- busca rápida de produtos
- filtro por categoria
- carrinho lateral com quantidade
- botões rápidos de pagamento
- salvamento real de pedidos no banco

### Para usar depois de atualizar os arquivos:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```


## Odin V4 | Salão + KDS + Fechamento
Adicionado:
- `/salao/` com mapa de mesas
- `/cozinha/` com quadro KDS
- pagamento baixando pedido vinculado
- navegação lateral atualizada

### Para atualizar:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```


## Odin V5 | Caixa + Entrega + Comandas
Adicionado:
- `/caixa/` com abertura e fechamento
- totais por forma de pagamento
- `/entrega/` com fluxo de delivery
- salão mostrando itens por mesa
- pagamento baixando pedido vinculado

### Atualização:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```


## Odin V6 | Estoque + Ficha Técnica + IA Operacional
Adicionado:
- `/estoque/` para insumos
- `/receitas/` para ficha técnica
- baixa automática de estoque ao criar pedido no PDV quando houver ficha técnica
- custo estimado por produto
- comandos de IA para consulta e ajuste simples de estoque

### Comandos novos de IA
- `quanto tem de arroz`
- `estoque de arroz acabou`
- `desabilitar contra-filé`


## Odin V7 | WhatsApp IA + Pedido Natural
Adicionado:
- `/whatsapp/` com simulador de mensagens
- interpretação de pedido em linguagem natural
- geração opcional de pedido real no sistema
- log das últimas mensagens processadas

### Exemplos para testar
- `quero arroz, feijão, purê e fígado`
- `quero arroz e salada e um pedaço de peito de frango empanado`
- `dois contra filé acebolado e uma coca`


## Odin V8 | Gerente Digital + Automações
Adicionado:
- `/painel-dono/` com visão gerencial
- `/alertas/` com centro de atenção
- `/automacoes/` com regras rápidas
- novos comandos da IA:
  - `quanto vendi hoje`
  - `produto mais vendido`
  - `estoque baixo`
  - `fecha o caixa`


## Odin V10 | Refino Premium
Adicionado:
- visual premium mais consistente
- navegação agrupada por operação, cadastros e inteligência
- barra rápida no mobile
- PDV com carrinho persistente no navegador
- tela de pedidos com pesquisa rápida

Esta versão foca em:
- UX
- leitura visual
- fluidez operacional
- preparação para deploy online


## Odin V11 | Online Ready
Adicionado:
- `Procfile`
- `runtime.txt`
- `render.yaml`
- `GUIA_DEPLOY_RENDER_V11.md`
- suporte melhor para produção
- `psycopg[binary]` para PostgreSQL online
- configurações de `CSRF_TRUSTED_ORIGINS` e cookies seguros

Objetivo desta versão:
- deixar o Odin pronto para deploy online com menos tropeços
- manter o uso local no VS Code simples


## Odin V12 | Correção Windows / Python 3.14
Correção aplicada:
- removido o driver PostgreSQL do `requirements.txt` local
- criado `requirements-prod.txt` para produção
- `build.sh` instala o driver PostgreSQL apenas no deploy
- local continua leve com SQLite

### Local
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

### Produção
O Render usa:
- `requirements.txt`
- `requirements-prod.txt`
- `build.sh`


## Odin V13 | Admin automático sem Shell
Esta versão adiciona o comando `bootstrap_admin`.

### O que muda
- cria ou atualiza superusuário automaticamente no deploy
- funciona por variáveis de ambiente
- evita depender do Shell pago do Render

### Variáveis necessárias no Render
- `ADMIN_USERNAME`
- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`

### Fluxo
1. subir arquivos no GitHub
2. configurar as 3 variáveis no Render
3. fazer deploy manual
4. entrar em `/admin/`
>>>>>>> da5694a (V13 admin automatico)
