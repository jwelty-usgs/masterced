from django.conf.urls import *
from ced_main import views

urlpatterns = [
    ### Menu URLs
    url(r'sgeditmenu/$', views.sgeditmenu, name='sgeditmenu'),
    url(r'sgappmenu/$', views.sgappmenu, name='sgappmenu'),
    url(r'sgadminmenu/$', views.sgadminmenu, name='sgadminmenu'),

    ### Home Page URLs
    url(r'^$', views.index, name='index'),

    ### New Project URLs
    url(r'dataentrynew/$', views.dataentry_new, name='dataentrynew'),

    ### Spoatial Entry URLs
    url(r'spatialhelp/$', views.spatialhelp, name='spatialhelp'),

    ### Edit Projects
    url(r'(?P<prid>\d+)/editproject/$', views.editproject, name='editproject'),
    url(r'(?P<prid>\d+)/readonly/$', views.readonly, name='readonly'),
    url(r'(?P<prid>\d+)/viewproject/$', views.viewproject, name='viewproject'),
    url(r'(?P<prid>\d+)/viewonlyproject/$', views.viewonlyproject, name='viewonlyproject'),

    url(r'redirectpg/$', views.redirectpg, name='redirectpg'),

    ### View Project Tables

    url(r'viewprojects/$', views.viewprojects, name='viewprojects'),

    url(r'viewprojectsicanedit/$', views.viewprojectsicanedit, name='viewprojectsicanedit'),

    url(r'viewallprojects/$', views.viewallprojects, name='viewallprojects'),

    url(r'viewdraftprojects/$', views.viewdraftprojects, name='viewdraftprojects'),

    url(r'viewawaitingprojects/$', views.viewawaitingprojects, name='viewawaitingprojects'),

    url(r'viewapprovedprojects/$', views.viewapprovedprojects, name='viewapprovedprojects'),

    url(r'viewapprovalprojects/$', views.viewapprovalprojects, name='viewapprovalprojects'),

    url(r'viewbatchapprovalprojects/$', views.viewbatchapprovalprojects, name='viewbatchapprovalprojects'),

    url(r'viewuserprojects/$', views.viewuserprojects, name='viewuserprojects'),

    url(r'error_check_projects/$', views.error_check_projects, name='error_check_projects'),
    url(r'error_check_projects_successful/$', views.error_check_projects_successful,
        name='error_check_projects_successful'),

    url(r'delete_success/$', views.delete_success, name='delete_success'),
    url(r'mark_for_deletion/$', views.mark_for_deletion, name='mark_for_deletion'),
    url(r'permanent_deletion/$', views.permanent_deletion, name='permanent_deletion'),

    url(r'project_not_exists/$', views.project_not_exists, name='project_not_exists'),
    url(r'project_not_exists_temp/$', views.project_not_exists_temp, name='project_not_exists_temp'),

    ### Project queries, reports, and summary charts
    url(r'sgcedquery/$', views.sgcedquery, name='sgcedquery'),
    url(r'fwsquery/$', views.fwsquery, name='fwsquery'),
    url(r'sgcedqueryresponse/$', views.sgcedqueryresponse, name='sgcedqueryresponse'),
    url(r'sgcedsummary/$', views.sgcedsummary, name='sgcedsummary'),
    url(r'sgceddocumentation/$', views.sgceddocumentation, name='sgceddocumentation'),

    ### Projects Updated
    url(r'edit_project_success/$', views.editprjsuccess, name='editprjsuccess'),

    url(r'project_approval_success/$', views.project_approval_success, name='project_approval_success'),

    url(r'project_approved/$', views.project_approved, name='project_approved'),

    ### Email CED users
    url(r'emailcedusers/$', views.emailcedusers, name='emailcedusers'),
    url(r'emailceduserssuccess/$', views.emailceduserssuccess, name='emailceduserssuccess'),

    ### Batch Upload URLs
    url(r'batch_upload/$', views.batch_upload, name='batch_upload'),
    url(r'batch_upload_available/$', views.batch_upload_available, name='batch_upload_available'),
    url(r'batch_upload_initial_success/$', views.batch_upload_initial_success, name='batch_upload_initial_success'),
    url(r'batch_upload_template/$', views.batch_upload_template, name='batch_upload_template'),

    ### SG CED bugs
    url(r'bug_reports/$', views.bug_reports, name='bug_reports'),

    ### SG CED bugs
    url(r'sgerd/$', views.sgerd, name='sgerd'),

    ### Permission Denied or Unable to Access Sites URLs
    url(r'permission_denied/$', views.permission_denied, name='permission_denied'),
    url(r'readonly/$', views.readonly, name='readonly'),
    url(r'none_to_edit/$', views.none_to_edit, name='none_to_edit'),
    url(r'accept_user_agreement/$', views.accept_user_agreement, name='accept_user_agreement'),
    url(r'lcmap_sb_down/$', views.lcmap_sb_down, name='lcmap_sb_down'),
    url(r'sbunavailable/$', views.sbunavailable, name='sbunavailable'),
    ### Temp Under Construction URLs
    url(r'under_construction/$', views.under_construction, name='under_construction'),
]
