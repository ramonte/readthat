# -*- coding: utf-8 -*-

from django import forms

from . import models as m

class ForumForm(forms.ModelForm):
    title = forms.CharField(label='Título', widget=forms.Textarea(attrs={'class': 'browser-default'}))
    description = forms.CharField(label='Descrição', widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))

    def __init__(self, *args, **kwargs):
        super(ForumForm, self).__init__(*args, **kwargs)

    def label_book(self, obj):
        return obj.title

    def label_author(self, obj):
        return obj.name

    class Meta:
        model = m.Forum
        fields = ('title', 'description')

class CommentForm(forms.ModelForm):
    description = forms.CharField(label='Comentário', widget=forms.Textarea(attrs={'cols': 80, 'rows': 20, 'class': 'browser-default'}))
    class Meta:
        model = m.Comment
        fields = ['description']
