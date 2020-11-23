from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    PUR = [
        (1, '자유게시판'),
        (2, '건의게시판'),
        (3, '추천게시판'),
    ]
    purpose = forms.IntegerField(
        label='게시판',
        widget=forms.Select(
                choices = PUR,
                attrs={
                    'style': 'width: 10rem;'
                }
            )
    )

    title = forms.CharField(
        label='제목',
    )


    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'rows': 10
            }
        )
    )

    class Meta:
        model = Article
        fields = ['purpose', 'title', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows': 1
            }
        )
    )
    class Meta:
        model = Comment
        fields = ['content']
