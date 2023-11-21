SHOW DATABASEs;
USE world;
--  --  1. 5 ngôn ngữ được dùng nhiều nhất trên thế giới
-- -- 1.1 tiêu chí 1. số lượng quốc gia dùng top 5 nhiều ít
select Language,
    COUNT(CountryCode) as Num_CTry
FROM countrylanguage
GROUP BY Language
ORDER BY Num_CTry DESC
limit 5;
-- -- 1.2 tiêu chí 2. theo dân số, top 5 từ nhiều tới ít
select s2.Language,
    s2.sum_Population
FROM (
        select s1.Language,
            sum(s1.Population) as sum_Population
        FROM (
                select cl.Language,
                    c.Population
                from countrylanguage as cl
                    inner join country as c on cl.CountryCode = c.Code
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
-- -- 1.2.ct: ngon ngu co 2 nuoc tro len dung
select Language,
    COUNT(CountryCode)
FROM countrylanguage
GROUP BY Language
HAVING COUNT(CountryCode) >= 2;
-- -- câu 2. tìm top 5 quốc gia có LifeExpectancy và GNP cao nhất
-- -- câu 2.cach 1
SELECT Code,
    LifeExpectancy,
    GNP
FROM (
        select tb1.Code,
            tb1.LifeExpectancy,
            tb1.GNp
        from (
                select Code,
                    LifeExpectancy,
                    GNP
                FROM country
                ORDER BY LifeExpectancy DESC
                LIMIT 5 
            ) as tb1 -- xep thu tu country co LifeExpectancy  cao nhat
    ) as tb11 -- 5 country co LifeExpectancy cao nhat
UNION all
SELECT Code,
    LifeExpectancy,
    GNP
FROM (
        select tb2.Code,
            tb2.LifeExpectancy,
            tb2.GNP
        from (
                select Code,
                    LifeExpectancy,
                    GNP
                FROM country
                ORDER BY GNP desc
                LIMIT 5
            ) as tb2  -- xep thu tu country co GNP  cao nhat
    ) as tb22 -- 5 country co GNP  cao nhat
    ;
-- -- câu 2. cach 2
select Code,
    LifeExpectancy,
    GNP
from country
WHERE Code in (
        select tb1.Code
        from (
                select Code,
                    LifeExpectancy
                FROM country
                ORDER BY LifeExpectancy DESC
                LIMIT 5
            ) as tb1
    )
    or Code in (
        select tb2.Code
        from (
                select Code,
                    GNP
                FROM country
                ORDER BY GNP desc
                LIMIT 5
            ) as tb2
    )
ORDER BY LifeExpectancy DESC;
-- -- tiêu chí 3 : đánh giá ngôn ngữ có tiềm năng trở thành phổ biến
-- -- ngôn ngữ có tiềm năng trở thành phổ biến, quốc gia sử dụng ngôn ngữ đó làm ngôn ngữ chính, thuộc top 5 GNP
-- -- số quốc gia đang sử dụng ngôn ngữ đó trên thế giới < 5
select language,
  CountryCode,
  IsOfficial,
  GNP
FROM (
    select language,
      CountryCode,
      IsOfficial,
      c.GNP
    from countrylanguage as cl
      left join country as c on cl.CountryCode = c.Code
  ) AS TBA
WHERE TBA.CountryCode in (
    select tbb.Code
    from (
        select Code,
          GNP
        FROM country
        ORDER BY GNP DESC
        LIMIT 5
      ) as tbb -- 5 country co GNP cao nhat
  )
    AND TBA.IsOfficial in ('T')
    AND TBA.Language in (
      select Language
      from countrylanguage 
      group by Language
      having  count(CountryCode) <5
    ) -- language co it hon 5 country use
  ;