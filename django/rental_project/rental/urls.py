from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('explore/', views.explore_page_view, name='explore'),
    path('host/', views.host_page_view, name='host'),
    path('product/<int:apartment_id>', views.product_page_view, name='apartment_details'),
    path('group/<int:group_id>', views.group_page_view, name='group_details'),
    path('userGroups/', views.user_groups_page_view, name='user_groups'),
    path('createGroup/<int:apartment_id>', views.CreateGroup.as_view(), name='create_group'),
    path('leaveFromGroup/<int:group_id>', views.leave_from_group, name='group_leave'),
    path('joinToGroup/<int:group_id>', views.join_to_group, name='group_join'),
]
