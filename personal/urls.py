from rest_framework import routers
from .views import DepartmentView, PersonnelView

router = routers.DefaultRouter()
router.register("department", DepartmentView)
router.register("personnel", PersonnelView)

urlpatterns = [
    
]

urlpatterns += router.urls