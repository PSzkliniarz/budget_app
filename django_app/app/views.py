from rest_framework.response import Response
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer


class AccountsView(generics.RetrieveAPIView):
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)
