code='''sql SELECT 
    p.product_id,
    p.product_name,
    p.product_price,
    SUM(o.order_quantity) AS total_quantity_sold
FROM products AS p
INNER JOIN orders AS o ON p.product_id = o.product_id
GROUP BY p.product_id, p.product_name, p.product_price
ORDER BY total_quantity_sold DESC
LIMIT 10;
'''

print(code[4:])