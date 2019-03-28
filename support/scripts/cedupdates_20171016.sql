UPDATE ced_main_project_info a
  INNER JOIN ced_main_metrics b
    ON a.Project_ID=b.Project_ID
SET a.Metric_Value = b.TotalAcres,
  Metric = 'Acres'
where a.metric is null
and b.TotalAcres is not null
and b.TotalAcres > 0;

UPDATE ced_main_project_info a
  INNER JOIN ced_main_metrics b
    ON a.Project_ID=b.Project_ID
SET a.Metric_Value = b.TotalMiles,
  Metric = 'Miles'
where a.metric is null
      and b.TotalMiles is not null
      and b.TotalMiles > 0;

UPDATE ced_main_project_info set Metric_Value = NULL where Metric is NULL;

create or replace view ced_main_metrics_view AS
select distinct Project_ID, Metric_Value as TotalAcres, 0 as TotalMiles, Date_Created as Date_Entered
  from ced_main_project_info
    where Metric = 'Acres'
UNION
  select distinct Project_ID, 0 as TotalAcres, Metric_Value as TotalMiles, Date_Created as Date_Entered
  from ced_main_project_info
  where Metric = 'Miles';

quit