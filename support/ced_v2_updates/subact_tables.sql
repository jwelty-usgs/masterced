drop table if exists subactivity_effectiveness_rating_data_lut;

create table subactivity_effectiveness_rating_data_lut(
id int(11) NOT NULL AUTO_INCREMENT,
activity_id int(11),
subactivity_id int(11),
Effectiveness_Rating varchar(200),
PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE 'subactivity_effectiveness_rating_data_lut.csv'
INTO TABLE subactivity_effectiveness_rating_data_lut
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

show warnings;

create or replace view ced_main_subactivity_effectiveness_rating_data as
select distinct a.id, b.Activity, c.SubActivity, a.Effectiveness_Rating
from subactivity_effectiveness_rating_data_lut a, activity_lut b, subactivity_lut c
where a.activity_id=b.id and a.subactivity_id=c.id;

drop table if exists subactivity_effective_state_data_lut;

create table subactivity_effective_state_data_lut(
id int(11) NOT NULL AUTO_INCREMENT,
activity_id int,
subactivity_id int,
Effectiveness_Statement varchar(200),
Ordering int(11) default 0,
PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE 'subactivity_effective_state_data_lut.csv'
INTO TABLE subactivity_effective_state_data_lut
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

show warnings;

create or replace view ced_main_subactivity_effective_state_data as
select distinct a.id, c.activity, b.subactivity, a.Effectiveness_Statement, a.Ordering
from subactivity_effective_state_data_lut a, subactivity_lut b, activity_lut c
where a.subactivity_id=b.id
and a.activity_id=c.id;


drop table if exists subactivity_methods_data_lut;

create table subactivity_methods_data_lut(
id int(11) NOT NULL AUTO_INCREMENT,
activity_id int(11),
subactivity_id int(11),
Method varchar(200),
Ordering int(11) default 0,
PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE 'subactivity_methods_data_lut.csv'
INTO TABLE subactivity_methods_data_lut
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

show warnings;

create or replace view ced_main_subactivity_methods_data as
select distinct a.id, b.Activity, c.SubActivity, a.Method, a.Ordering
from subactivity_methods_data_lut a, activity_lut b, subactivity_lut c
where a.activity_id=b.id and a.subactivity_id=c.id;


drop table if exists subactivity_objectives_data_lut;

create table subactivity_objectives_data_lut(
id int(11) NOT NULL AUTO_INCREMENT,
activity_id int(11),
subactivity_id int(11),
Objective varchar(200),
Ordering int(11) default 0,
PRIMARY KEY (`id`)
);

LOAD DATA LOCAL INFILE 'subactivity_objectives_data_lut.csv'
INTO TABLE subactivity_objectives_data_lut
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n';

show warnings;

create or replace view ced_main_subactivity_objectives_data as
select distinct a.id, b.Activity, c.SubActivity, a.Objective, a.Ordering
from subactivity_objectives_data_lut a, activity_lut b, subactivity_lut c
where a.activity_id=b.id and a.subactivity_id=c.id;
