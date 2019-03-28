### Set user name variables to be filled in below
SET @newelidgeuserdisplay = 'Shauna Everett (User: eshauna), U.S. Fish and Wildlife Service, Oregon Fish and Wildlife Office'; #New elidgble user display name

SET @oldusernm = 'gshauna'; #Old Username
SET @newusernm = 'eshauna'; #New Username

SET @oldfullnm = 'Shauna Ginger'; #Old Full Name
SET @newfullnm = 'Shauna Everett'; #New Full Name

SET @olduseremail = 'shauna_ginger@fws.gov'; #Old email
SET @newuseremail = 'shauna_everett@fws.gov'; #New email

SET @olduserlastnm = 'Ginger'; #Old last name
SET @newuserlastnm = 'Everett'; #New last name

SET @authuserid = 296; #User ID in the auth_user table
###


SET SQL_SAFE_UPDATES = 0; #Disable safe mode to allow database updates based on names rather than primary keys

### Update specific tables as necessary

# Update accounts_elidgbleusers
UPDATE ced.accounts_elidgbleusers
SET username = @newusernm, userdisplay = @newelidgeuserdisplay
WHERE username = @oldusernm;

# Update accounts_userprofile
UPDATE ced.accounts_userprofile
SET Approving_Official = @newfullnm
WHERE Approving_Official = @oldfullnm;

# Update auth_user
UPDATE ced.auth_user
SET username = @newusernm, email = @newuseremail, last_name = @newuserlastnm
WHERE id = @authuserid;

# Update ced_main_agreement_protect
UPDATE ced.ced_main_agreement_protect
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_batchupload
UPDATE ced.ced_main_batchupload
SET Uploading_User = @newusernm
WHERE Uploading_User = @oldusernm;

# Update ced_main_batchupload_groups
UPDATE ced.ced_main_batchupload_groups
SET Uploading_User = @newusernm
WHERE Uploading_User = @oldusernm;

# Update ced_main_collab_party
UPDATE ced.ced_main_collab_party
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_county_info
UPDATE ced.ced_main_county_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_documentation
UPDATE ced.ced_main_documentation
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_fwsreview
UPDATE ced.ced_main_fwsreview
SET Certifier_Name = @oldfullnm
WHERE Certifier_Name = @newfullnm;

# Update ced_main_implementation_info
UPDATE ced.ced_main_implementation_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_location_info
UPDATE ced.ced_main_location_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_metrics
UPDATE ced.ced_main_metrics
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_ownership_info
UPDATE ced.ced_main_ownership_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_population_info
UPDATE ced.ced_main_population_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_project_info
UPDATE ced.ced_main_project_info
SET Created_By = @newusernm
WHERE Created_By = @oldusernm;

# Update ced_main_project_info
UPDATE ced.ced_main_project_info
SET User_Email = @olduseremail
WHERE User_Email = @newuseremail;

# Update ced_main_project_info
UPDATE ced.ced_main_project_info
SET Updating_User = @newusernm
WHERE Updating_User = @oldusernm;

# Update ced_main_project_info
UPDATE ced.ced_main_project_info
SET Approving_Official = @newusernm
WHERE Approving_Official = @oldusernm;

# Update ced_main_project_query
UPDATE ced.ced_main_project_query
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_state_info
UPDATE ced.ced_main_state_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_subactivity_effective_state
UPDATE ced.ced_main_subactivity_effective_state
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_subactivity_methods
UPDATE ced.ced_main_subactivity_methods
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_subactivity_objectives
UPDATE ced.ced_main_subactivity_objectives
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_threats
UPDATE ced.ced_main_threats
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_wafwa_info
UPDATE ced.ced_main_wafwa_info
SET User = @newusernm
WHERE User = @oldusernm;

# Update ced_main_wafwa_info
UPDATE ced.ced_main_wafwa_info
SET User = @newusernm
WHERE User = @oldusernm;

###

SET SQL_SAFE_UPDATES = 1; #Set the safe mode back to default