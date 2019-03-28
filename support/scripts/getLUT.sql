select * from ced_main_activity
INTO OUTFILE '/tmp/ced_main_activity.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_subactivity
INTO OUTFILE '/tmp/ced_main_subactivity.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_typeact
INTO OUTFILE '/tmp/ced_main_typeact.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from accounts_office_values
INTO OUTFILE '/tmp/accounts_office_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from auth_group
INTO OUTFILE '/tmp/auth_group.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from auth_permission
INTO OUTFILE '/tmp/auth_permission.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_activity_plan_values
INTO OUTFILE '/tmp/ced_main_activity_plan_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_documentation_values
INTO OUTFILE '/tmp/ced_main_documentation_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_imp_party_values
INTO OUTFILE '/tmp/ced_main_imp_party_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_metric
INTO OUTFILE '/tmp/ced_main_metric.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_ownership_values
INTO OUTFILE '/tmp/ced_main_ownership_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_population_values
INTO OUTFILE '/tmp/ced_main_population_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_subactivity_effectiveness_rating_data
INTO OUTFILE '/tmp/ced_main_subactivity_effectiveness_rating_data.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_subactivity_effective_state_data
INTO OUTFILE '/tmp/ced_main_subactivity_effective_state_data.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_subactivity_methods_data
INTO OUTFILE '/tmp/ced_main_subactivity_methods_data.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_subactivity_objectives_data
INTO OUTFILE '/tmp/ced_main_subactivity_objectives_data.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_threat_values
INTO OUTFILE '/tmp/ced_main_threat_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from ced_main_wafwa_zone_values
INTO OUTFILE '/tmp/ced_main_wafwa_zone_values.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from subactivity_effective_state_data_lut
INTO OUTFILE '/tmp/subactivity_effective_state_data_lut.txt'
FIELDS ENCLOSED BY '"'
TERMINATED BY '|'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n';

select * from subactivity_effectiveness_rating_data_lut
INTO OUTFILE '/tmp/subactivity_effectiveness_rating_data_lut.txt'
FIELDS ENCLOSED BY '"'
TERMINATED BY '|'
LINES TERMINATED BY '\r\n';

select * from subactivity_methods_data_lut
INTO OUTFILE '/tmp/subactivity_methods_data_lut.txt'
FIELDS ENCLOSED BY '"'
TERMINATED BY '|'
LINES TERMINATED BY '\r\n';

select * from subactivity_objectives_data_lut
INTO OUTFILE '/tmp/subactivity_objectives_data_lut.txt'
FIELDS ENCLOSED BY '"'
TERMINATED BY '|'
LINES TERMINATED BY '\r\n';

select * from subactivity_metric_lut
INTO OUTFILE '/tmp/subactivity_metric_lut.csv'
FIELDS ENCLOSED BY '"'
TERMINATED BY ','
LINES TERMINATED BY '\r\n';
