-- Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
from tv_genres
LEFT JOIN tv_show_genres on tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;