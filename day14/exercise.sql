班级   学生  1  多
老师   课程  1  多
学生   课程  多  多 -> 分数

查询综合
1. 查询每位老师教授的课程数量
select teacher.tname,count(cname) from teacher
left join course
on teacher.tid=course.teacher_id
group by teacher.tname;

2. 查询各科成绩最高和最低的分数,形式 : 课程ID  课程名称 最高分  最低分
select cid as 课程ID,cname as 课程名称,
max(number) as 最高分,min(number) as 最低分
from course left join score
on course.cid = score.course_id
group by cid;

3. 查询平均成绩大于85分的所有学生学号,姓名和平均成绩
select student.sid,student.sname,avg(number)
from student inner join score
on student.sid = score.student_id
group by student.sid,student.sname
having avg(number) > 85;

4. 查询课程编号为2且课程成绩在80以上的学生学号和姓名
select student.sid,student.sname
from student inner join score
on student.sid = score.student_id
where course_id=2 and number > 80;

5. 查询各个课程及相应的选修人数
select cname,count(course_id)
from course left join score
on course.cid = score.course_id
group by cname;

6. 查询每位学生的姓名，所在班级和各科平均成绩

select student.sname,class.caption,avg(number) from class
left join student on class.cid = student.class_id
left join score on student.sid = score.student_id
group by student.sname,class.caption;

