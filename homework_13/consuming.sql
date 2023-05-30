drop table consumption;
drop table users;


create table users (
id serial primary key,
name varchar[8] ,
age integer check (age > 0)
);

create table products (
id serial primary key,
name text,
price decimal,
supplier text,
amount integer
);

create table consumption (
id serial primary key,
user_id integer references users,
product_id integer references products,
amount integer,
bought_at timestamp default now()
);