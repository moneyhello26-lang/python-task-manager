# Python Task Manager

Простой консольный планировщик задач. Проект создан для практики Git: работа в ветках, слияние, rebase, разрешение конфликта и Pull Request.

## Возможности

- Добавление и просмотр задач.
- Отметка выполненных задач и удаление по номеру.
- Поиск по названию без учёта регистра.
- Интерактивное меню и сохранение задач в JSON.

## Технологии

Python 3.10 или новее, стандартная библиотека Python, Git и GitHub.

## Структура проекта

| Путь | Назначение |
| --- | --- |
| `src/core.py` | Операции с задачами и хранение данных |
| `src/main.py` | Команды и интерактивное меню |
| `tests/` | Автоматические проверки |
| [`requirements.txt`](requirements.txt) | Список внешних зависимостей |
| `.gitignore` | Исключения для Git |

## Установка

```bash
git clone https://github.com/moneyhello26-lang/python-task-manager.git
cd python-task-manager
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

В Windows активация окружения: `.venv\\Scripts\\activate`.

## Запуск и примеры

Команды запускаются из корня проекта. Если параметр `--data` не указан, задачи сохраняются в файле `~/.python-task-manager.json`.

```bash
python -m src.main add "Подготовить отчёт"
python -m src.main list
python -m src.main complete 1
python -m src.main search "отчёт"
python -m src.main delete 1
python -m src.main menu
```

Для отдельного файла данных добавьте `--data tasks.json` в конец команды. Команда `menu` предлагает просмотр и добавление задач; остальные действия доступны отдельными командами.

## Проверка

```bash
python -m unittest discover -s tests -v
```

## Зависимости

Внешних пакетов нет. `requirements.txt` намеренно пуст: программа использует только стандартную библиотеку. Установка из файла завершится без загрузки пакетов.

## Автор

ФИО и группу студент заполняет в отчёте самостоятельно.
