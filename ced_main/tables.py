import django_tables2 as tables
from ced_main.models import project_info, documentation, documentation_values, project_query
from django_tables2.utils import A
from django.utils.safestring import mark_safe

class viewprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Created_By','Entry_Type', 'Date_Approved') # fields to display

class viewprojectname_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_query
        attrs = {"class": "paleblue"}
        fields = ('Project_Name','Project_ID') # fields to display

class viewprojectid_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_query
        attrs = {"class": "paleblue"}
        fields = ('Project_ID','Project_Name') # fields to display

class viewproject_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Created_By','Entry_Type', 'Date_Approved')

class viewdraftprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Date_Created', 'Last_Updated', 'Entry_Type')

class viewawaitingprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Date_Created', 'Last_Updated', 'Date_Approved', 'Entry_Type')


class viewapprovedprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Date_Created', 'Last_Updated', 'Date_Approved', 'Entry_Type')

class viewallprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Created_By', 'Entry_Type', 'Date_Approved')

class viewapprovalprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Created_By','Entry_Type', 'Date_Approved')

class viewuserprojects_table(tables.Table):
    # An inline class to provide additional information on the form.
    Project_Name = tables.LinkColumn('editproject', args=[A('Project_ID')], empty_values=())
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity', 'Office', 'Date_Created', 'Created_By', 'Last_Updated', 'Updating_User', 'Entry_Type', 'Date_Approved')

class viewbatchs1_table(tables.Table):
    # An inline class to provide additional information on the form.
    class Meta:
        model = project_info
        attrs = {"class": "paleblue"}
        fields = ('Project_ID', 'Project_Name', 'Activity', 'SubActivity') # fields to display


TEMPLATE = """
<input id="desc" maxlength="255" name="Document_Description" type="text"/>
"""

Test = documentation_values.objects.all()
TEMPLATE1 = """
<select id="File_Type">
<option>---Choose File Type---
<option>Data
<option>Habitat Assessment
<option>Management Plan
<option>Map(s)
<option>Monitoring Report
<option>Other
<option>Photos
<option>Project Proposal
<option>Seed Information
<option>Peer-Reviewed Science
</select>
"""

class MyColumn(tables.Column):
     empty_values = list()
     def render(self, value, record):
        FP = 'file://localhost/ced_main/Templates/ced_main/media/'
        return mark_safe('<a href="' + FP + '%s">%s </a>' % (value, value))

class viewdocuments_table(tables.Table):
    # An inline class to provide additional information on the form.
    File_Type = tables.TemplateColumn(TEMPLATE1)
    Document_Description = tables.TemplateColumn(TEMPLATE, accessor='pk')
    Document_Name = MyColumn(A('Document_Name'), empty_values=())

    class Meta:
        model = documentation
        attrs = {"class": "paleblue"}
        fields = ('id', 'Project_ID', 'File_Type', 'Document_Description', 'Document_Name', 'Date_Entered', 'User')
