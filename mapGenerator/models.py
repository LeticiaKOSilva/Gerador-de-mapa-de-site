## Representa um Link (Endereço Web).
class Link:


    def __init__(self, title,url):
        self.title = title
        self.url = url

    def __str__(self):
        return f'{self.title} = {self.url}'
