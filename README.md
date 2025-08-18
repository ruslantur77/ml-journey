# ml-journey  
4-недельный путь от нуля до продакшена в Data Science / ML.

## ✅ Проекты за первую неделю

| День | Название | Что сделано |
|---|---|---|
| **1–2** | Wine Bias–Variance Demo | На датасете Wine Quality сравннение деревья разной глубины и построение графика «train vs test error», чтобы наглядно увидеть bias и variance. |
| **3** | Wine Pipeline & GridSearch | Собран sklearn Pipeline (StandardScaler → RandomForest) и подобран `max_depth` + `n_estimators` через GridSearchCV; лучший F1 ≈ 0.41. |
| **4** | Imbalance & SMOTE | Сгенерирован синтетический датасет (95 % «0», 5 % «1»). Применен SMOTE, поднят recall c 6 % до 31 % и F1 до 0.37, показав как бороться с дисбалансом. |
| **5** | Linear Regression | Vспользован датасет цен домов «House Prices». Модель – простая LinearRegression, обученная после стандартизации признаков, но итоговый RMSE ≈ 69 k (R² ≈ 0.57) показывает, что линейная регрессия не достаточно хорошо описывает зависимость цен от признаков, поэтому её стоит заменить более гибкими моделями.|
| **6** | PostgreSQL & Data Pipeline, Prophet Forecast | Поднят Docker-контейнер PostgreSQL, создана таблица продаж и загружен CSV-файл с 1095 записями (365 дней × 3 товара). Написаны SQL-запросы для ежедневной агрегации. На ежедневных агрегатах обучена модель Prophet и сохранена в week1-day6-prophet.pkl, готовая к прогнозу на 30 дней вперёд. |
| **7** | FastAPI + Docker | Собран микро-сервис: FastAPI (/predict, /health) + Docker-контейнер; API отдаёт JSON-прогноз по http://localhost:8000/predict?days=30. |
| 8–9 | PyTorch MNIST + Regularization | Обучена полносвязная сеть на MNIST с dropout (0.3), L2 (weight-decay 1e-4) и L1 (1e-5); достигнута точность 97.45 %, раннее прекращение и логи TensorBoard сохранены.|
| 10 | TensorFlow CNN Cifar10 | Обучена модель на датасете CIFAR-10 (60k изображений 32x32 пикселей, 10 классов). Метрики на тестовых данных: accuracy: 0.7296 - loss: 0.7868, на валидационных: val_accuracy: 0.7230 - val_loss: 0.8046|
| 11 | TensorFlow Custom logs | Расширенные логи модели 10 дня. В ноутбуке лежит код запуска просмотра логов в TensorBoard|

## 📂 Структура
week1-day1-2/ # ноутбук + графики

week1-day3/   # pipeline + gridsearch

week1-day4/   # imbalance + smote

week1-day5/   # Linear Regression

week1-day6-7/   # PostgreSQL + Prophet + FastAPI

week2-day8-9/   #PyTorch Mnist dataset

week2-day10/   #TensorFlow CNN Cifar10

week2-day11/   #TensorFlow Сustom los
