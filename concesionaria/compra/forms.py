from django import forms

class AutomovilFormulario (forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    color = forms.CharField()
    km = forms.IntegerField()
    año = forms.IntegerField()
    precio = forms.IntegerField()
    patente = forms.CharField()
    vtv_hecha = forms.CharField()