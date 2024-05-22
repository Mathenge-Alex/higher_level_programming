-- List all available coincidences--
SELECT
    score,
    name
FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
