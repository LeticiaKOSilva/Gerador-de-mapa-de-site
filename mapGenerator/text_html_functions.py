from bs4 import BeautifulSoup

def remove_tags_from_HTML(soup: BeautifulSoup):
    return soup.get_text()

def head_remove(soup: BeautifulSoup):
    soup.head.decompose()
    return soup

def get_title_tags(soup: BeautifulSoup):
    """
    Obtem as tags de titulo de uma pagina HTML como title,h1,h2,h3 etc.
    """
    title_tags = soup.find_all(['body'])
    titles = [tag.get_text() for tag in title_tags]
    
    return titles

def get_all_tag_names(soup: BeautifulSoup):
    tags = [tag.name for tag in soup.find_all()]
    return tags
