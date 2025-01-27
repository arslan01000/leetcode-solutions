SELECT 
    p.product_name,
    s.year,
    s.price
FROM 
    Sales s
JOIN 
    Product p
ON 
    s.product_id = p.product_id;

-- Problem: Retrieve product name, year, and price for each sale in the Sales table
-- Link: https://leetcode.com/problems/product-sales-analysis-i
