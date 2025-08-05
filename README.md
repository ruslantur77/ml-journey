# ml-journey  
4-недельный путь от нуля до продакшена в Data Science / ML.

## ✅ Проекты за первую неделю

| День | Название | Что сделано |
|---|---|---|
| **1–2** | Wine Bias–Variance Demo | На датасете Wine Quality сравннение деревья разной глубины и построение графика «train vs test error», чтобы наглядно увидеть bias и variance. |
| **3** | Wine Pipeline & GridSearch | Собран sklearn Pipeline (StandardScaler → RandomForest) и подобран `max_depth` + `n_estimators` через GridSearchCV; лучший F1 ≈ 0.41. |
| **4** | Imbalance & SMOTE | Сгенерирован синтетический датасет (95 % «0», 5 % «1»). Применен SMOTE, поднят recall c 6 % до 31 % и F1 до 0.37, показав как бороться с дисбалансом. |

## 📂 Структура
week1-day1/   # ноутбук + графики

week1-day3/   # pipeline + gridsearch

week1-day4/   # imbalance + smote
