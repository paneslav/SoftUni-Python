UPDATE projects
SET end_date = start_date + interval '5 months'
WHERE end_date IS NULL
;