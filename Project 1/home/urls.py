from django.urls import path
from home import views

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.musician_view, name='musician_view'),
    path('album/', views.album_view, name='album_view'),
    path('musician_form/', views.musician_form_view, name='musician_form'),
    path('album_form/', views.album_form_view, name='album_form'),
    path('album_list/<int:id>/', views.artist_album_view, name='artist_album_view'),
    path('artist_edit/<int:id>/', views.artist_edit_view, name='artist_edit_view'),
    path('album_edit/<int:album_id>/', views.album_edit_view, name='album_edit_view'),
    path('album_delete/<int:album_id>/', views.album_delete_view, name='album_delete_view'),
    path('artist_delete/<int:id>/', views.musician_delete_view, name='musician_delete_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
