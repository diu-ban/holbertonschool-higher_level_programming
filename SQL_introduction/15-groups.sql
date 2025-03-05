-- number by score 
SELECT DISTINCT score, COUNT(score) AS number FROM second_table GROUP BY score;
