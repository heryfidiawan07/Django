from django.conf.urls import url
from django.contrib import admin
from perpustakaan.views import buku, tambah_buku, ubah_buku

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^buku/', buku),
    url(r'^tambah-buku/', tambah_buku, name='tambah_buku'),
    #url(r'^buku/edit/<int:id_buku>', ubah_buku, name='ubah_buku'),
    url(r'^edit-buku/(?P<id_buku>\d+)/$', ubah_buku, name='ubah_buku'),
]
