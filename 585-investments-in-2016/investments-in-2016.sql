# Write your MySQL query statement below
SELECT round(sum(tiv_2016),2) AS tiv_2016
FROM insurance
WHERE tiv_2015 IN (
  SELECT tiv_2015
  FROM insurance
  GROUP BY tiv_2015
  having count(*)>1
) AND
(lat,lon) IN (
  SELECT lat,lon FROM
  insurance
  group BY lat, lon
  having count(*) = 1
)