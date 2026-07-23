-- list all genres not linked to the show Dexter
USE hbtn_0d_tvshows;
SELECT name
FROM tv_genres
WHERE NOT name IN (
    SELECT name
    FROM tv_genres g
    JOIN tv_show_genres sg ON sg.genre_id = g.id
    JOIN tv_shows s ON sg.show_id = s.id
    WHERE s.title = 'New Girl'
        )
ORDER BY name;
