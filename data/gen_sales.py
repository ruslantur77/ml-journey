import pandas as pd, numpy as np, datetime as dt
np.random.seed(42)

dates = pd.date_range('2023-01-01', '2023-12-31')
items = [1, 2, 3]
rows = []

for d in dates:
    for i in items:
        # простая сезонность + случайность
        base = 10 + 5*np.sin(2*np.pi*d.dayofyear/365)
        qty  = max(0, int(base + np.random.poisson(3)))
        rows.append((d.date(), i, qty))

pd.DataFrame(rows, columns=['date','item_id','qty']).to_csv('data/sales.csv', index=False)