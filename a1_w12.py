'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210407]                                   ##
#*******************************************************************************************#
#############################################################################################
'''

import psycopg2

# (M:Manuel olarak, K:SQL komutlariyla, C:Python kodlariyla)

# Asagidaki sorulardan K ve C ile cozulmesini istediklerimizin cozumlerini (komut veya kodlarini) ustte sorusu altta cozumu 
# olacak sekilde bir dosyaya yapistirip gondermenizi istiyoruz.

# 1- 'pycoders' isimli bir server kurun. (M)

# 2- 'class4' database olusturun (M). Database silin (M). Ayni database yine olusturun (K)
CREATE Database class4

# 3- https://www.postgresqltutorial.com/postgresql-sample-database/ adresine gidin ve ER modeli inceleyin. 
# Tablolar arasindaki en az 5 iliskiyi yazin.(Hangi tablolar arasinda ne tur bir iliski var)
country table da her country,               birden cok city ye sahip olabilir.              Yani one-to-many iliskisi.
city table da her city,                     birden cok address e sahip olabilir.            Yani one-to-many iliskisi.
actor table i olan herkisinin,              bir film_aktor table i vardir.                  Yani one-to-one iliskisi.
film table da herfilm,                      birden cok inventory ye sahip olabilir.         Yani one-to-many iliskisi.
her customer birden cok payment yapabilir,  her payment birden cok rental icin olabilir.    Yani many-to-many iliskisi.

# 4- ER modeldeki tablolardan 3 tanesini M olusturun.

# 5- ER modeldeki tablolardan 3 tanesini K olusturun.
CREATE TABLE City (
    city_id int NOT NULL PRIMARY KEY,
    city character varying(50) NOT NULL,
    country_id smallint NOT NULL,
    last_update timestamp without time zone NOT NULL,
        CONSTRAINT City
        FOREIGN KEY (country_id)
        REFERENCES Country (country_id)          
)
CREATE TABLE Country (
    country_id integer NOT NULL PRIMARY KEY,
    country character varying(50) NOT NULL,
    last_update timestamp without time zone NOT NULL        
)
CREATE TABLE Actor (
    actor_id integer NOT NULL PRIMARY KEY,
    first_name character varying(45),
    last_name character varying(45),
    last_update timestamp without time zone NOT NULL
)

# 6- ER modeldeki tablolardan 3 tanesini C olusturun.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()

command2 = '''CREATE TABLE Country (
    country_id integer NOT NULL PRIMARY KEY,
    country character varying(50) NOT NULL,
    last_update timestamp without time zone NOT NULL
)
'''
cur.execute(command2)

command1 = '''CREATE TABLE City (
    city_id int NOT NULL PRIMARY KEY,
    city character varying(50) NOT NULL,
    country_id smallint NOT NULL,
    last_update timestamp without time zone NOT NULL,
        CONSTRAINT City
        FOREIGN KEY (country_id)
        REFERENCES Country (country_id)
)
'''
cur.execute(command1)

command3 = '''CREATE TABLE Actor (
    actor_id integer NOT NULL PRIMARY KEY,
    first_name character varying(45),
    last_name character varying(45),
    last_update timestamp without time zone NOT NULL
)
'''
cur.execute(command3)

cur.close()
conn.commit()
conn.close()
# (4-5-6. sorulari cozerken toblolar arasindaki iliskileri gozardi edebilirsiniz. 
# Tum kolonlari girmek zorunda degilsiniz, en az 2 kolon olmasi yeterli.)

# 7- Olusturdugunuz 3 tabloya M ile 5 veri girisi yapin.

# 8- Olusturdugunuz 3 tabloya K ile 5 veri girisi yapin.
insert into actor(actor_id,first_name,last_name,last_update) values (1,'morgan','freeman','2021-04-06 06:30:30')
insert into actor(actor_id,first_name,last_name,last_update) values (2,'jim','carry','2021-04-06 06:30:30')
insert into actor(actor_id,first_name,last_name,last_update) values (3,'julia','roberts','2021-04-06 06:30:30')
insert into actor(actor_id,first_name,last_name,last_update) values (4,'bruce','lee','2021-04-06 06:30:30')
insert into actor(actor_id,first_name,last_name,last_update) values (5,'tom','hanks','2021-04-06 06:30:30')

insert into country(country_id, country, last_update) values (1,'NL','2021-04-06 06:30:30')
insert into country(country_id, country, last_update) values (2,'DE','2021-04-06 06:30:30')
insert into country(country_id, country, last_update) values (3,'FR','2021-04-06 06:30:30')
insert into country(country_id, country, last_update) values (4,'BE','2021-04-06 06:30:30')
insert into country(country_id, country, last_update) values (5,'TR','2021-04-06 06:30:30')

insert into city(city_id, city, country_id,last_update) values (1,'AMS',1,'2021-04-06 06:30:30')
insert into city(city_id, city, country_id,last_update) values (2,'FRA',2,'2021-04-06 06:30:30')
insert into city(city_id, city, country_id,last_update) values (3,'ATN',3,'2021-04-06 06:30:30')
insert into city(city_id, city, country_id,last_update) values (4,'MAD',4,'2021-04-06 06:30:30')
insert into city(city_id, city, country_id,last_update) values (5,'IST',5,'2021-04-06 06:30:30')

# 9- Olusturdugunuz 3 tabloya C ile 5 veri girisi yapin.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()
 
cur.execute("INSERT INTO country VALUES (%s, %s, %s)", (1,'NederL','2021-04-06 06:30:30'))
cur.execute("INSERT INTO country VALUES (%s, %s, %s)", (2,'DEuctschland','2021-04-06 06:30:30'))
cur.execute("INSERT INTO country VALUES (%s, %s, %s)", (3,'FRance','2021-04-06 06:30:30'))
cur.execute("INSERT INTO country VALUES (%s, %s, %s)", (4,'BElgie','2021-04-06 06:30:30'))
cur.execute("INSERT INTO country VALUES (%s, %s, %s)", (5,'TuRiye','2021-04-06 06:30:30'))

cur.execute("INSERT INTO city VALUES (%s, %s, %s,%s)", (1,'AMS',1,'2021-04-06 06:30:30'))
cur.execute("INSERT INTO city VALUES (%s, %s, %s,%s)", (2,'FRAnkfurt',2,'2021-04-06 06:30:30'))
cur.execute("INSERT INTO city VALUES (%s, %s, %s,%s)", (3,'ATiNa',3,'2021-04-06 06:30:30'))
cur.execute("INSERT INTO city VALUES (%s, %s, %s,%s)", (4,'MADrid',4,'2021-04-06 06:30:30'))
cur.execute("INSERT INTO city VALUES (%s, %s, %s,%s)", (5,'ISTanbul',5,'2021-04-06 06:30:30'))
 
cur.execute("INSERT INTO actor VALUES (%s, %s, %s,%s)", (1,'morgan','freemann','2021-04-06 06:30:30'))
cur.execute("INSERT INTO actor VALUES (%s, %s, %s,%s)", (2,'jim-','carry','2021-04-06 06:30:30'))
cur.execute("INSERT INTO actor VALUES (%s, %s, %s,%s)", (3,'julia-','roberts','2021-04-06 06:30:30'))
cur.execute("INSERT INTO actor VALUES (%s, %s, %s,%s)", (4,'bruce-','lee','2021-04-06 06:30:30'))
cur.execute("INSERT INTO actor VALUES (%s, %s, %s,%s)", (5,'tom-','hanks','2021-04-06 06:30:30'))

cur.close()
conn.commit()
conn.close()
# 10- 3 tablodaki birer veriyi M ile degistirin.

# 11- 3 tablodaki birer veriyi K ile degistirin.
UPDATE actor set last_name='HANKS' where actor_id=5
UPDATE city set city='ANK' where city_id=5
UPDATE country set country='TUR' where country_id=5

# 12- 3 tablodaki birer veriyi C ile degistirin.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()

cur.execute("UPDATE country SET country=%s WHERE country_id=%s", ('congo',4))
cur.execute("UPDATE city SET city=%s WHERE city_id=%s", ('tokyo',4))
cur.execute("UPDATE actor SET last_name=%s WHERE actor_id=%s", ('John',4))

cur.close()
conn.commit()
conn.close()
# 13- 3 tablonun son satirini M ile silin.

# 14- 3 tablonun son satirini K ile silin.
delete from actor where actor_id = 5
delete from city where city_id = 5
delete from country where country_id = 5

# 15- 3 tablonun son satirini C ile silin.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()

cur.execute("DELETE FROM actor WHERE actor_id = %s", (5,))
cur.execute("DELETE FROM city WHERE city_id = %s", (5,))
cur.execute("DELETE FROM country WHERE country_id = %s", (5,))

cur.close()
conn.commit()
conn.close()
# 16- 1 tabloyu M ile silin.

# 17- 1 tabloyu K ile silin.
DROP TABLE city

# # 18- 1 tabloyu C ile silin.
conn = psycopg2.connect("dbname = class4 user = postgres password = abc123 ")
cur = conn.cursor()

cur.execute("DROP TABLE city")
cur.close()
conn.commit()
conn.close()

# 19- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu K ile baska bir tablo olarak olusturun.
CREATE TABLE actor_new1 AS SELECT first_name,last_name FROM actor

# 20- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu C ile baska bir tablo olarak olusturun.
conn = psycopg2.connect("dbname = class4 user = postgres password = abc123 ")
cur = conn.cursor()

cur.execute("CREATE TABLE actor_new2 AS SELECT first_name,last_name,last_update FROM actor")
cur.close()
conn.commit()
conn.close()

# 21- Tablolardan 1 tanesini M ile truncate edin.

# 22- Tablolardan 1 tanesini K ile truncate edin.
TRUNCATE TABLE actor

# 23- Tablolardan 1 tanesini C ile truncate edin.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()

cur.execute("TRUNCATE TABLE city")

cur.close()
conn.commit()
conn.close()
# 24- Truncate edilmis tablolari M ile silin.

# 25- 2 tabloyu K ile silin.
DROP TABLE country
DROP TABLE city

# 26- 2 tabloyu C ile silin.
conn = psycopg2.connect("dbname = class4 user = postgres password = Fsm1453. ")
cur = conn.cursor()

cur.execute("DROP TABLE country, city")

cur.close()
conn.commit()
conn.close()

# 27- Elimizde veri olan 1 tablo kalmis olmasi lazim. Bu tabloyu csv olarak bilgisayariniza yukleyin.

# 28- Postgresql arayuzundeki son tabloyu da K ile silin.
DROP TABLE actor
# 29- Bilgisayarinizdaki csv yi arayuze import edin.

# 30- Import ettiginiz bu tabloyu C ile silin.

# 31- https://www.postgresqltutorial.com/postgresql-sample-database/ linkindeki ornek DB yi bilgisayariniza indirin ve arayuze yukleyin.

# 32- DB nizde 15 adet tablo olmasi lazim. Her tabloyu teker teker goruntuleyin ve kolon isimlerine bakarak, 
# 5 tabloda hangi kolonun PK ve FK oldugunu yazin.
address table:  PK=address_id   FK=city_id
city table:     PK=city_id      FK=country_id
customer table: PK=customer_id  FK=store_id
payment table:  PK=payment_id   FK=customer_id
rental table:   PK=rental_id    FK=inventory_id

# Sorgular? (Asagidaki sorularin cevaplarini ve bu cevabi bulurken kullandiginiz kodlari yazin)

# 33- Action filmlerinin ortalama suresi ne kadar?
select avg(length) from film where film_id in (select film_id from film_category where category_id=1)
# 34- En cok staff olan store hangisidir?

# 35- 'Gene Willis' adli actorun oynadigi filmlerin ratingi nedir?
select rating from film where film_id in (select film_id from film_actor where actor_id = (select actor_id from actor where first_name='Gene' and last_name='Willis' ))

# 36- Aktif customer sayisi nedir?
select count(*) from customer where active=1

# 37- 'C' harfiyle baslayan filmler hangileridir?
select * from film where title like 'C%'

# 38- 4$ den az odeme yapan musterilerin e-mail edresleri nedir?
select email from customer where customer_id in (select customer_id from payment where amount<4 )

# 39- Moscow'da ikamet eden staff ve customer tablosu? (sadece isim/soyisim sutunu olsun)
select first_name, last_name from staff where address_id in (select address_id from address where district like 'Mos%') union select first_name, last_name from customer where address_id in (select address_id from address where district like 'Mos%')

# 40- En az kiralanan 5 film hangisidir?
create table new as select inventory.inventory_id, inventory.film_id, rental.rental_id from inventory right join rental on inventory.inventory_id=rental.inventory_id 
select film_id, count(inventory_id) from new group by film_id  order by count(film_id) asc limit 5

# 41- 2006 yilinda yayinlanan ingilizce filmler hangileridir?
select title from film where release_year=2006 and language_id in (select language_id from language where name='English')