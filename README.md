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
| Linear Regression | 0.805421 | 1.028351 | 0.584829
| Random Forest |0.855757 | 1.104322 | 0.521220
| XGBoost |0.803329 | 1.027093 | 0.585843

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

Пользователь может ввести параметры заказа и получить предсказание Sales. Link: https://zhanelashirbek-superstore-sales-prediction-app-sdimec.streamlit.app/

### Интерфейс включает:
- выбор категорий
- quantity
- discount
- год и месяц заказа

Дополнительно отображаются графики:
- распределение Sales
- продажи по категориям

---

