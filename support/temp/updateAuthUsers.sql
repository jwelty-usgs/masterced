select distinct c.user_id,a.username,a.first_name,a.last_name,c.agency,c.field_office
from accounts_userprofile c, auth_user a, auth_user_groups b
where c.user_id = a.id and a.id=b.user_id and b.group_id=1;

update accounts_office_values
set office = 'Wind River Reservation'
where id = 96;

update accounts_userprofile
set field_office = 'Wind River Reservation'
where field_office = 'Wind River Agency';