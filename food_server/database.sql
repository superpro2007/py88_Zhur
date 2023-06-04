create table food (
id serial primary key,
name text ,
proteins integer check (proteins >= 0),
fats integer check (fats >=0),
carbohydrates integer check(carbohydrates >= 0),
eaten_at timestamp default now(),
user_id bigint
);