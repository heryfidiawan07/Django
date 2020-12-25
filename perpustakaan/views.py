from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
# from django.http import HttpResponse

def buku(request):
	# return HttpResponse('Halaman Buku')
	books = Buku.objects.all()
	# books = Buku.objects.filter(kelompok_id__nama='value')
	# LIMIT DATA
	# books = Buku.objects.all()[:3]
	title = "Variable title"
	array = ['satu', 'dua', 'tiga']
	
	konteks = {
		'title': title,
		'array': array,
		'books': books,
	}
	return render(request, 'buku.html', konteks)

def tambah_buku(request):
	if request.POST:
		form = FormBuku(request.POST)
		if form.is_valid():
			form.save()
			form = FormBuku()
			pesan = 'Data berhasil di simpan'
			konteks = {
				'form': form,
				'pesan': pesan,
			}
			return render(request, 'tambah-buku.html', konteks)
	else:
		form = FormBuku()
		konteks = {
			'form': form,
		}

	return render(request, 'tambah-buku.html', konteks)

def ubah_buku(request, id_buku):
	buku = Buku.objects.get(id=id_buku)
	if request.POST:
		form = FormBuku(request.POST, instance=buku)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data berhasil di update')
			return redirect('ubah_buku', id_buku=id_buku)
	else:
		form = FormBuku(instance=buku)
		konteks = {
			'form': form,
			'buku': buku,
		}
	return render(request, 'ubah-buku.html', konteks)
