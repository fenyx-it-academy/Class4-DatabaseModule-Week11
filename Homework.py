"""(M:Manuel olarak, K:SQL komutlariyla, C:Python kodlariyla)

Asagidaki sorulardan K ve C ile cozulmesini istediklerimizin cozumlerini
(komut veya kodlarini) ustte sorusu altta cozumu olacak sekilde bir dosyaya yapistirip gondermenizi istiyoruz.

1- 'pycoders' isimli bir server kurun. (M)

2- 'class4' database olusturun (M). Database silin (M). Ayni database yine olusturun (K)

   *create database class4

3- https://www.postgresqltutorial.com/postgresql-sample-database/ adresine gidin ve ER modeli inceleyin.
Tablolar arasindaki en az 5 iliskiyi yazin.(Hangi tablolar arasinda ne tur bir iliski var)

   * category ile film_category arasinda (one to one) iliskisi var.
   * film ile inventory arasinda (one to many) iliskisi var.
   * rental ile staff arasinda (many to one) iliskisi var.
   * adress ile store arasinda (one to many) iliskisi var.
   * payment ile customer arasinda (many to one) iliskisi var.

4- ER modeldeki tablolardan 3 tanesini M olusturun.

5- ER modeldeki tablolardan 3 tanesini K olusturun.

create table category (
    category_id int NOT NULL PRIMARY KEY,
    name varchar (20) NOT NULL,
    last_update timestamp without time zone NOT NULL,
        PRIMARY KEY(category_id)
        CONSTRAINT category

)
create table film_category (
    film_id integer NOT NULL PRIMARY KEY,
    last_update timestamp without time zone NOT NULL
    PRIMARY KEY(film_id)
    CONSTRAINT film_category
    FOREIGN KEY (category_id)
    REFERENCES category(category_id)
)
create table film (
    film_id integer NOT NULL PRIMARY KEY,
    title varchar(20),
    description varchar(20),
    release_year int text
)

6- ER modeldeki tablolardan 3 tanesini C olusturun.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

command='''create table inventory (
                inventory_id INTEGER PRIMARY KEY,
                last_update timestamp without time zone NOT NULL
                FOREIGN KEY (film_id)
                FOREIGN KEY (store_id)

)'''

command1='''create table rental (
                rental_id INTEGER PRIMARY KEY,
                rental_date text
                return_date text
                last_update timestamp without time zone NOT NULL
                FOREIGN KEY (inventory_id)
                FOREIGN KEY (customer_id)

)'''

command2='''create table staff (
                staff_id INTEGER PRIMARY KEY,
                first_name varchar(20)
                last_name varchar(20)
                email text
                FOREIGN KEY (address_id)
                FOREIGN KEY (store_id)
)'''

#create a table
cur.execute(command)
cur.execute(command1)
cur.execute(command2)
# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

7- Olusturdugunuz 3 tabloya M ile 5 veri girisi yapin.

8- Olusturdugunuz 3 tabloya K ile 5 veri girisi yapin.

insert into category(category_id,name,last_update) values (1,'action','1905-10-01 19:05:00')
insert into category(category_id,name,last_update) values (2,'comedies','1905-10-01 19:05:00')
insert into category(category_id,name,last_update) values (3,'adventure','1905-10-01 19:05:00')
insert into category(category_id,name,last_update) values (4,'musicals','1905-10-01 19:05:00')
insert into category(category_id,name,last_update) values (5,'war','1905-10-01 19:05:00')

insert into film_category(category_id,film_id,last_update) values (1,'1','1905-10-01 19:05:00')
insert into film_category(category_id,film_id,last_update) values (2,'1','1905-10-01 19:05:00')
insert into film_category(category_id,film_id,last_update) values (3,'1','1905-10-01 19:05:00')
insert into film_category(category_id,film_id,last_update) values (4,'1','1905-10-01 19:05:00')
insert into film_category(category_id,film_id,last_update) values (5,'1','1905-10-01 19:05:00')

insert into film(film_id,description,release_year) values (1,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China','2006')
insert into film(film_id,description,release_year) values (2,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China','2006')
insert into film(film_id,description,release_year) values (3,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China','2006')
insert into film(film_id,description,release_year) values (4,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China','2006')
insert into film(film_id,description,release_year) values (5,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China','2006')

9- Olusturdugunuz 3 tabloya C ile 5 veri girisi yapin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("INSERT INTO category VALUES (%s, %s, %s)", (1,'action','1905-10-01 19:05:00'))
cur.execute("INSERT INTO category VALUES (%s, %s, %s)", (2,'comedies','1905-10-01 19:05:00'))
cur.execute("INSERT INTO category VALUES (%s, %s, %s)", (3,'adventure','1905-10-01 19:05:00'))
cur.execute("INSERT INTO category VALUES (%s, %s, %s)", (4,'musicals','1905-10-01 19:05:00'))
cur.execute("INSERT INTO category VALUES (%s, %s, %s)", (5,'war','1905-10-01 19:05:00'))

cur.execute("INSERT INTO film_category VALUES (%s, %s, %s)", (1,'1','1905-10-01 19:05:00'))
cur.execute("INSERT INTO film_category VALUES (%s, %s, %s)", (2,'1','1905-10-01 19:05:00'))
cur.execute("INSERT INTO film_category VALUES (%s, %s, %s)", (3,'1','1905-10-01 19:05:00'))
cur.execute("INSERT INTO film_category VALUES (%s, %s, %s)", (4,'1','1905-10-01 19:05:00'))
cur.execute("INSERT INTO film_category VALUES (%s, %s, %s)", (5,'1','1905-10-01 19:05:00'))

cur.execute("INSERT INTO film VALUES (%s, %s, %s)", (1,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China',2006))
cur.execute("INSERT INTO film VALUES (%s, %s, %s)", (2,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China',2006))
cur.execute("INSERT INTO film VALUES (%s, %s, %s)", (3,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China',2006))
cur.execute("INSERT INTO film VALUES (%s, %s, %s)", (4,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China',2006))
cur.execute("INSERT INTO film VALUES (%s, %s, %s)", (5,'A Action-Packed Tale of a Man And a Lumberjack who must Reach a Feminist in Ancient China',2006))

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

10- 3 tablodaki birer veriyi M ile degistirin.

11- 3 tablodaki birer veriyi K ile degistirin.

UPDATE category set name='actions' where category_id=2
UPDATE category set name='musicals' where category_id=3
UPDATE category set name='war' where category_id=4

12- 3 tablodaki birer veriyi C ile degistirin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("UPDATE category SET category=%s WHERE category_id=%s", ('adventure',1))
cur.execute("UPDATE film_category SET film_category=%s WHERE category_id=%s", (2,3))
cur.execute("UPDATE film SET release_year=%s WHERE film_id=%s", (2007,5))

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

13- 3 tablonun son satirini M ile silin.

14- 3 tablonun son satirini K ile silin.

delete from category where category_id = 5
delete from film_category where film_category_id = 5
delete from film where film_id = 5

15- 3 tablonun son satirini C ile silin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("DELETE FROM category WHERE category_id = %s", (5,))
cur.execute("DELETE FROM film_category WHERE film_category_id = %s", (5,))
cur.execute("DELETE FROM film WHERE film_id = %s", (5,))

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

16- 1 tabloyu M ile silin.

17- 1 tabloyu K ile silin.

drop table film

18- 1 tabloyu C ile silin.
conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("drop table film")

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

19- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu K ile baska bir tablo olarak olusturun.

CREATE TABLE category_new AS SELECT category_id,name FROM category;

20- Kalan tablolardan 1 tanesinin 2 veya 3 sutununu C ile baska bir tablo olarak olusturun.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("CREATE TABLE category_new AS SELECT category_id,name FROM category")

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

21- Tablolardan 1 tanesini M ile truncate edin.

22- Tablolardan 1 tanesini K ile truncate edin.

truncate table film

23- Tablolardan 1 tanesini C ile truncate edin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("TRUNCATE TABLE film")

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

24- Truncate edilmis tablolari M ile silin.

25- 2 tabloyu K ile silin.

drop table category
drop table film_category

26- 2 tabloyu C ile silin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("DROP TABLE category, film_category")

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

27- Elimizde veri olan 1 tablo kalmis olmasi lazim. Bu tabloyu csv olarak bilgisayariniza yukleyin.

COPY film FROM '/path/to/csv/film.txt' WITH (FORMAT csv);

28- Postgresql arayuzundeki son tabloyu da K ile silin.

drop table film

29- Bilgisayarinizdaki csv yi arayuze import edin.

import pandas as pd

df = pd.read_csv (r'Path where the CSV file is stored\File film.csv')
print (df)

30- Import ettiginiz bu tabloyu C ile silin.

conn = psycopg2.connect("dbname=class4, user=postgres, password=***********")
cur = conn.cursor()

cur.execute("DROP TABLE film ")

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()
# close the connection
conn.close()

31- https://www.postgresqltutorial.com/postgresql-sample-database/ linkindeki ornek DB yi bilgisayariniza indirin
ve arayuze yukleyin.

This process was done during the lesson.

32- DB nizde 15 adet tablo olmasi lazim. Her tabloyu teker teker goruntuleyin ve kolon isimlerine bakarak,
5 tabloda hangi kolonun PK ve FK oldugunu yazin.

inventory==> PK:inventory_id FK:film_id,store_id
rental==>PK:rental_id FK:inventory_id,customer_id
payment==>PK:peyment_id FK:staff_id,customer_id,rental_id
language==>PK:language_id FK:
store==>PK:store_id FK:manager_staff_id,address_id

Sorgular? (Asagidaki sorularin cevaplarini ve bu cevabi bulurken kullandiginiz kodlari yazin)

33- Action filmlerinin ortalama suresi ne kadar?

--select * from film
select avg(length) from film where film_id=1

34- En cok staff olan store hangisidir?

--select * from store
select count(*) from store where manager_staff_id=1

output
count(begint)
1

--select * from store
select count(*) from store where manager_staff_id=2

output
count(begint)
1

35- 'Gene Willis' adli actorun oynadigi filmlerin ratingi nedir?

select__??????______(select film_id from film where film_id=(select actor_id from actor where first_name='Gene' and last_name='Willis'))

36- Aktif customer sayisi nedir?

select count(*) from customer where active=1

37- 'C' harfiyle baslayan filmler hangileridir?

select * from film where title like 'C%'

38- 4$ den az odeme yapan musterilerin e-mail edresleri nedir?

select email from customer where customer_id in (select customer_id from payment where amount<4 )

39- Moscow'da ikamet eden staff ve customer tablosu? (sadece isim/soyisim sutunu olsun)

select first_name, last_name
from staff where address_id in (select address_id from address where district like 'Mos%')
union select first_name, last_name
from customer where address_id in (select address_id from address where district like 'Mos%')

40- En az kiralanan 5 film hangisidir?

----------------------------------------------

41- 2006 yilinda yayinlanan ingilizce filmler hangileridir?

select title from film
where release_year=2006 and language_id in
(select language_id from language where name='English')
















"""