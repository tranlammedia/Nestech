use world;

select *  from country
left join countrylanguage
on country.code = countrylanguage.countrycode;

select * from country
where Name ='Vietnam';
select * from countrylanguage;

SELECT *
FROM countrylanguage AS t
INNER JOIN countrylanguage AS t1 ON t.CountryCode = t1.CountryCode
INNER JOIN countrylanguage AS t2 ON t.CountryCode = t2.CountryCode
WHERE t.countrycode = 'ABW';
-- WHERE t1.Language = 'French'
--   AND t2.Language = 'English'
--   AND t.Language = 'Dutch';

-- 1.Việt Nam đang sử dụng bao nhiêu ngôn ngữ (chính thức lẫn không chính thức-- 
select count(*) FROM countrylanguage
WHERE countrycode = 'VNM';
-- 2. VN sẽ có khả năng giao tiếp với những quốc gia nào
select distinct countrycode from countrylanguage 
WHERE language in (select language FROM countrylanguage
WHERE countrycode = 'VNM') and countrycode not LIKE 'VNM';
-- 3. có bao nhiêu quốc gia và dân số mà người VN ko thể giao tiếp trực tiếp được 

select SUM(t1.population)
from city as t1
right join (
	select distinct countrycode
    from countrylanguage 
	WHERE language not in (	
		select language 
        FROM countrylanguage
		WHERE countrycode = 'VNM'
	)
) as t2
on t1.countrycode =  t2.countrycode;

select SUM(t1.population) from city as t1
WHERE t1.countrycode IN (select distinct countrycode from countrylanguage 
						WHERE language not in (select language FROM countrylanguage
												WHERE countrycode = 'VNM') );

-- ======= BT buoi 2 ======
-- Cau 1a: 5 ngôn ngữ được dùng nhiều nhất trên thế giới, tiêu chí 1. số lượng quốc gia 

select Language,count(*) as quantity from countrylanguage
group by Language
order by quantity DESC
LIMIT 5;

-- Cau 1b: 5 ngôn ngữ được dùng nhiều nhất trên thế giới, tiêu chí 2. số lượng dan so (it nhat 2 nuoc tro len su dung)
select language, sum(population) as total_population 
from country as t1
right join (
	select countrycode, language
    from countrylanguage
	where language in (
		select language 
		from countrylanguage
		group by language
		having count(*) >=15
	)
) as t2
on t1.code = t2.countrycode
group by language
order by total_population DESC
LIMIT 5;

select s2.Language, s2.sum_Population
FROM (
	select s1.Language, sum(s1.Population) as sum_Population
	FROM (
		select cl.Language, c.Population
		from countrylanguage as cl
		inner join country as c 
        on cl.CountryCode = c.Code
	) as s1 -- tuong quan Language va Population theo tung country
	GROUP BY s1.Language
	order by sum_Population desc
) as s2 -- tuong quan Language va sum_Population
WHERE s2.Language in (
	select Language
	FROM countrylanguage
	GROUP BY Language
	HAVING COUNT(CountryCode) >= 2
) -- Language co > 2 nuoc dung
LIMIT 5;

-- câu 2. tìm top 5 quốc gia có LifeExpectancy và GNP cao nhất

SELECT *
FROM (
	SELECT Name, LifeExpectancy, GNP
	FROM country
	ORDER BY LifeExpectancy DESC
	LIMIT 5
) as GNP
UNION (
	SELECT Name, LifeExpectancy, GNP
	FROM country
	ORDER BY GNP DESC
	LIMIT 5
);

SELECT code,  LifeExpectancy, GNP, (tyle_gnp + tyle_life) as tyle_total 
FROM (
	SELECT code, 
			LifeExpectancy,
            GNP, 
			(GNP /(SELECT max(GNP) FROM country)) as tyle_gnp, 
			(LifeExpectancy / (SELECT max(LifeExpectancy) FROM country)) as tyle_life
	FROM country) as c1
order by tyle_total DESC
LIMIT 5;

-- câu 3. ngôn ngữ có tiềm năng trở thành phổ biến: thuộc top 5 GN, quốc gia sử dụng ngôn ngữ đó làm ngôn ngữ chinh, số quốc gia đang sử dụng ngôn ngữ đó trên thế giới < 5

-- b3: lay country dung 4 tieng tren
SELECT cl.language, count(cl.countrycode) AS quantity 
FROM countrylanguage AS cl
WHERE cl.language IN (
	-- b2: lay language chi'nh cua top 5 GNP => 'English' 'Japanese' 'German' 'French'
	SELECT distinct language
	FROM countrylanguage as cl_lg
	WHERE cl_lg.countrycode IN (
		-- b1: lay country cua top 5 GNP
		SELECT c_top.code 
		FROM (
			SELECT c.code 
			FROM country c
			ORDER BY c.GNP DESC
			LIMIT 20
		) AS c_top
	) AND cl_lg.isofficial = 'T'
)
-- b4 lay language co country < 5
GROUP BY cl.language
HAVING quantity < 5;