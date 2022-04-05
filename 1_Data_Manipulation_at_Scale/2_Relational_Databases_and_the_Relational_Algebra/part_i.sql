-- SQLite
DROP VIEW IF EXISTS MYVIEW;

CREATE VIEW MYVIEW AS
    SELECT * FROM frequency
    UNION
    SELECT 'query' as docid, 'washington' as term, 1 as count 
    UNION
    SELECT 'query' as docid, 'taxes' as term, 1 as count
    UNION 
    SELECT 'query' as docid, 'treasury' as term, 1 as count;

DROP VIEW IF EXISTS SIMILARITY;
CREATE VIEW SIMILARITY AS
SELECT B.docid, SUM(A.count*B.count) as similarity
FROM
(SELECT docid, term, count FROM MYVIEW WHERE docid="query") AS A
JOIN Frequency AS B ON A.term=B.term
GROUP BY B.docid
ORDER BY similarity DESC LIMIT 10;

SELECT max(similarity) FROM SIMILARITY;