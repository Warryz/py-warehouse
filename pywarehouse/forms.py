from django import forms

from .models import Article


class NewArticleForm(forms.ModelForm):
    '''
    Required:
    - Name: Textfield
    - Article Number: Numberfield
    - Amount: Numberfield
    - Warehouse: Textfield or Dropdown
    - StorageUnit: Number
    - Shelf: Number
    '''
    # article_name_form = forms.CharField(
    #     widget=forms.TextInput(), max_length=40)
    # article_number_form = forms.IntegerField(min_value=1)
    # article_amount_form = forms.IntegerField(min_value=0)

    # # Other stuff
    # article_warehouse_form = forms.CharField()
    # article_storage_unit_form = forms.CharField()
    # article_shelf_form = forms.CharField()

    class Meta:
        model = Article
        fields = ['name', 'article_number', 'amount']
