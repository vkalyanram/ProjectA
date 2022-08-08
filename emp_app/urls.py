from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
        path('',views.index,name='index'),
        path('view_emp',views.view_emp,name='view_emp'),
        path('add_emp',views.add_emp,name='add_emp'),
        path('del_emp',views.del_emp,name='del_emp'),
        path('edit_emp',views.edit_emp,name='edit_emp'),
        path('edit_emp_details/<int:emp_id>',views.edit_emp_details,name='edit_emp_details'),
        path('edit_emp/<int:emp_id>',views.edit_emp,name='edit_emp'),
        path('del_emp/<int:emp_id>',views.del_emp,name='del_emp'),
        path('search_emp',views.search_emp,name='search_emp'),

]
