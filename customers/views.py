from customers.models import Customer
from customers.serializers import CustomerSerializer
from rest_framework import generics


# Create your views here.
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = Customer
