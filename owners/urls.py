from owners.views import OwnerView
from django.urls import path
from .views import OwnerView

urlpatterns = [
    path('/owner', OwnerView.as_view())

]
