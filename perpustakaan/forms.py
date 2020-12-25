from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
	class Meta:
		model = Buku
		fields = '__all__'
		# exclude = ['penerbit']

		widgets = {
			'judul': forms.TextInput({'class':'form-control form-control-sm mb-2'}),
			'penulis': forms.TextInput({'class':'form-control form-control-sm mb-2'}),
			'penerbit': forms.TextInput({'class':'form-control form-control-sm mb-2'}),
			'kelompok_id': forms.Select({'class':'form-control form-control-sm mb-2'}),
			'jumlah': forms.NumberInput({'class':'form-control form-control-sm mb-2'}),
		}