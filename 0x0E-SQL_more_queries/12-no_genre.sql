-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT t.title, g.genre_id
  FROM tv_shows AS t
    LEFT JOIN tv_show_genres AS g
      ON t.id = g.show_id
      WHERE g.genre_id IS NULL
 ORDER BY t.title, g.genre_id;
