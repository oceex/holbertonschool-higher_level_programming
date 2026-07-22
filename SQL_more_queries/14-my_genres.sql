--  lists all genres of the show Dexter
SELECT gen.name
FROM tv_genres gen
JOIN tv_show_genres shen ON shen.genre_id = gen.id
JOIN tv_shows sho ON sho.id = shen.show_id
WHERE sho.title = 'Dexter'
ORDER BY gen.name;