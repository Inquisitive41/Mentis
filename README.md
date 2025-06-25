# Mentis
The Method of Fundamental AI Learning Based on Hypothetical Thinking: The Nova Mentis Paradigm
# Nova Mentis: Гипотезное мышление для ИИ

## Описание
Nova Mentis — фундаментальный метод обучения искусственного интеллекта, основанный на гипотезном мышлении. В отличие от статистических моделей, система формирует и проверяет гипотезы, строит теории и хранит знания в графе понятий.

## Философия
- Учится через структурированные знания и логические выводы
- Формирует и проверяет гипотезы, строит теории
- Работает с абстракциями (числа, графы, логические выражения)
- Интерпретируемость и адаптация в реальном времени
- Независимость от языка и устойчивость к шуму данных

## Архитектура
- **Гипотезатор (Hypothesizer):** Генерирует предположения на основе входных данных.
- **Логический тестер (Logical Tester):** Проверяет гипотезы на новых примерах.
- **Корректор (Corrector):** Корректирует веса гипотез при появлении новых данных.
- **Граф памяти (Memory Graph):** Хранит проверенные знания и причинно-следственные связи.

## Преимущества
- Обучение на малых примерах (2-3 примера)
- Интерпретируемость: логические цепочки вместо «чёрного ящика»
- Масштабируемость: работает локально, не требует больших данных
- Инновация: построение теорий, а не просто запоминание

## Пример использования
```python
from Mentis import NovaMentis
nm = NovaMentis()
data = [(1, 1), (2, 4)]
theory, graph = nm.build_theory(data)
print(f"Теория: {theory}")
new_data = [(3, 9)]
nm.update(new_data)
print(f"Обновлённая теория: {max(nm.hypotheses, key=nm.hypotheses.get)}")
```

## Пример вывода
```
Теория: n^2 = y
Обновлённая теория: n^2 = y
```

## Структура кода
- `NovaMentis` — основной класс
- `hypothesize` — генерация гипотез
- `_test_hypothesis` — тестирование гипотезы
- `update` — корректировка весов
- `build_theory` — построение теории и графа

## Установка
```bash
pip install -r requirements.txt
```

## Запуск демо
```bash
python Mentis.py
```

## Contributing
Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.

## License
MIT License

## Контакты / Contacts
- Telegram: https://t.me/Inqusitive41
- Qalam AGI

---

# Nova Mentis: Hypothesis-Driven AI Learning (EN)

## Description
Nova Mentis is a fundamental AI learning method based on hypothesis-driven reasoning. Unlike statistical models, it forms and tests hypotheses, builds theories, and stores knowledge in a concept graph.

## Philosophy
- Learns through structured knowledge and logical inference
- Forms and tests hypotheses, builds theories
- Works with abstractions (numbers, graphs, logical expressions)
- Interpretability and real-time adaptation
- Language independence and robustness to data noise

## Architecture
- **Hypothesizer:** Generates hypotheses from input data
- **Logical Tester:** Validates hypotheses on new examples
- **Corrector:** Adjusts hypothesis weights with new data
- **Memory Graph:** Stores validated knowledge and causal links

## Advantages
- Few-shot learning (2-3 examples)
- Interpretability: logical chains instead of a "black box"
- Scalability: works locally, no need for big data
- Innovation: theory-building, not just memorization

## Usage Example
```python
from Mentis import NovaMentis
nm = NovaMentis()
data = [(1, 1), (2, 4)]
theory, graph = nm.build_theory(data)
print(f"Theory: {theory}")
new_data = [(3, 9)]
nm.update(new_data)
print(f"Updated theory: {max(nm.hypotheses, key=nm.hypotheses.get)}")
```

## Example Output
```
Theory: n^2 = y
Updated theory: n^2 = y
```

## Code Structure
- `NovaMentis` — main class
- `hypothesize` — hypothesis generation
- `_test_hypothesis` — hypothesis testing
- `update` — weight correction
- `build_theory` — theory and graph construction

## Installation
```bash
pip install -r requirements.txt
```

## Demo Run
```bash
python Mentis.py
```

## Contributing
Pull requests and suggestions are welcome! Please open an issue first to discuss what you would like to change.

## License
MIT License

## Contacts
- Telegram: https://t.me/Inqusitive41
- Qalam AGI 
