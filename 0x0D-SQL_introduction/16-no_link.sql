-- Lists all records of the table second_table having a name,
-- displaying the score and the name in this order
-- in descending order.

SELECT score, name FROM second_table
WHERE name != "" ORDER BY score DESC
