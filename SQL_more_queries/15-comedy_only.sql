-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title
from tv_genres
LEFT JOIN tv_show_genres on tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows on tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;