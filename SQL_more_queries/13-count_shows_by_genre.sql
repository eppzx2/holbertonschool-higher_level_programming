-- a little difficult task
SELECT tv_show_genres.genre_id AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
JOIN genres g ON tsg.genre_id = g.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;

