-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres, tv_show_genres, tv_shows
LEFT JOIN tv_show_genres AS tgenre ON tv_shows.id = tgenre.show_id
GROUP BY tv_shows.id;
