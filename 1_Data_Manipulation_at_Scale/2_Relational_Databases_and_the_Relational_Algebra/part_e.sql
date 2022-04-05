-- SQLite

SELECT count(docid) FROM (
    SELECT docid, sum(count) as term_count
    FROM Frequency
    GROUP BY docid
    HAVING sum(count)>300
)