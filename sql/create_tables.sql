CREATE TABLE IF NOT EXISTS public.transactions (
    transaction_id BIGINT PRIMARY KEY,
    user_id BIGINT,
    product_id BIGINT,
    category VARCHAR(50),
    quantity INTEGER,
    price NUMERIC(10,2),
    timestamp TIMESTAMP,
    region VARCHAR(50)
);