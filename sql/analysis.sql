-- E-Commerce Sales Analysis
-- 1. Total sales
SELECT ROUND(SUM(sales), 2) AS total_sales FROM sales;

-- 2. Total profit
SELECT ROUND(SUM(profit), 2) AS total_profit FROM sales;

-- 3. Monthly sales
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       ROUND(SUM(sales),2) AS sales
FROM sales
GROUP BY month
ORDER BY month;

-- 4. Best categories
SELECT category, ROUND(SUM(sales),2) AS sales
FROM sales GROUP BY category ORDER BY sales DESC;

-- 5. Top 10 products
SELECT product, ROUND(SUM(sales),2) AS sales
FROM sales GROUP BY product ORDER BY sales DESC LIMIT 10;

-- 6. Regional performance
SELECT region, ROUND(SUM(sales),2) AS sales,
       ROUND(SUM(profit),2) AS profit
FROM sales GROUP BY region ORDER BY sales DESC;

-- 7. Average order value
SELECT ROUND(SUM(sales)/COUNT(DISTINCT order_id),2) AS avg_order_value
FROM sales;

-- 8. Top customers
SELECT customer_id, ROUND(SUM(sales),2) AS lifetime_sales
FROM sales GROUP BY customer_id ORDER BY lifetime_sales DESC LIMIT 10;
