-- list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN (
    SELECT name
    FROM tv_genres g
    JOIN tv_show_genres sg ON sg.genre_id = g.id
    JOIN tv_shows s ON sg.show_id = s.id
    WHERE s.title = 'Dexter'
        )
ORDER BY name;