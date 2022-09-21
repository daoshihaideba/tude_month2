
--聚合函数作为展示内容放在select 后
select avg(attack) as 平均攻击力 from sanguo;

--select 后写的是聚合函数的时候，不适合写其他普通字段
--除非这个字段的值是一致的
select country,avg(attack) as 平均攻击力 from sanguo
where country="蜀";

--select 后可以同时使用多个聚合函数
select country,max(attack) as 最大攻击力,min(attack) as 最小攻击力
from sanguo
where country="蜀";

--统计计数： 统计字段时不会统计null   count(*)可以表示统计记录条数
select country,count(*) from sanguo
where country="蜀";


分组 : 字段值相同的作为一组
分组时按照什么字段分，就查询什么字段。可以同时分组进行聚合函数统计
select country,avg(attack) from sanguo group by country;

如果按照主键分组则可以写其他字段
select id,country  from sanguo group by id;

每个国家男英雄最高攻击力
select country,max(attack)  from sanguo
where gender="男" group by country;

所有国家中男性英雄防御力之和最高的国家 ：  国家  防御力之和
select country,sum(defense)
from sanguo
where gender = '男'
group by country
order by sum(defense) desc
limit 1;

--按照多个字段分组
select country,gender,count(*) from sanguo
group by country,gender;

聚合筛选
select country,avg(attack) from sanguo
where gender="男"
group by country
having avg(attack) >= 300;

去重 : 去除查询结果中重复的显示
select distinct country from sanguo;
select count(distinct country) from sanguo;





