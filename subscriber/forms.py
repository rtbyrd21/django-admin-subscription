
from __future__ import absolute_import
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit
from subscriber.models import Catalog, Article, Issue, Annual

from . import models

class OrderListForm(forms.ModelForm):


    articles = forms.ModelChoiceField(queryset=Catalog.objects.get().article_products.all())
    issues = forms.ModelChoiceField(queryset=Catalog.objects.get().issue_products.all())
    annuals = forms.ModelChoiceField(queryset=Catalog.objects.get().annual_products.all())
    #
    # annuals = forms.ModelChoiceField(queryset=Annual.objects.all())
    # issues = forms.ModelChoiceField(queryset=Issue.objects.all())
    # articles = forms.ModelChoiceField(queryset=Article.objects.all())


    class Meta:
        fields = (
                    'annuals',
                    'issues',
                    'articles',)
        model = models.Order



    def __init__(self, *args, **kwargs):
        super(OrderListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                    'annuals',
                    'issues',
                    'articles',
            ButtonHolder(
                Submit('create', 'Create')

            )


        )


