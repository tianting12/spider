#_*_coding:utf-8_*_
#作者       ：  Deth
#创建时间    : 2020/3/11 19:21
#文件       ： forms. py
# IDE       : PyCharm

from  django import forms

class Add_english(forms.Form):

    geneder=(
        ('名词', 'n'),
        ('带词', 'prep'),
        ('动词', 'v'),
        ('形容词', 'adj'),
        ('副词', 'adv'),
        ('数词', 'num'),
        ('冠词', 'art'),
        ('连词', 'conj'),
        ('感叹词', 'int'),
    )
    word = forms.CharField(label="单词", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    word_chinese = forms.CharField(label="意思", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cx = forms.ChoiceField(label='词性', choices=geneder)