SELECT
	p.id,
	COUNT(l.id) AS likes_count,
	(SELECT COUNT(*) FROM comments WHERE photo_id = p.id) AS comments_count
FROM
	photos AS p
JOIN
	likes AS l ON p.id = l.photo_id
GROUP BY 
	p.id
ORDER BY
	likes_count DESC,
	comments_count DESC,
	p.id