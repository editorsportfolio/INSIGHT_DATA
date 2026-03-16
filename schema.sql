-- InsightOps Advanced Database Schema

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS regions;
DROP TABLE IF EXISTS sales;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT
);

CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT,
    region_name TEXT NOT NULL
);

CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    region_id INTEGER,
    quantity INTEGER,
    price REAL,
    sale_date DATE,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(region_id) REFERENCES regions(region_id)
);

INSERT INTO products (product_name, category) VALUES
('Laptop','Electronics'),
('Phone','Electronics'),
('Tablet','Electronics'),
('Headphones','Accessories');

INSERT INTO regions (region_name) VALUES
('North'),
('South'),
('East'),
('West');

INSERT INTO sales (product_id, region_id, quantity, price, sale_date) VALUES
(1,1,5,800,'2026-01-01'),
(2,2,8,500,'2026-01-02'),
(3,3,6,300,'2026-01-03'),
(1,4,3,800,'2026-01-04'),
(2,1,10,500,'2026-01-05'),
(4,2,12,100,'2026-01-06'),
(3,4,4,300,'2026-01-07'),
(1,3,2,800,'2026-01-08');