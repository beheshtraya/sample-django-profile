from django.contrib import admin
from django.urls import path, include

from utils.router import CustomRouter
from user_app.urls import router as user_app_router

router = CustomRouter(trailing_slash=False)
router.extend(user_app_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
