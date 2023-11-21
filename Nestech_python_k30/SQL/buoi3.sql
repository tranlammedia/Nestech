use k30_final;
show tables;

select * from sales_target;
select * from list_of_orders;
select * from order_details;

select * from order_details
where `Order ID` IN (
	select `Order ID` from order_details
	group by `Order ID`
	having count(*) > 1
);

ALTER TABLE order_details
	ADD ID INT AUTO_INCREMENT,
	ADD PRIMARY KEY(ID);

SELECT st.*
FROM sales_target st
INNER JOIN (
    SELECT `Month of Order Date` AS month, MAX(Target) AS max_sales
    FROM sales_target
    GROUP BY `Month of Order Date`
) AS t
ON st.`Month of Order Date` = t.month AND st.Target = t.max_sales;

select * 
from (
	select *,
    rank() over (partition by `Month of Order Date` order by Target desc) as Top
	from sales_target
	order by `Month of Order Date` asc
) as t1
-- order by `Month of Order Date`, top
where top =1;

SELECT st.Month, Category, (Amount*Quantity) + (Profit*Quantity) AS total_amount
FROM order_details AS od
INNER JOIN
	(
	SELECT `Month of Order Date` AS Month, `Category` AS Cat, MAX(Target) AS Target
	FROM sales_target AS st
	GROUP BY Month, Cat
	ORDER BY target DESC
	) AS st
ON od.Category = st.Cat    
GROUP BY st.Month, Category, total_amount
ORDER BY total_amount DESC;

UPDATE `sales_target`
SET `Month of Order Date` = str_to_date(CONCAT('01-',`Month of Order Date`), '%d-%b-%y');

UPDATE list_of_orders
SET `Order Date` = STR_TO_DATE(`Order Date`, '%d-%m-%Y')
WHERE `Order ID` IS NOT NULL;


SELECT STR_TO_DATE(s.`Order Date`, '%d-%m-%Y') From 
(select `Order Date` from list_of_orders
where `Order Date` = '01-04-2018') as s;

SELECT *, str_to_date(CONCAT('01-',`Month of Order Date`), '%d-%b-%y') as date
From sales_target;

select cast(`Month of Order Date` as Date) as date 
from sales_target;

SELECT *, STR_TO_DATE(`Order Date`, '%d-%m-%Y') as date
From list_of_orders;

SELECT str_to_date('01-04-2018','%d-%m-%Y');

-- Xay customerID
With list_of_orders_new (`Order ID`,date, customerid) as ( 
	SELECT `Order ID`,
			STR_TO_DATE(`Order Date`, '%d-%m-%Y') as date, 
			concat_ws("",CustomerName,REPLACE(State,' ',''),City) as customerid
	FROM list_of_orders
)
SELECT *
FROM list_of_orders_new;
-- 'SakshiMadhyaPradesh', 'Bhopal'
-- 'SakshiMadhyaPradesh', 'Indore'

-- Lan cuoi khach hang den
With list_of_orders_new (`Order ID`,date, customerid) as ( 
	SELECT `Order ID`,
			STR_TO_DATE(`Order Date`, '%d-%m-%Y') as date, 
			concat_ws("",CustomerName,REPLACE(State,' ',''),City) as customerid
	FROM list_of_orders
)
SELECT customerid, MAX(date) as last_date
FROM list_of_orders_new
GROUP BY customerid;

-- tim so lan khach da den
With list_of_orders_new (`Order ID`,date, customerid) as ( 
	SELECT `Order ID`,
			STR_TO_DATE(`Order Date`, '%d-%m-%Y') as date, 
			concat_ws("",CustomerName,REPLACE(State,' ',''),City) as customerid
	FROM list_of_orders
)
SELECT customerid, COUNT(*) as frequency
FROM list_of_orders_new
GROUP BY customerid;

-- So tien khach da chi
With list_of_orders_new (`Order ID`,date, customerid) as ( 
	SELECT `Order ID`,
			STR_TO_DATE(`Order Date`, '%d-%m-%Y') as date, 
			concat_ws("",CustomerName,REPLACE(State,' ',''),City) as customerid
	FROM list_of_orders
)
SELECT customerid, SUM(d.Amount * d.Quantity) as Total
FROM list_of_orders_new as o
LEFT JOIN order_details as d
ON o.`Order ID` = d.`Order ID`
GROUP BY o.customerid;
