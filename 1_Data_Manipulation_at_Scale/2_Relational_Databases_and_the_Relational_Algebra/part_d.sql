-- SQLite
SELECT count(distinct(docid))
FROM Frequency
WHERE term LIKE "law" OR term LIKE "legal"