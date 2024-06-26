from django.conf import settings
from functools import partial
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from leerming.core import views as core_views
from health_check.views import MainView
from django.contrib.auth.decorators import login_required
from leerming.profiles.decorators import profile_required
from decorator_include import decorator_include

decorator_include_login_and_profile = partial(
    decorator_include,
    (login_required, profile_required),
)

urlpatterns = [
    path("", core_views.home, name="home"),
    path("about/", core_views.about, name="about"),
    path(".well-known/security.txt", core_views.security_txt),
    path("robots.txt", core_views.robots_txt),
    path("android-chrome-192x192.png", core_views.favicon),
    path("android-chrome-512x512.png", core_views.favicon),
    path("apple-touch-icon.png", core_views.favicon),
    path("browserconfig.xml", core_views.favicon),
    path("favicon-16x16.png", core_views.favicon),
    path("favicon-32x32.png", core_views.favicon),
    path("favicon.ico", core_views.favicon),
    path("mstile-150x150.png", core_views.favicon),
    path("safari-pinned-tab.svg", core_views.favicon),
    path("health/", MainView.as_view()),
    path("accounts/", include("allauth.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        "profiles/",
        decorator_include(
            login_required, "leerming.profiles.urls", namespace="profiles"
        ),
    ),
    path(
        "flashcards/",
        decorator_include_login_and_profile(
            "leerming.flashcards.urls", namespace="flashcards"
        ),
    ),
    path(
        "reviews/",
        decorator_include_login_and_profile(
            "leerming.reviews.urls", namespace="reviews"
        ),
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        path("__debug__/", include("debug_toolbar.urls")),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
