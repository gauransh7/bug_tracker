from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knox import views as knox_views
from tracker import views

router = DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'issue', views.IssueViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'tag', views.TagViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'issuemedia', views.IssueMediaViewSet)
router.register(r'whoami', views.WhoAmIViewSet, basename='whoami')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/<code>', views.AuthView.as_view()),
    path('api-auth/login/', views.LoginView.as_view(), name='knox_login'),
    path('api-auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('api-auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]