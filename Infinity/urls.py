from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Infinity import views as infinityViews
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='HomePage/')),
    path('HomePage/', infinityViews.HomePage),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

