# Superstore Sales Prediction ML Project

## Описание проекта

Данный проект представляет собой систему предсказания продаж на основе датасета https://www.kaggle.com/datasets/vivek468/superstore-dataset-final  с использованием методов машинного обучения.

Проект включает полный ML pipeline:

- загрузка и анализ данных (EDA)
- предобработка данных
- обучение нескольких моделей
- сравнение метрик
- деплой Streamlit приложения через Streamlit Cloud

---

## Цель проекта

Предсказать значение **Sales** на основе характеристик заказа:

- Ship Mode
- Segment
- Region
- Category
- Sub-Category
- Quantity
- Discount
- order_year
- order_month

---

## Используемые модели

### Baseline model
- Linear Regression

### Улучшенные модели
- Random Forest Regressor
- XGBoost Regressor

---

## Метрики оценки

Использовались следующие метрики:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

Пример результатов:

| Model | MAE | RMSE | R2 |
|---|---|---|---|
| Linear Regression |  226.362425|693.342018 | 0.186179 |
| Random Forest |215.225520 |  687.163334 | 0.200619
| XGBoost |196.565317 | 672.482683  | 0.234411

---

## Этапы проекта

### 1. Data Analysis (EDA)

Проведены:

- проверка пропусков
- корреляционная матрица
- анализ категориальных признаков

---

### 2. Preprocessing

Использованы:

- обработка даты заказа
- извлечение:
  - order_year
  - order_month
- удаление нерелевантных колонок
- OneHotEncoding категориальных признаков
- StandardScaler для числовых признаков

---

### 3. ML Pipeline

Использован sklearn Pipeline:

- ColumnTransformer
- OneHotEncoder
- StandardScaler
- model

---

## Streamlit приложение

Пользователь может ввести параметры заказа и получить предсказание Sales.

### Интерфейс включает:
- выбор категорий
- quantity
- discount
- год и месяц заказа

Дополнительно отображаются графики:
- распределение Sales
- продажи по категориям

---

## Структура проекта

```text
superstore-sales-prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── Sample - Superstore.csv
└── README.md
