-- noinspection SqlDialectInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

-- noinspection SqlNoDataSourceInspection,SqlDialectInspection,SqlNoDataSourceInspection
update ced_main_project_info set activity='RESTORATION: Infrastructure Removal and Modification'
where activity = 'RESTORATION: Infrastructure Removal, and Modification';

update ced_main_activity set activity='RESTORATION: Infrastructure Removal and Modification'
where activity = 'RESTORATION: Infrastructure Removal, and Modification';

create table ced_main_subactivity_new (
id integer,
subactivity varchar(100),
activity VARCHAR(100),
typeact VARCHAR (20),
old_id INTEGER
);

LOAD DATA INFILE '/temp/subnew.csv' INTO TABLE ced_main_subactivity_new
FIELDS TERMINATED BY ',';

rename table ced_main_subactivity to ced_main_subactivity_old;
rename table ced_main_subactivity_new to ced_main_subactivity;

quit

