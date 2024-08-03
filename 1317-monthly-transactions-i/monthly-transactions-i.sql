# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') as 'month',
		t.country,
		count(*) as trans_count,
		count(case when t.state = 'approved' then 1 end) as approved_count ,
        sum(t.amount) as trans_total_amount,
        sum(case when t.state = 'approved' then t.amount else 0 end) as approved_total_amount
FROM transactions t
GROUP BY DATE_FORMAT(t.trans_date, '%Y-%m'), t.country;