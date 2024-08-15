from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('add',AddpView.as_view(),name='add'),
    path('list',PListView.as_view(),name='plist'),
    path('del/<int:pid>',PDeleteView.as_view(),name='pdel'),
    path('edt/<int:pid>',PEditView.as_view(),name='pedt'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)