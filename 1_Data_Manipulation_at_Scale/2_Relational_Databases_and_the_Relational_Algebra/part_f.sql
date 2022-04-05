-- SQLite
SELECT count(*) FROM (
    SELECT docid
    FROM Frequency
    WHERE term LIKE "transactions"
    INTERSECT
    SELECT docid
    FROM Frequency
    WHERE term like "world"
)