DROP TABLE IF EXISTS `accounts_groups`;
DROP TABLE IF EXISTS `accounts_office_values`;
DROP TABLE IF EXISTS `accounts_useredits_editinguser`;
DROP TABLE IF EXISTS `accounts_usergroups`;
DROP TABLE IF EXISTS `accounts_usergroups_groupid`;
DROP TABLE IF EXISTS `accounts_userprofile`;
DROP TABLE IF EXISTS `auth_group`;
DROP TABLE IF EXISTS `auth_group_permissions`;
DROP TABLE IF EXISTS `auth_permission`;
DROP TABLE IF EXISTS `auth_user_groups`;
DROP TABLE IF EXISTS `auth_user_user_permissions`;
DROP TABLE IF EXISTS `ced_main_activity_legacy`;
DROP TABLE IF EXISTS `ced_main_activity_plan_values`;
DROP TABLE IF EXISTS `ced_main_agreement_protect`;
DROP TABLE IF EXISTS `ced_main_collab_party_collab_party`;
DROP TABLE IF EXISTS `ced_main_county`;
DROP TABLE IF EXISTS `ced_main_county_info_county_value`;
DROP TABLE IF EXISTS `ced_main_documentation`;
DROP TABLE IF EXISTS `ced_main_documentation_values`;
DROP TABLE IF EXISTS `ced_main_fwsreview`;
DROP TABLE IF EXISTS `ced_main_huc12`;
DROP TABLE IF EXISTS `ced_main_huc12_info_huc12_value`;
DROP TABLE IF EXISTS `ced_main_imp_party_values`;
DROP TABLE IF EXISTS `ced_main_implementation_info`;
DROP TABLE IF EXISTS `ced_main_location_check`;
DROP TABLE IF EXISTS `ced_main_location_info`;
DROP TABLE IF EXISTS `ced_main_metric`;
DROP TABLE IF EXISTS `ced_main_metrics`;
DROP TABLE IF EXISTS `ced_main_ownership_info_owner_value`;
DROP TABLE IF EXISTS `ced_main_ownership_values`;
DROP TABLE IF EXISTS `ced_main_population_info_population_value`;
DROP TABLE IF EXISTS `ced_main_population_values`;
DROP TABLE IF EXISTS `ced_main_project_query`;
DROP TABLE IF EXISTS `ced_main_seeding`;
DROP TABLE IF EXISTS `ced_main_state_county`;
DROP TABLE IF EXISTS `ced_main_state_county_huc12_values`;
DROP TABLE IF EXISTS `ced_main_state_info_state_value`;
DROP TABLE IF EXISTS `ced_main_subactivity_old`;
DROP TABLE IF EXISTS `ced_main_threats_threat`;
DROP TABLE IF EXISTS `ced_main_threat_values`;
DROP TABLE IF EXISTS `ced_main_threats`;
DROP TABLE IF EXISTS `ced_main_typeact_legacy`;
DROP TABLE IF EXISTS `ced_main_wafwa_info_wafwa_value`;
DROP TABLE IF EXISTS `ced_main_wafwa_zone_values`;
DROP TABLE IF EXISTS `django_admin_log`;
DROP TABLE IF EXISTS `django_content_type`;
DROP TABLE IF EXISTS `django_session`;
DROP TABLE IF EXISTS `legacy_project_subactivities`;
DROP TABLE IF EXISTS `registration_registrationprofile`;

DROP TABLE IF EXISTS `ced_main_batchupload`;
DROP TABLE IF EXISTS `ced_main_batchupload_groups`;

DROP VIEW IF EXISTS `ced_main_subactivity_methods_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_objectives_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_effectiveness_rating_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_effective_state_data`;

DROP TABLE IF EXISTS `ced_main_subactivity_effective_state_Effectiveness_Statement`;
DROP TABLE IF EXISTS `ced_main_subactivity_effective_state`;

DROP TABLE IF EXISTS `ced_main_subactivity_methods_Method`;
DROP TABLE IF EXISTS `ced_main_subactivity_methods`;

DROP TABLE IF EXISTS `ced_main_subactivity_objectives_Objective`;
DROP TABLE IF EXISTS `ced_main_subactivity_objectives`;

DROP VIEW IF EXISTS `ced_main_activity`;
DROP VIEW IF EXISTS `ced_main_metrics_view`;
DROP VIEW IF EXISTS `ced_main_subactivity`;
DROP VIEW IF EXISTS `ced_main_typeact`;
DROP VIEW IF EXISTS `qry_ced2ags_agreement_protect`;
DROP VIEW IF EXISTS `qry_ced2ags_collaborators`;
DROP VIEW IF EXISTS `qry_ced2ags_county`;
DROP VIEW IF EXISTS `qry_ced2ags_documentation`;
DROP VIEW IF EXISTS `qry_ced2ags_huc12`;
DROP VIEW IF EXISTS `qry_ced2ags_office`;
DROP VIEW IF EXISTS `qry_ced2ags_ownership`;
DROP VIEW IF EXISTS `qry_ced2ags_population`;
DROP VIEW IF EXISTS `qry_ced2ags_project`;
DROP VIEW IF EXISTS `qry_ced2ags_project2`;
DROP VIEW IF EXISTS `qry_ced2ags_state`;
DROP VIEW IF EXISTS `qry_ced2ags_threats`;
DROP VIEW IF EXISTS `qry_ced2ags_wafwa`;

DROP TABLE IF EXISTS `accounts_elidgbleusers`;
DROP TABLE IF EXISTS `accounts_useredits`;
DROP TABLE IF EXISTS `auth_user`;
DROP TABLE IF EXISTS `ced_main_collab_party`;
DROP TABLE IF EXISTS `ced_main_county_info`;
DROP TABLE IF EXISTS `ced_main_huc12_info`;
DROP TABLE IF EXISTS `ced_main_ownership_info`;
DROP TABLE IF EXISTS `ced_main_population_info`;
DROP TABLE IF EXISTS `ced_main_state_info`;
DROP TABLE IF EXISTS `ced_main_wafwa_info`;

DROP TABLE IF EXISTS `ced_main_subactivity_effective_state_effectiveness_statement`;
DROP TABLE IF EXISTS `ced_main_subactivity_effective_state`;
DROP TABLE IF EXISTS `ced_main_subactivity_methods_method`;
DROP TABLE IF EXISTS `ced_main_subactivity_methods`;
DROP TABLE IF EXISTS `ced_main_subactivity_objectives_objective`;
DROP TABLE IF EXISTS `ced_main_subactivity_objectives`;

DROP VIEW IF EXISTS `ced_main_subactivity_effective_state_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_effectiveness_rating_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_methods_data`;
DROP VIEW IF EXISTS `ced_main_subactivity_objectives_data`;
DROP TABLE IF EXISTS `subactivity_effective_state_data_lut`;
DROP TABLE IF EXISTS `subactivity_effectiveness_rating_data_lut`;
DROP TABLE IF EXISTS `subactivity_objectives_data_lut`;
DROP TABLE IF EXISTS `subactivity_methods_data_lut`;

DROP TABLE IF EXISTS `ced_main_activity_plan_values`;
DROP VIEW IF EXISTS `ced_main_activity_plan_values`;
DROP TABLE IF EXISTS `subactivity_metric_lut`;

DROP TABLE IF EXISTS `ced_main_state`;
DROP TABLE IF EXISTS `subactivity_lut`;
DROP TABLE IF EXISTS `subactivity_metric_mapping`;
DROP TABLE IF EXISTS `activity_lut`;
DROP TABLE IF EXISTS `typeact_lut`;
DROP TABLE IF EXISTS `ced_main_project_info`;

show tables;