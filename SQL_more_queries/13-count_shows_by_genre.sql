-- 13-count_shows_by_genre.sql
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) 
FROM tv_genres
GROUP BY tv_genres.name
RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id 
ORDER BY COUNT(tv_show_genres.show_id) DESC;