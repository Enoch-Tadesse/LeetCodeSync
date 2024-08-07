WITH aggr
AS
(SELECT
    visited_on,
    SUM(amount) AS amount
  FROM customer
  GROUP BY visited_on),
final
AS
(SELECT
    visited_on,
    SUM(amount) OVER w AS amount,
    AVG(amount) OVER w AS average_amount,
    ROW_NUMBER() OVER w AS rn
  FROM aggr
  WINDOW w AS (
  ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW))

SELECT
  visited_on,
  amount,
  ROUND(average_amount, 2) AS average_amount
FROM final
WHERE rn >= 7;