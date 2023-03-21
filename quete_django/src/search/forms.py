from django import forms

class ProductSearchForm(forms.Form):
    code_barre = forms.CharField(label="Code barre du produit", max_length=13)

class ProductReplacementForm(forms.Form):
    nom = forms.CharField(label="Nom du produit de remplacement", max_length=100)
    description = forms.CharField(label="Description du produit de remplacement", widget=forms.Textarea)
    photo = forms.ImageField(label="Photo du produit de remplacement")