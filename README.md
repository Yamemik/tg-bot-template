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
    USER |o--o{ PAYMENT : creates
    USER |o--o{ REQUEST : creates
    USER {
        int telegram_id PK      
        string username "*"
        string first_name "*"      
    }
    PAYMENT {
      int id PK
      float summary 
      int user_id FK
    }
    REQUEST {
      int id PK
      bool is_access 
      int user_id FK
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
