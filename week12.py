#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 2- Ayni database yine olusturun (K)

CREATE DATABASE class4;


# 3- https://www.postgresqltutorial.com/postgresql-sample-database/ adresine gidin ve ER modeli inceleyin. Tablolar arasindaki en az 5 iliskiyi yazin.(Hangi tablolar arasinda ne tur bir iliski var)
# 
# - film- inventory  => One-to-Many
# - customer-rental  => one-to-many
# - film-language    => one-to-many
# - staff-address    => one-to-one
# - customer-payment => one-to-many
# 

# In[ ]:


# 5- ER modeldeki tablolardan 3 tanesini K olusturun.

-- CREATE TABLE actor (
-- 	actor_id serial PRIMARY KEY,
-- 	first_name VARCHAR ( 50 ) Not NULL,
-- 	last_name VARCHAR ( 50 )  NOT NULL,
-- 	lasT_update TIMESTAMP 
-- );

-- CREATE TABLE film_actor (
-- 	actor_id serial,
-- 	film_id serial,
-- 	last_login TIMESTAMP ,
-- 	Foreign Key(actor_id) References actor(actor_id),
-- 	Foreign Key(film_id) References film(film_id)
-- );



CREATE TABLE customer_id (
    customer_id INT NOT NULL,
    store_id INT NOT NULL,
	first_name VARCHAR ( 50 ) Not NULL,
	last_name VARCHAR ( 50 )  NOT NULL,
	email VARCHAR ( 50 )  NOT NULL,
	address_id Int  NOT NULL,
	activebool bool  NOT NULL,
	create_date Timestamp  NOT NULL,
	last_update TimeStamp,
	active bool
);


# In[4]:


6- ER modeldeki tablolardan 3 tanesini C olusturun.

import psycopg2

conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")

cur = conn.cursor()

cur.execute("""Create table inventory (
    inventory_id integer Primary key not null,
    film_id integer not null,
    store_id integer not null,
    last_update date not null
    )""")

cur.execute("""Create table stapaymentff (
    payment_id integer Primary key not null,
    customer_id integer not null,
    staff_id integer,
    rental_id integer null,
    amount varchar(40) not null,
    payment_date timestamp not null
    )""")

cur.execute("""Create table staff (
    stafF_id integer,
    first_name varchar(20) not null,
    last_name varchar(20) not null,
    address_id integer null,
    email varchar(40) not null
    )""")

cur.close()
conn.commit()
conn.close()


# In[ ]:


8- Olusturdugunuz 3 tabloya K ile 5 veri girisi yapin.
1- film_actor
# insert Into film_actor (actor_id, film_id, last_update) values(1,2,'12/12/2020');
# insert Into film_actor (actor_id, film_id, last_update) values(1,2,'12/12/2020');
# insert Into film_actor (actor_id, film_id, last_update) values(1,2,'12/12/2020');
# insert Into film_actor (actor_id, film_id, last_update) values(1,2,'12/12/2020');
# insert Into film_actor (actor_id, film_id, last_update) values(1,2,'12/12/2020');

2- 

# insert Into film_category (film_id, category_id, last_update) values(1,2,'12/12/2020');
# insert Into film_category (film_id, category_id, last_update) values(2,2,'12/5/2020');
# insert Into film_category (film_id, category_id, last_update) values(3,2,'1/3/2020');
# insert Into film_category (film_id, category_id, last_update) values(1,3,'1/1/2020');
# insert Into film_category (film_id, category_id, last_update) values(5,4,'1/2/2020');

# insert Into inventory (inventory_id, film_id, store_id, last_update) values(1, 2,2,'12/12/2020');
# insert Into inventory (inventory_id, film_id, store_id, last_update) values(2, 5,1,'12/12/2020');
# insert Into inventory (inventory_id, film_id, store_id, last_update) values(3, 4,5,'12/12/2020');
# insert Into inventory (inventory_id, film_id, store_id, last_update) values(4, 3,3,'12/12/2020');
# insert Into inventory (inventory_id, film_id, store_id, last_update) values(5, 2,4,'12/12/2020');


# In[ ]:


9- Olusturdugunuz 3 tabloya C ile 5 veri girisi yapin.

import psycopg2

conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")

cur = conn.cursor()

data_list = [
    (1, "Turkce", '12/12/2001',),
    (2, "English", '12/12/2001',),
    (3, "Nederlands", '12/12/2001',),
    (4, "Spanish", '12/12/2001',),
    (5, "French", '12/12/2001',)
]

command = 'Insert into language(language_id, name, last_update) values (%s, %s, %s)'


data_list_staff = [
    (1, 'Ahmet', 'Vural', 2, 'ahmetvural@test',),
    (2, 'Ayse', 'Klascascsafs', 2, 'test@test',),
    (3, 'Yavuz', 'dasdasd', 2, 'test3@test',),
    (4, 'Abuzer', 'Alaca', 2, 'abuzer@test',),
    (5, 'Murat', 'aa', 2, 'test3@test',),
]

command_staff = 'Insert into staff(staff_id, first_name, last_name, address_id, email) values (%s, %s, %s, %s, %s)'

data_list_payment = [
    (1, 3, 4, 1, 25, '12/12/2020',),
    (2, 2, 3, 2, 25, '12/12/2020',),
    (3, 3, 5, 4, 25, '12/12/2020',),
    (4, 5, 2, 5, 25, '12/12/2020',),
    (5, 1, 1, 8, 25, '12/12/2020',),
]

command_payment = 'Insert into payment(payment_id, customer_id, staff_id, rental_id, amount, payment_date) values (%s, %s, %s, %s, %s, %s)'


cur.executemany(command_staff, data_list_staff)
cur.executemany(command_payment, data_list_payment)


cur.close()
conn.commit()
conn.close()


# In[ ]:


11- 3 tablodaki birer veriyi K ile degistirin.

Update film set title='Mission imposible:Ghost Protocol' where film_id=1; 
Update actor set last_name='Jullie' where actor_id=3; 
Update category set name='Romantic' where category_id=4; 


# In[ ]:


12- 3 tablodaki birer veriyi C ile degistirin.

import psycopg2

conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")

cur = conn.cursor()

command_staff = """ UPDATE staff
                SET last_name = %s
                WHERE staff_id = %s"""

command_payment = """UPDATE payment
                SET amount = %s
                WHERE payment_id = %s"""

command_payment = """UPDATE inventory
                SET store_id = %s
                WHERE inventory_id = %s"""

cur.execute(command_staff, ('Balli', 2))
cur.execute(command_payment, (200, 1))
cur.execute(command_staff, (3, 4))

cur.close()
conn.commit()
conn.close()


# In[ ]:


14- 3 tablonun son satirini K ile silin.


 DELETE 
  FROM actor 
  WHERE actor_id in (
      SELECT actor_id 
      FROM actor 
      ORDER BY actor_id desc
      LIMIT 1
     )
    

    
 DELETE 
  FROM film 
  WHERE film_id in (
      SELECT film_id 
      FROM film 
      ORDER BY film_id desc
      LIMIT 1
     )


 DELETE 
  FROM inventory 
  WHERE inventory_id in (
      SELECT inventory_id 
      FROM inventory 
      ORDER BY inventory_id desc
      LIMIT 1
     )


# In[ ]:


15- 3 tablonun son satirini C ile silin.

import psycopg2

conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")

cur = conn.cursor()

command_language = """DELETE
FROM actor
WHERE actor_id in (
    SELECT actor_id
    FROM actor
    ORDER BY actor_id desc
    LIMIT 1
)"""

command_payment = """DELETE
FROM film
WHERE film_id in (
    SELECT film_id
    FROM film
    ORDER BY film_id desc
    LIMIT 1
)"""

command_staff = """DELETE
FROM inventory
WHERE inventory_id in (
    SELECT inventory_id
    FROM inventory
    ORDER BY inventory_id desc
    LIMIT 1
)"""

cur.execute(command_language)
cur.execute(command_payment)
cur.execute(command_staff)

cur.close()
conn.commit()
conn.close()


# In[ ]:


17- 1 tabloyu K ile silin.

drop table actor Cascade


# In[ ]:


18- 1 tabloyu C ile silin.

import psycopg2

conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")

cur = conn.cursor()

command = """drop table film Cascade"""

cur.execute(command)

cur.close()
conn.commit()
conn.close()


# In[ ]:


19- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu K ile baska bir tablo olarak olusturun.

Create table new_table as Select( first_name), (last_name) from staff


# In[ ]:


20- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu C ile baska bir tablo olarak olusturun.


import psycopg2
conn = psycopg2.connect("dbname='class4' user='postgres' password='Asude1608.'")
cur = conn.cursor()
command = """Create table new_table_2 as Select(actor_id), (film_id) from film_actor"""
cur.execute(command)
cur.close()
conn.commit()
conn.close()


# In[ ]:


22- Tablolardan 1 tanesini K ile truncate edin.


Truncate category


# In[ ]:


23- Tablolardan 1 tanesini C ile truncate edin.

import psycopg2
conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")
cur = conn.cursor()
command = """Truncate film_actor"""
cur.execute(command)
cur.close()
conn.commit()
conn.close()


# In[ ]:


25- 2 tabloyu K ile silin.


Drop table category Cascade;
Drop table film_category Cascade;


# In[ ]:


26- 2 tabloyu C ile silin.


import psycopg2
conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")
cur = conn.cursor()
command_1 = """Drop table new_table Cascade"""
command_2 = """Drop table new_table_2 Cascade"""
cur.execute(command_1)
cur.execute(command_2)
cur.close()
conn.commit()
conn.close()


# In[ ]:





# In[ ]:


28- Postgresql arayuzundeki son tabloyu da K ile silin.



Drop table staff Cascade;


# In[ ]:


30- Import ettiginiz bu tabloyu C ile silin.



import psycopg2
conn = psycopg2.connect(
    "dbname='class4' user='postgres' password='Asude1608.'")
cur = conn.cursor()
command = """Drop table staff Cascade"""
cur.execute(command)
cur.close()
conn.commit()
conn.close()


# In[ ]:


32- DB nizde 15 adet tablo olmasi lazim. Her tabloyu teker teker goruntuleyin ve kolon isimlerine bakarak, 5 tabloda hangi kolonun PK ve FK oldugunu yazin.

actor table: actor_id Primary Key
    
address table: address_id PK, city_id FK referenced from city

category table: category_id PK, 
    
inventory table: inventory_id PK, film_id FK referenced from film
    
rental table: rental_id PK, customer_id FK referenced from customer, inventory_id referenced from inventory, staff_id referenced from staff


# In[ ]:


get_ipython().set_next_input('33- Action filmlerinin ortalama suresi ne kadar');get_ipython().run_line_magic('pinfo', 'kadar')


select avg(length) from film where film_id in (select film_id from film_category where category_id =1)


# In[ ]:


get_ipython().set_next_input('34- En cok staff olan store hangisidir');get_ipython().run_line_magic('pinfo', 'hangisidir')


select store_id from staff Group by store_id order by count(store_id) limit 1


# In[ ]:


get_ipython().set_next_input("35- 'Gene Willis' adli actorun oynadigi filmlerin ratingi nedir");get_ipython().run_line_magic('pinfo', 'nedir')

select rating from film where film_id in (select film_id from film_actor where actor_id in (select actor_id from actor where first_name='Gene' and last_name='Willis'))


# In[ ]:


get_ipython().set_next_input('36- Aktif customer sayisi nedir');get_ipython().run_line_magic('pinfo', 'nedir')

select count(*) from customer where active =1


# In[ ]:


get_ipython().set_next_input("37- 'C' harfiyle baslayan filmler hangileridir");get_ipython().run_line_magic('pinfo', 'hangileridir')

select * from film where title like 'C%'


# In[ ]:


get_ipython().set_next_input('38- 4$ den az odeme yapan musterilerin e-mail edresleri nedir');get_ipython().run_line_magic('pinfo', 'nedir')


select email from customer where customer_id in (select customer_id from payment where amount < 4)


# In[ ]:


39- Moscow'da ikamet eden staff ve customer tablosu? (sadece isim/soyisim sutunu olsun)


select first_name, last_name 
	from customer 
	where address_id in (select address_id from address where city_id = (select city_id from city where city='Moscow')) 
	union select first_name, last_name 
	from staff 
	where address_id in (select address_id from address where city_id = (select city_id from city where city='Moscow'))


# In[ ]:


get_ipython().set_next_input('40- En az kiralanan 5 film hangisidir');get_ipython().run_line_magic('pinfo', 'hangisidir')

select film_id , count(inventory_id) 
	from (select i.inventory_id, i.film_id, r.rental_id from inventory as i right join rental as r on i.inventory_id = r.inventory_id) as foo
# 	group by film_id order by count(inventory_id) asc limit 5


# In[ ]:


get_ipython().set_next_input('41- 2006 yilinda yayinlanan ingilizce filmler hangileridir');get_ipython().run_line_magic('pinfo', 'hangileridir')
select * from film where language_id in (select language_id from language where name='English') and release_year = 2006

