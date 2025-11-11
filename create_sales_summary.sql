-- Aggregate monthly sales per region
SELECT
  month,
  region,
  SUM(total_amount) AS total_sales,
  COUNT(DISTINCT customer) AS unique_customers
INTO sales_summary
FROM sales_cleaned
GROUP BY month, region
ORDER BY month, region;
