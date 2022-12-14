from django.contrib import admin
from django.urls import include,path,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
import debug_toolbar
from django.contrib.flatpages import views
urlpatterns = [
    path('social/', include('social_django.urls', namespace='social')),
    path('accounts/', include('allauth.urls')),
    # раздел администратора
    path('admin/', admin.site.urls),
    path("", include("posts.urls")),
    path("", include("likes.urls")),
    # flatpages
    path('about/', include('django.contrib.flatpages.urls')),
    path('about-us/', views.flatpage, {'url': '/about-us/'}, name='about'),
#  регистрация и авторизация
    path("auth/", include("users.urls")),
#  если нужного шаблона для /auth не нашлось в файле users.urls —
    #  ищем совпадения в файле django.contrib.auth.urls
    path("auth/", include("django.contrib.auth.urls")),

    path("carousel/", include("cms.urls")),


    path('captcha/', include('captcha.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

handler404 = "posts.views.page_not_found" # noqa
handler500 = "posts.views.server_error" # noqa

