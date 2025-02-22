-- What are the top 5 brands by receipts scanned for most recent month?
SELECT
    b.name,
    COUNT(r.receiptId) AS receipt_count
FROM
    Receipts r
JOIN
    Brands b ON r.brandId = b.brandId
WHERE
    DATE_TRUNC('month', r.purchaseDate) = DATE_TRUNC('month', (SELECT MAX(purchaseDate) FROM Receipts)) -- Most recent month in data
GROUP BY
    b.name
ORDER BY
    receipt_count DESC
LIMIT 5;
