create table products (
id serial primary key,
name text,
proteins decimal,
fats decimal,
carbohydrates decimal,
eaten_at timestamp default now()
);