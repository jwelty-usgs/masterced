/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 * Author:  kernt
 * Created: May 11, 2017
 */

drop table if exists typeact_mapping;
create table typeact_mapping as select distinct project_id, activity, subactivity, typeact from ced_main_project_info;
alter table typeact_mapping add column activity2 varchar(75);
alter table typeact_mapping add column subactivity2 varchar(100);
alter table typeact_mapping add column typeact2 varchar(40);

update typeact_mapping set activity2 = 'Conifer Removal', subactivity2 = 'Conifer Removal (all phases)', typeact2 = 'Spatial Project' where activity = 'RESTORATION: Conifer Removal' and subactivity = 'Conifer Removal (all phases)';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Structure Removal', typeact2 = 'Non-Spatial Project' where activity = 'RESTORATION: Infrastructure Removal and Modification' and subactivity = 'Structure Removal';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Fence Removal', typeact2 = 'on-Spatial Project' where activity = 'RESTORATION: Infrastructure Removal and Modification' and subactivity = 'Fence Removal';

update typeact_mapping set activity2 = 'Non-Fire Related: Habitat Improvement / Restoration', subactivity2 = 'Annual Grass (Cheatgrass) Treatments', typeact2 = 'Spatial Project' where activity = 'RESTORATION: Non-Fire Related: Habitat Improvement / Restoration' and subactivity = 'Annual Grass (Cheatgrass) Treatments';

update typeact_mapping set activity2 = 'Non-Fire Related: Habitat Improvement / Restoration', subactivity2 = 'Vegetation Management / Habitat Enhancement', typeact2 = 'Spatial Project' where activity = 'RESTORATION: Non-Fire Related: Habitat Improvement / Restoration' and subactivity = 'Vegetation Management / Habitat Enhancement';

update typeact_mapping set activity2 = 'Habitat Restoration (Fire)', subactivity2 = 'Post-fire restoration (only native seeding, plantings)', typeact2 = 'Spatial Project' where activity = 'RESTORATION: Habitat Restoration (Fire)' and subactivity = 'Post-fire restoration (only native seeding, plantings)';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Federal Land Use Plan', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'Federal Land Use Plan';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'State Conservation Plan', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'State Conservation Plan	Non-Spatial Plan';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Fire Mutual Aid Agreement', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'Fire Mutual Aid Agreement';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Conservation Banking / Advanced Crediting Systems', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'Conservation Banking / Advanced Crediting Systems';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Fire Related Conservation Strategy (Pre-suppression Plans)', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'Fire Related Conservation Strategy (Pre-suppression Plans)';

update typeact_mapping set activity2 = 'NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs)', subactivity2 = 'Non-regulatory Conservation Strategies', typeact2 = 'Non-Spatial Plan' where activity = 'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)' and subactivity = 'Non-regulatory Conservation Strategies';

update typeact_mapping set activity2 = 'NON-REGULATORY MECHANISMS: (Plans, Strategies, BMPs)', subactivity2 = 'Minimization  and Avoidance Strategies / BMPs', typeact2 = 'Non-Spatial Plan' where activity = 'NON-REGULATORY CONSERVATION PLANS (Strategies, BMPs)' and subactivity = 'Minimization and Avoidance Strategies / BMPs';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Fence Modification', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Fence Modification';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Fence Marking', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Fence Removal';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Powerline Burial', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Structure Removed: Powerline';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Powerline Retrofitting / Modification', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Powerline Retrofitting / Modification: Distribution Line';

update typeact_mapping set activity2 = 'Livestock & Rangeland Management', subactivity2 = 'Improved Grazing Practices (Rest, Rotation, Etc.)', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Livestock & Rangeland Management' and subactivity = 'Improved grazing practices in place (rest rotation, riparian areas fenced off)';
				
update typeact_mapping set activity2 = 'Fire-Related: Habitat Restoration and/or Pre-Supression Efforts', subactivity2 = 'Fuels Management / Cheatgrass Treatments', typeact2 = 'Spatial Project' where activity = 'Restoration: Wildfire Pre-suppression Efforts' and subactivity = 'Fuel Reduction Treatments';

update typeact_mapping set activity2 = 'Fire-Related: Habitat Restoration and/or Pre-Supression Efforts', subactivity2 = 'Fire Breaks', typeact2 = 'Spatial Project' where activity = 'Restoration: Wildfire Pre-suppression Efforts' and subactivity = 'Fuel Breaks';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Reclamation Plan', typeact2 = 'Non-Spatial Plan' where activity = 'Restoration: Habitat Reclamation Efforts' and subactivity = '---Select a Subactivity---';

update typeact_mapping set activity2 = 'Travel Management', subactivity2 = 'Road and Trail closure', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Recreation Management' and subactivity = 'Road and Trail closure';

update typeact_mapping set activity2 = 'Population Augmentation', subactivity2 = 'Translocation', typeact2 = 'Non-Spatial Project' where activity = 'Restoration: Population Augmentation' and subactivity = 'Translocation';

update typeact_mapping set activity2 = 'Wild Equid Management', subactivity2 = 'Wild Equid Gather', typeact2 = 'Non-Spatial Project' where activity = 'Restoration: Wild Equid Management' and subactivity = 'Wild Equid Gather';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'County/Local Government Plan', typeact2 = 'Non-Spatial Plan' where activity = 'Regulatory Mechanisms, Plans, Policy' and subactivity = 'Local Government Plan';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Programmatic Candidate Conservation Agreement', typeact2 = 'Non-Spatial Plan' where activity = 'Non-regulatory Conservation Strategies' and subactivity = 'Programmatic Candidate Conservation Agreement with Assurances';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Programmatic Candidate Conservation Agreement with Assurances', typeact2 = 'Non-Spatial Plan' where activity = 'Non-regulatory Conservation Strategies' and subactivity = 'Programmatic Candidate Conservation Agreement';

update typeact_mapping set activity2 = 'Sagebrush Protection', subactivity2 = 'Land Acquisition', typeact2 = 'Spatial Project' where activity = 'Habitat Protection: Habitat Acquisition' and subactivity = 'Habitat Protected by Acquisition for Long-Term Conservation';

update typeact_mapping set activity2 = 'Sagebrush Protection', subactivity2 = 'Conservation Easement', typeact2 = 'Spatial Project' where activity = 'Habitat Protection: Conservation Easement' and subactivity = 'Habitat Protected by Easement for Long-Term Conservation';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Fence Marking', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Fence Marking';

update typeact_mapping set activity2 = 'Infrastucture Removal, and Modification', subactivity2 = 'Fence Removal', typeact2 = 'Non-Spatial Project' where activity = 'Restoration:  Infrastructure Removal and Modification' and subactivity = 'Fence Removal';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'State Conservation Plan', typeact2 = 'Non-Spatial Plan' where activity = 'Regulatory Mechanisms, Plans, Policy' and subactivity = 'State Conservation Plan';

update typeact_mapping set activity2 = 'Non-Fire Related: Habitat Improvement / Restoration', subactivity2 = 'Non-fire restroration (only non-native seedings, plantings)', typeact2 = 'Spatial Project' where activity = 'RESTORATION: Non-Fire Related: Habitat Improvement / Restoration' and subactivity = 'Non-fire restroration (only native seedings, plantings)';

update typeact_mapping set activity2 = 'Wild Equid Management', subactivity2 = 'Wild Equid Population Control', typeact2 = 'Non-Spatial Project' where activity = 'RESTORATION: Wild Equid Management' and subactivity = 'Wild Equid Population Control';

update typeact_mapping set activity2 = 'Sagebrush Protection', subactivity2 = 'Conservation Agreements (includes CCAs, CCAAs, Farm Bill and other Incentive-based programs).', typeact2 = 'Non-Spatial Project' where activity = 'SAGEBRUSH PROTECTION' and subactivity = 'Conservation Agreements (includes CCAs, CCAAs, Farm Bill and other Incentive-based programs)';

update typeact_mapping set activity2 = 'Sagebrush Protection', subactivity2 = 'Conservation Easement', typeact2 = 'Spatial Project' where activity = 'SAGEBRUSH PROTECTION' and subactivity = 'Conservation Easement';

update typeact_mapping set activity2 = 'Sagebrush Protection', subactivity2 = 'Land Acquisition', typeact2 = 'Spatial Project' where activity = 'SAGEBRUSH PROTECTION' and subactivity = 'Land Acquisition';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'Compensatory Mitigation Plans', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'Compensatory Mitigation Plans';

update typeact_mapping set activity2 = 'REGULATORY MECHANISMS: (Plans, Policies, Exec./Sec. Orders)', subactivity2 = 'State Conservation Plan', typeact2 = 'Non-Spatial Plan' where activity = 'REGULATORY MECHANISMS: Plans, Policies' and subactivity = 'State Conservation Plan';

quit