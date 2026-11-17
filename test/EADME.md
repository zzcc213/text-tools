# text-tools

Невеликий застосунок на Python з функціями для роботи з рядками:

- `reverse_string` — повертає рядок у зворотному порядку;
- `is_palindrome` — перевіряє, чи є рядок паліндромом;
- `count_words` — рахує кількість слів у рядку.

## Запуск

```bash
python textutils.py reverse "Привіт"
python textutils.py palindrome "Нагорі роган"
python textutils.py words "раз два три"
```

## Тести та перевірка стилю

```bash
pip install -r requirements-dev.txt
pytest -v
black --check --diff .
```

## CI

Пайплайн `.github/workflows/ci.yml` запускається при кожному push і pull request.
Він містить два незалежні паралельні jobs:

- **Tests** — запускає тести `pytest`; завершується з помилкою, якщо хоча б один тест не пройшов;
- **Lint (Black)** — перевіряє форматування коду `black --check`; завершується з помилкою, якщо код не відформатовано.
