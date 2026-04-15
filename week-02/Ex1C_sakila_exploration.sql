/*
a) The information that is included in the actor table is actor_id, first_name, last_name, last_update
b) The information that is included in the film table is film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features and last_update.
c) The table that contains both actor_id and film_id is film_actor.
d) The information that is included in the rental table is rental_id, rental_date, inventory_id, customer_id, return_date, staff_id and last_update. The table is easy to read because of how it's structured in the table.
e) The information that is inculded in the inventory table is inventory_id, film_id, store_id and last_update.
f) To find the names of the films that were rented on a specific date you would need the rental, inventory and film tables. They are related because the rental table uses inventory_id as a forgein key to link it to the inventory table, and inventory table uses the forgein key film_id to connect to connect to the film table.
*/

Select rental_id, rental_date, inventory_id from rental;
select inventory_id, film_id from inventory;
select film_id, title from film;
