"""forumfix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from forum import views
from forum.views import (category, create_response, create_thread, dashboard,
                         thread_detail, thread_list,edit_response,edit_thread,delete_thread,delete_response)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("account/", include("django.contrib.auth.urls")),
    path("forum/", dashboard.dashboard, name="dashboard"),
    path("category/", category.CategoryListView.as_view(), name="category"),
    path("list/<int:category_id>/", thread_list.list, name="thread_list"),
    path("detail/<int:thread_id>/", thread_detail.detail, name="thread_detail"),
    # path("detail/<pk>/", thread_detail.ThreadDetailView.as_view(), name="thread_detail"),
    path("thread/<int:category_id>", create_thread.create, name="create_thread"),
    path("response/<int:thread_id>", create_response.home, name="create_response"),
    path("<int:thread_id>/<int:response_id>/edit", edit_response.edit_response, name="edit_response"),
    path("<int:category_id>/<int:thread_id>/new", edit_thread.edit_thread, name="edit_thread"),
    path("delete/<int:category_id>/<int:thread_id>/", delete_thread.delete, name="thread_delete"),
    path("deletee/<int:thread_id>/<int:response_id>/", delete_response.delete_response, name="response_delete"),
]
