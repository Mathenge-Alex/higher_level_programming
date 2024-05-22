-- List all shows contained in hbtn_0d_tvshows without a genre linked
SELECT	shows.title,
	show_gen.genre_id
FROM	tv_shows AS shows
LEFT JOIN tv_show_genres AS show_gen
ON shows.id = show_gen.show_id
WHERE show_gen.genre_id IS NULL
ORDER BY shows.title, show_gen.genre_id;
