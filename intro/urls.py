from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from profiles import views as profileviews

class MyRegistrationView(RegistrationView):
	def get_success_url(self,user):
		return '/profiles/edit/2/'

urlpatterns = [
	url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
	url(r'^accounts/', include('registration.backends.simple.urls')),
	url(r'^profiles/', include('profiles.urls')),	
    url(r'^admin/', admin.site.urls),
    url(r'^$', profileviews.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)