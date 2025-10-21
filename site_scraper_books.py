from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://books.toscrape.com/index.html').text

soup = BeautifulSoup(html_text , 'lxml')

main_tag_div = soup.find('div', class_='col-sm-8 col-md-9')
# print(main_tag_div)

heading_tag_div = main_tag_div.div.h1.text
# print(heading_tag_div)

warning_div = main_tag_div.find('div', class_ = 'alert alert-warning')
# print(warning_div.text)

ol_tag = main_tag_div.find('ol', class_='row')

for item in ol_tag.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3'):
    print('='*20)
    print('\n')
    
    article = item.find('article', class_='product_pod')
    div_= article.div
    
    a_tag = div_.a['href']
    img_tag_src = div_.a.img['src']
    img_tag_alt = div_.a.img['alt']
    
    h3_tag = article.find('h3')
    title = h3_tag.a['title']
    print(f'A tag href: {a_tag}')
    print(f'Image tag Src: {img_tag_src}')
    print(f'Image tag alt: {img_tag_alt}')
    print(f'Heading tag: {title}')
    
    print('\n')
    print('='*20)
    
    
    
    
    
    
    
    