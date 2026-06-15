-- Write your query below

-- quiet:
-- never scored highest or lowest
-- took part in at least one exam


WITH lowest_score AS (
    SELECT 
        exam_id,
        student_id,
        score,
        DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score) AS rnk
        -- MIN(student_id) AS student_id,
        -- MIN(score) AS score
    FROM exam
),
highest_score AS (
    SELECT 
        exam_id,
        student_id,
        score,
        DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) AS rnk
        -- MIN(student_id) AS student_id,
        -- MIN(score) AS score
    FROM exam
),
exam_student AS (
    SELECT DISTINCT student_id
    FROM exam
)
SELECT *
FROM student s
JOIN exam_student e USING (student_id)
WHERE s.student_id NOT IN (SELECT student_id FROM lowest_score WHERE rnk = 1)
AND s.student_id NOT IN (SELECT student_id FROM highest_score WHERE rnk = 1)

-- WITH lowest_score AS (
--     SELECT 
--         exam_id,
--         MIN(student_id) AS student_id,
--         MIN(score) AS score
--     FROM exam
--     GROUP BY exam_id
-- ),
-- highest_score AS (
--     SELECT 
--         exam_id,
--         MAX(student_id) AS student_id,
--         MAX(score) AS score
--     FROM exam
--     GROUP BY exam_id
-- ),
-- students AS (
--     SELECT DISTINCT student_id
--     FROM exam
-- )
-- SELECT s2.student_id, s2.student_name
-- -- FROM highest_score
-- FROM students s1
-- JOIN student s2 ON s1.student_id = s2.student_id
-- WHERE 
--     s1.student_id NOT IN (SELECT student_id FROM lowest_score)
--     AND s1.student_id NOT IN (SELECT student_id FROM highest_score)