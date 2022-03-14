from django.urls import path
from django.urls.resolvers  import URLPattern
from .views import SnackDetailView, SnackListView, SnackCreateView, SnackUpdateView, SnackDeleteView


urlpatterns = [
    path('', SnackListView.as_view(), name='List_view'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
    path('new/', SnackCreateView.as_view(), name='snack_create'),
    path('', SnackUpdateView.as_view(), name='update_view'),
    path('', SnackDeleteView.as_view(), name='delete_view')
    

]