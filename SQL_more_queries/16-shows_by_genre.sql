-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_genres.name
from tv_shows
LEFT JOIN tv_show_genres on tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_genres on tv_show_genres.show_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name ASC;