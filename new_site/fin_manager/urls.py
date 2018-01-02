from django.conf.urls import url
import django.contrib.auth.views as auth_view
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="index"),
    url(r'^login/$', auth_view.login, {'template_name': 'login.html'}, name='login'),
    url(r'^wallet/add/$', views.NewWalletView.as_view(), name='wallet-add' ),
    url(r'^wallet/(?P<pk>[\w ]+)/delete/$', views.DeleteWalletView.as_view(), name='wallet-delete' ),
    url(r'^wallet/(?P<pk>[\w ]+)/edit/$', views.EditWallet.as_view(), name="wallet-edit"),
    url(r'^wallet/(?P<name>[\w ]+)/detail/$', views.WalletDetailView.as_view(), name="wallet-info"),
    url(r'^logout/$', auth_view.logout, {'next_page': '/'}, name='logout'),
    url(r'^user/$', views.UserView.as_view(), name='user')
#    urlpatterns(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': path.join(path.dirname(__file__), 'static')}),

]