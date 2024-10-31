-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
INNER JOIN tv_genres
ORDER BY tv_shows.title, tv_genres.name ASC;
