'''
Author=Bulent Caliskan date=07/04/2021
'''

2- 'class4' database olusturun (M). Database silin (M). Ayni database yine olusturun (K)

CREATE database class4

3- https://www.postgresqltutorial.com/postgresql-sample-database/ adresine gidin ve ER modeli inceleyin. Tablolar arasindaki en az 5 iliskiyi yazin.(Hangi tablolar arasinda ne tur bir iliski var)

# film_actor and actor tables >> one to zero or one relation
# country and city tables >> one to zero or many relation
# staff and payment tables >> one to zero or many relation
# stayy and store tables >> one to zero or one relation
# film and inventory tables >> one to zero or many relation

5- ER modeldeki tablolardan 3 tanesini K olusturun.

CREATE TABLE City (
    city_id int NOT NULL PRIMARY KEY,
    city character varying(25) NOT NULL,
    country_id smallint NOT NULL,
    last_update timestamp without time zone NOT NULL,
        CONSTRAINT City
        FOREIGN KEY (country_id)
        REFERENCES Country (country_id)          
)
CREATE TABLE Country (
    country_id integer NOT NULL PRIMARY KEY,
    country character varying(35) NOT NULL,
    last_update timestamp without time zone NOT NULL        
)
CREATE TABLE Actor (
    actor_id integer NOT NULL PRIMARY KEY,
    first_name character varying(50),
    last_name character varying(50),
    last_update timestamp without time zone NOT NULL
)
6- ER modeldeki tablolardan 3 tanesini C olusturun.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
command='''create table address (
adress_id integer primary key,
district varchar(15)
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
command='''create table inventory (
inventory_id integer primary key,
film_id integer
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
command='''create table staff (
staff_id integer primary key,
first_name varchar(15),
active integer
)'''
cur.execute(command)
cur.close()
conn.commit()
conn.close()


8- Olusturdugunuz 3 tabloya K ile 5 veri girisi yapin.

insert into inventory  values(5, 8, 9)
insert into inventory  values(1, 5, 8)
insert into inventory  values(6, 8, 3)
insert into inventory  values(1, 9, 2)
insert into inventory  values(2, 9, 2)

insert into payment  values(9, 8, 5, 3)
insert into payment  values(1, 2, 3, 4)
insert into payment  values(9, 8, 6, 5)
insert into payment  values(7, 5, 3, 2)
insert into payment  values(7, 8, 9, 2)

insert into country(country_id, country, last_update) values (1,'Turkey','2021-04-07 19:20:20')
insert into country(country_id, country, last_update) values (2,'France','2021-04-07 19:20:20')
insert into country(country_id, country, last_update) values (3,'Spain','2021-04-07 19:20:20')
insert into country(country_id, country, last_update) values (4,'Italy','2021-04-07 19:20:20')
insert into country(country_id, country, last_update) values (5,'Greece','2021-04-07 19:20:20')

9- Olusturdugunuz 3 tabloya C ile 5 veri girisi yapin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("insert into address values(%s, %s, %s) (1,'Tiel')")
cur.execute("insert into address values(%s, %s, %s) (2,'Rotterdam')")
cur.execute("insert into address values(%s, %s, %s) (3,'Emmen')")
cur.execute("insert into address values(%s, %s, %s) (4,'Ost')")
cur.execute("insert into address values(%s, %s, %s) (5,'Emmelord')")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("insert into inventory values(%s, %s, %s), (4, 5)")
cur.execute("insert into inventory values(%s, %s, %s), (8, 7)")
cur.execute("insert into inventory values(%s, %s, %s), (8,6)")
cur.execute("insert into inventory values(%s, %s, %s), (1,7)")
cur.execute("insert into inventory values(%s, %s, %s), (4, 8)")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("insert into staff values(%s, %s, %s) ,(6, 'bulent', 1)")
cur.execute("insert into staff values(%s, %s, %s), (5, 'asya', 0)")
cur.execute("insert into staff values(%s, %s, %s) ,(4, 'funda', 1)")
cur.execute("insert into staff values(%s, %s, %s) ,(3, 'cem', 1)")
cur.execute("insert into staff values(%s, %s, %s) ,(2, 'john', 0)")
cur.close()
conn.commit()
conn.close()

11-  3 tablodaki birer veriyi K ile degistirin.

update inventory set film_id=3 where film_id=4
update payment set staff_id=4 where rental_id=1
update rental set rental_date='2020/04/05' where rental_id=1

12- 3 tablodaki birer veriyi C ile degistirin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("update inventory set film_id=7 where film_id=4")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("update address set district='Tiel' where adress_id=5")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("update staff set active=0 where first_name='bulent'")
cur.close()
conn.commit()
conn.close()

14- 3 tablonun son satirini K ile silin.

delete from payment where rental_id=1
delete from inventory where inventory_id=1
delete from rental where inventory_date='2020-05-03'

15- 3 tablonun son satirini C ile silin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("delete from inventory where film_id=15")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("delete from address where district='Emmen'")
cur.close()
conn.commit()
conn.close()


conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("delete from staff where first_name='asya'")
cur.close()
conn.commit()
conn.close()

17- 1 tabloyu K ile silin.

drop table customer

18- 1 tabloyu C ile silin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("drop table staff")
cur.close()
conn.commit()
conn.close()

19- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu K ile baska bir tablo olarak olusturun.

create table inventory_new AS
select inventory_id, film_id
from inventory;

20- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu C ile baska bir tablo olarak olusturun.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("create table inventory_new as select inventory_id, film_id from inventory")
cur.close()
conn.commit()
conn.close()

22- Tablolardan 1 tanesini K ile truncate edin.

truncate inventory

23- Tablolardan 1 tanesini C ile truncate edin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("truncate payment")
cur.close()
conn.commit()
conn.close()

25- 2 tabloyu K ile silin.

drop table film_category, inventory_new

26- 2 tabloyu C ile silin.
conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("drop table address, inventory")
cur.close()
conn.commit()
conn.close()

28- Postgresql arayuzundeki son tabloyu da K ile silin.

drop table payment

30- Import ettiginiz bu tabloyu C ile silin.

conn=psycopg2.connect("dbname=class4 user=postgres password=220525525.b")
cur=conn.cursor()
cur.execute("drop table inventory_new")
cur.close()
conn.commit()
conn.close()

32- DB nizde 15 adet tablo olmasi lazim. Her tabloyu teker teker goruntuleyin ve kolon isimlerine bakarak, 5 tabloda hangi kolonun PK ve FK oldugunu yazin.

-'inventory' table primarykey: inventory_pkey  foreignkey: inventory_film_id_fkey
-'language' table primarykey: language_pkey   foreignkey:
-'payment' table primarykey: payment_pkey  foreignkey: payment_customer_id_fkey, payment_rental_id_fkey, payment_staff_id_fkey
-'' table primarykey: rental_pkey  foreignkey: rental_customer_id_fkey, rental_inventory_id_fkey, rental_staff_id_key
-'rental' table primarykey:   foreignkey:
-'staff' table primarykey: staff_pkey  foreignkey: staff_address_id_fkey
-'store' table primarykey: store_pkey  foreignkey: store_address_id_fkey, store_manager_staff_id_fkey
-'actor' table primarykey: actor_id
-'adress' table primarykey: adress_pkey foreignkey: fk_address_city
-'category' table primarykey:category_pkey foreignkey:
-'city' table primarykey: city_pkey  foreignkey: fk_city
-'country' table primarykey: country_pkey   foreignkey:
-'customer' table primarykey: customer_pkey  foreignkey: customer_address_id_fkey
-'film' table primarykey: film_pkey   foreignkey: film_language_id_fkey
-'film_actor' table primarykey: film_actor_pkey  foreignkey: film_actor_actor_id_fkey, film_actor_film_id_fkey
-'film_category' table primarykey: film_category_pkey  foreignkey: film_category_category_id_fkey, film_category_film_id_fkey

33- Action filmlerinin ortalama suresi ne kadar?
select avg(length) from film where film_id in (select film_id from film_category where category_id=1)

34- En cok staff olan store hangisidir?

35- 'Gene Willis' adli actorun oynadigi filmlerin ratingi nedir?
select rating from film where film_id in (select film_id from film_actor where actor_id = (select actor_id from actor where first_name='Gene' and last_name='Willis' ))

36- Aktif customer sayisi nedir?
select count(*) from customer where active=1

37- 'C' harfiyle baslayan filmler hangileridir?
select * from film where title like 'C%'

38- 4$ den az odeme yapan musterilerin e-mail edresleri nedir?
select email from customer where customer_id in (select customer_id from payment where amount<4 )

39- Moscow'da ikamet eden staff ve customer tablosu? (sadece isim/soyisim sutunu olsun)
select first_name, last_name from staff where address_id in (select address_id from address where district like 'Mos%') union select first_name, last_name from customer where address_id in (select address_id from address where district like 'Mos%')

40- En az kiralanan 5 film hangisidir?
create table new as select inventory.inventory_id, inventory.film_id, rental.rental_id from inventory right join rental on inventory.inventory_id=rental.inventory_id 
select film_id, count(inventory_id) from new group by film_id  order by count(film_id) asc limit 5

41- 2006 yilinda yayinlanan ingilizce filmler hangileridir?
select title from film where release_year=2006 and language_id in (select language_id from language where name='English')