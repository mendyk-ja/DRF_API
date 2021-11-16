from snippets.models import UploadImageTest
from snippets.serializers import ImageSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import permissions


class ImageViewSet(viewsets.ModelViewSet):
    """
    This viewset provides 'list' and 'create' actions.

    """
    queryset = UploadImageTest.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'images': reverse('images-list', request=request, format=format)
    })
