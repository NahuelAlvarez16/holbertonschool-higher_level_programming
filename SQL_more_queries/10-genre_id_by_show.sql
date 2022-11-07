-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
use hbtn_0d_tvshows;
SELECT tv_shows.title, tv_show_genres.genre_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;