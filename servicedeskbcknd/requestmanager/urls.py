from rest_framework.routers import DefaultRouter
from .views import BusinessSystemViewSet, PriorityDictionaryViewSet

app_name = 'redbutton'

router = DefaultRouter()
router.register('bslist', BusinessSystemViewSet, basename='bslist')
router.register('priority', PriorityDictionaryViewSet, basename='prioritylist' )


urlpatterns = [



]

urlpatterns +=router.urls