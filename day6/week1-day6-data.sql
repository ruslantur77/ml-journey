-- Day 5: создание таблицы и загрузка данных
CREATE TABLE sales (
    date DATE,
    item_id INT,
    qty INT
);

COPY sales FROM '/tmp/sales.csv' CSV HEADER;

-- quick check
SELECT date, SUM(qty) AS total_qty
FROM sales
GROUP BY date
ORDER BY date
LIMIT 5;
