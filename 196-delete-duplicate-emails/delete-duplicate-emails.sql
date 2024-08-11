# Write your MySQL query statement below
delete FROM person
where id not IN 
(
  SELECT dup from(
      SELECT min(id) AS dup FROM person p
      GROUP by email
      ) t
    );