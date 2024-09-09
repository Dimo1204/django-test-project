from django import forms


class AddProductForm(forms.Form):
    title = forms.CharField(max_length=10, label="Название", widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.IntegerField(label="Цена")