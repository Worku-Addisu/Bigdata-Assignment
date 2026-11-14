
-- 1. Count total transactions
SELECT COUNT(*)
FROM public.transactions;

-- 2. Sales by category
SELECT
    category,
    SUM(quantity * price) AS total_sales
FROM public.transactions
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Transactions by region
SELECT
    region,
    COUNT(*) AS total_transactions
FROM public.transactions
GROUP BY region
ORDER BY total_transactions DESC;

-- 4. Average product price
SELECT AVG(price) AS average_price
FROM public.transactions;
