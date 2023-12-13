-- Displays the average temp (in Fahrenheit) by city ordered by descending temp.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
