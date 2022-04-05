-- SQLite

    SELECT SUM(A.count*B.count) as similarity
    FROM Frequency as A JOIN Frequency as B on A.term=B.term
    WHERE A.docid < B.docid 
    AND A.docid = '10080_txt_crude'
    AND B.docid = '17035_txt_earn'
    GROUP BY A.docid, B.docid;
