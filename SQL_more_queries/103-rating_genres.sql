-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT name, SUM(rate) AS rating
FROM tv_show_ratings r
JOIN tv_show_genres sg ON sg.show_id = r.show_id
JOIN tv_genres g ON g.id = sg.genre_id
GROUP BY name
ORDER BY rating DESC;