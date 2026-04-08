# Odin V11 | Deploy online no Render

## 1. Suba para o GitHub
Crie um repositório e envie os arquivos do Odin V11.

## 2. Crie o projeto no Render
- New +
- Blueprint
- escolha o repositório
- confirme

O arquivo `render.yaml` já cria:
- 1 web service
- 1 banco PostgreSQL

## 3. Primeira execução
O Render vai:
- instalar dependências
- aplicar migrações
- publicar estáticos
- subir o servidor Gunicorn

## 4. Criar usuário admin
Depois do deploy, no Shell do Render rode:
```bash
python manage.py createsuperuser
```

## 5. Variáveis importantes
O projeto já está preparado para:
- SECRET_KEY
- DEBUG=False
- ALLOWED_HOSTS
- CSRF_TRUSTED_ORIGINS
- DATABASE_URL
- OPENAI_API_KEY

## 6. Acessos
Rotas úteis:
- `/pdv/`
- `/salao/`
- `/cozinha/`
- `/caixa/`
- `/entrega/`
- `/estoque/`
- `/receitas/`
- `/whatsapp/`
- `/painel-dono/`
- `/admin/`

## 7. Observação importante
No Windows local, o projeto continua leve.
No online, ele usa PostgreSQL automaticamente via `DATABASE_URL`.


## Ajuste V12
No ambiente local Windows/Python 3.14, o driver PostgreSQL foi separado.
- local: `requirements.txt`
- produção: `requirements-prod.txt`

O `build.sh` já cuida disso automaticamente no Render.
