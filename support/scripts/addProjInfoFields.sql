/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 * Author:  kernt
 * Created: May 22, 2017
 */

alter table ced_main_project_info add column BatchUploadFileName varchar(255);
alter table ced_main_project_info add column BatchUploadFolderName varchar(255);
alter table ced_main_project_info add column BatchUploadOBJECTID int(11);
alter table ced_main_project_info add column Prj_ID int(11);
update ced_main_project_info set BatchUploadOBJECTID=0, Prj_ID=0;
 
alter table ced_main_implementation_info add column Prj_ID int(11);
alter table ced_main_implementation_info add column Project_Name varchar(255);

quit