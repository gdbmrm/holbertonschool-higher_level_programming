-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM hbtn_0d_tvshows.tv_genres, hbtn_0d_tvshows.tv_show_genres
GROUP BY tv_genres.name;
