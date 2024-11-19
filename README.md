# bot (tg bot)

![Static Badge](https://img.shields.io/badge/Yamemik-tgtemplate)
![GitHub top language](https://img.shields.io/github/languages/top/Yamemik/tg-bot-template)
![GitHub](https://img.shields.io/github/license/Yamemik/tg-bot-template)
![GitHub Repo stars](https://img.shields.io/github/stars/Yamemik/tg-bot-template)
![GitHub issues](https://img.shields.io/github/issues/Yamemik/tg-bot-template)


## Общее описание
_____
### Краткое описание
...


## Техническое описание
_____
### Стек технологий:
  - Python;
  - SQLite/PostgreSQL.

### ER-Diagrams
```mermaid
erDiagram
    USER }o--o{ COURSE : wrights    
    USER {
        int id PK      
        string email "*"
        string hashed_password "*"
        bool is_active
        bool is_superuser
        bool is_verified        
    }

```


## Python
_____

### PipENV
```bash
# install pipenv
pip install pipenv
# .venv in fold of the project
$env:PIPENV_VENV_IN_PROJECT=1
# initilization
pipenv shell
# install
pipenv install
```

## Ссылки
_____
[by Yamemik](https://github.com/Yamemik)
