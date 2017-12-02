from django import forms

from . import models as m

class ForumForm(forms.ModelForm):
    author = forms.ModelChoiceField(label='Autor', queryset=m.Author.objects.all(), widget=forms.Select(attrs={'class': 'browser-default'}))
    book = forms.ModelChoiceField(label='Livro', queryset=m.Book.objects.all(), widget=forms.Select(attrs={'class': 'browser-default'}))
    title = forms.CharField(label='Título', widget=forms.Textarea(attrs={'class': 'browser-default'}))
    description = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))

    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)

        self.fields['book'].label_from_instance = self.label_book
        self.fields['author'].label_from_instance = self.label_author

    def label_book(self, obj):
        return obj.title

    def label_author(self, obj):
        return obj.name

    class Meta:
        model = m.Forum
        fields = ('author', 'book', 'title', 'description')
