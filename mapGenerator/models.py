## Representa um Link (Endereço Web).
# from django.forms import ModelForm

class Link:
    """
    Representa um Link (Endereço Web).
    """
    def __init__(self,title,url,conteudo):
        self.title = title
        self.url = url
        self.conteudo = conteudo

    def to_dict(self):
        return {
            'title': self.title,
            'url': self.url
        }

    def __str__(self):
        return f'\n{self.title} = {self.url}\n{self.conteudo}\n'

