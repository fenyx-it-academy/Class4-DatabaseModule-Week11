"""2.soru
create databates class_4 """
"""5.soru:
create table rentall
(
    rental_id integer primary key NOT NULL,
    rental_date integer NOT NULL,
	inventory_id integer NOT NULL,
	customer_id integer NOT NULL,
	return_date integer NOT NULL,
	staff_id integer NOT NULL,
	last_update integer NOT NULL,
);

create table payment
(
payment_id integer primary key not null,
	customer_id integer,
	staff_id integer,
	rental_id integer,
	amount integer,
	payment_date integer);
create table language
(
language_id integer primary key not null,
	name integer ,
	last_update integer
	);
"""

"""6.soru"""
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
command = '''create table actor
(
    actor_id integer primary key ,
    first_name varchar(15) NOT NULL,
    last_name varchar(10) NOT NULL,
    last_update integer
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()


import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
command = '''create table store
(
    store_id integer primary key ,
    manager_staff_id integer NOT NULL,
    adress_id integer NOT NULL,
    last_update integer
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
command = '''create table city
(
    city_id integer primary key ,
    city integer NOT NULL,
    country_id integer NOT NULL,
    last_update integer
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()

"""8.soru
insert into category(category_id,name,last_update) values(1,'action',2006)
insert into category(category_id,name,last_update) values(2,'comedy',2006)
insert into category(category_id,name,last_update) values(3,'drama',2006)
insert into category(category_id,name,last_update) values(4,'documantary',2006)
insert into category(category_id,name,last_update) values(5,'family',2006)"""

"""9.soru"""
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute('insert into city values(%s,%s,%s,%s)',(1,35,2003,'İzmir'))
cur.close()
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute('insert into city values(%s,%s,%s,%s)',(2,34,2003,'İstanbul'))
cur.close()
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute('insert into language values(%s,%s,%s)',(1,2003,'english'))
cur.close()
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute('insert into language values(%s,%s,%s)',(2,2003,'german'))
cur.close()
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute('insert into film_category values(%s,%s,%s)',(1,23,2006))
cur.close()
conn.commit()
conn.close()
"""11.soru
UPDATE category set  name='science fiction' where category_id=2
UPDATE city set city='ısparta' where city_id=2
UPDATE language set name='french' where language_id=1   """

"12.soru"
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute("update city set city=%s where city_id=%s", ('aydın',1))
cur.execute("update category set name=%s where category_id=%s", ('horror',1))
cur.execute("update language set name=%s where language_id=%s", ('italian',2))
cur.close()
conn.commit()
conn.close()

"""14.soru
delete from category where category_id=2
delete from city where city_id=1
delete from language where language_id=3 """

"""15.soru"""
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute("delete from category where category_id=%s ", (1,))
cur.execute("delete from city where city_id=%s ", (2,))
cur.execute("delete from language where language_id=%s ", (1,))
cur.close()
conn.commit()
conn.close()

"""17.soru
drop table actor"""

"""18.soru"""
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute("drop table inventory")
cur.close()
conn.commit()
conn.close()

"""22.soru
truncate table language"""

"""23.soru"""
import psycopg2
conn = psycopg2.connect("dbname=class_4 user=postgres password=F96f96f96 port=2529")
cur = conn.cursor()
cur.execute("truncate table payment")
cur.close()
conn.commit()
conn.close()
"""33.soru
select avg(length) from film where film_id in (select film_id from film_category where category_id=1)
answer=111.6093750000000000"""

"""37.soru
select * from film where title like 'C%'
"""

"""41.soru
select title from film where release_year=2006 and language_id in (select language_id from language where name='English')"""