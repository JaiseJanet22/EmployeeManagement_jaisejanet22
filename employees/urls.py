from django.urls import path
from .views import CustomTokenObtainPairView, RegisterView, EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),

]
