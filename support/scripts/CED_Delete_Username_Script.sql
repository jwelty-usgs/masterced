### Set user name variables to be filled in below
SET @username = "StateLands"; 
SET @authuserid = 386; #User ID in the auth_user table
###


SET SQL_SAFE_UPDATES = 0; #Disable safe mode to allow database updates based on names rather than primary keys

### Delete specific tables as necessary

# Delete accounts_usergroups and accounts_usergroups_groupid
DELETE ced.accounts_usergroups, ced.accounts_usergroups_groupid
FROM ced.accounts_usergroups
INNER JOIN ced.accounts_usergroups_groupid ON ced.accounts_usergroups.id = ced.accounts_usergroups_groupid.usergroups_id
WHERE userid_id = @authuserid;

# Delete accounts_usergroups table
DELETE FROM ced.accounts_usergroups
WHERE userid_id = @authuserid;

# Delete accounts_useredits and accounts_useredits_editinguser
DELETE ced.accounts_useredits, ced.accounts_useredits_editinguser
FROM ced.accounts_useredits
INNER JOIN ced.accounts_useredits_editinguser ON ced.accounts_useredits.id = ced.accounts_useredits_editinguser.useredits_id
WHERE userid_id = @authuserid;

# Delete accounts_useredits table
DELETE FROM ced.accounts_useredits
WHERE userid_id = @authuserid;

# Delete accounts_elidgbleusers
DELETE FROM ced.accounts_elidgbleusers
WHERE username = @username;

# Delete auth_user_groups table
DELETE FROM ced.auth_user_groups
WHERE User_ID = @authuserid;

# Delete accounts_userprofile
DELETE FROM ced.accounts_userprofile
WHERE User_ID = @authuserid;

# Delete auth_user
DELETE FROM ced.auth_user
WHERE id = @authuserid;

###

SET SQL_SAFE_UPDATES = 1; #Set the safe mode back to default