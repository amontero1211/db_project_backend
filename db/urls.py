from rest_framework import routers
from .models import ArtWork
from .api import ArtworkViewSet, ArtistViewSet, InvoiceViewSet, PurchaserViewSet


router = routers.DefaultRouter()

router.register('api/artworks', ArtworkViewSet, 'artworks')
router.register('api/artists', ArtistViewSet, 'artists')
router.register('api/invoice', InvoiceViewSet, 'invoice')
router.register('api/purchaser', PurchaserViewSet, 'purchaser')

urlpatterns = router.urls
