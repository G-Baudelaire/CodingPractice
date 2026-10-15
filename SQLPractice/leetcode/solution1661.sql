SELECT a1.machine_id, AVG(a2.timesstamp - a1.timestamp) AS processing_time
FROM Activity AS a1
JOIN Activity AS a2
    ON a2.activity_type = 'end'
    AND a1.activity_type = 'start'
    AND a1.machine_id = a2.machine_id
    AND a1.process_id = a2.process_id;
