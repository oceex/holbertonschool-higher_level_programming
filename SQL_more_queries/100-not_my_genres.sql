--  list all genres not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE NOT name IN (
    SELECT name
    FROM tv_genres G
    JOIN tv_show_genres SG ON SG.genre_id = G.id
    JOIN tv_shows S ON SG.show_id = S.id
    WHERE S.title = 'Dexter'
        )
ORDER BY name;