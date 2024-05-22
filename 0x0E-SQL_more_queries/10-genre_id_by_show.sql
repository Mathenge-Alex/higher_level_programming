-- List all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT	shows.title,
	show_gen.genre_id
FROM	tv_shows AS shows
INNER JOIN tv_show_genres AS show_gen
ON	shows.id = show_gen.show_id
ORDER BY shows.title, show_gen.genre_id;
