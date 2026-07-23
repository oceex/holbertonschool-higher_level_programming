-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT title
FROM tv_shows
WHERE title NOT IN (
    SELECT title
    FROM tv_shows s
    JOIN tv_show_genres sg ON sg.show_id = s.id
    JOIN tv_genres g ON g.id = sg.genre_id
    WHERE g.name = 'Comedy'
    )
ORDER BY title;