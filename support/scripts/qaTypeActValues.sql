/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 * Author:  kernt
 * Created: May 12, 2017
 */

UPDATE ced_main_project_info t2
(   
SELECT activity, subactivity, id2 
FROM typeact_new
) t1
SET t2.subactivity_id = t1.id2
WHERE t1.activity = t2.activity
and t1.subactivity = t2.subactivity;
 
UPDATE ced_main_project_info t2
join typeact_new t1 
on t1.activity = t2.activity
and t1.subactivity = t2.subactivity
set t2.subactivity_id = t1.id2;
 
UPDATE ced_main_project_info t2
( 
SELECT activity, subactivity, id 
FROM ced_main_subactivity
) t1
SET t2.activity = t1.activity, 
t2.subactivity = t1.subactivity,
t2.typeact = t1.typeact
where t1.id = t2.id;
 
UPDATE ced_main_project_info t2
join ced_main_subactivity t1 
on t2.subactivity_id = t1.id
set t2.activity = t1.activity;
 
UPDATE ced_main_project_info t2
(
SELECT activity, subactivity, id
FROM ced_main_subactivity
) t1
SET t2.activity = t1.activity,
t2.subactivity = t1.subactivity,
t2.typeact = t1.typeact
where t1.id = t2.id;
 
UPDATE c1 t2
(
SELECT activity, id
FROM ced_main_subactivity
) t1
SET t2.activity = t1.activity
where t1.id = t2.subactivity_id;
 
UPDATE ced_main_project_info  t2
join ced_main_subactivity t1
on t2.subactivity_id = t1.id
set t2.activity = t1.activity,
t2.subactivity = t1.subactivity,
t2.typeact = t1.typeact;
 
create or replace view missing_subactivities as
select distinct subactivity_id, count(*) totalcount
from ced_main_project_info
where subactivity_id not in
(select id from ced_main_subactivity)
group by subactivity_id
order by 1;

quit