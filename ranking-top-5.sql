-- How does the ranking of the top 5 brands by receipts scanned for the recent month compare to the ranking for the previous month?
SELECT b.name, SUM(r.totalSpent) AS total_spend
FROM Brands b
JOIN RewardsReceiptItems rri ON b.barcode = rri.barcode
JOIN Receipts r ON rri.receipt_id = r.receipt_id
JOIN Users u ON r.userId = u.user_id
WHERE u.createdDate >= date('now', '-6 months')
GROUP BY b.name
ORDER BY total_spend DESC
LIMIT 1;

