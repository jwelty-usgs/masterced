import django_tables2 as tables
from django_tables2.utils import A
from django.contrib.auth.models import User

class viewuser_table(tables.Table):
    username = tables.LinkColumn('edituser', args=[A('id')], empty_values=())

      # An inline class to provide additional information on the form.
    class Meta:
        model = User
        attrs = {"class": "paleblue"}
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined')


class viewalluser_table(tables.Table):
    username = tables.LinkColumn('manageuser', args=[A('id')], empty_values=())

      # An inline class to provide additional information on the form.
    class Meta:
        model = User
        attrs = {"class": "paleblue"}
        fields = ('username', 'email', 'first_name', 'last_name', 'date_joined')


