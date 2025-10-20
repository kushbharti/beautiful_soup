from bs4 import BeautifulSoup


with open('home.html','r') as html_file:
    content = html_file.read()
  
  
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    
    heading_tags = soup.find_all('div', class_ = 'card')
    # print(tags)
    
    for course in heading_tags: 
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'Course Name: {course_name} ===> Price: {course_price}')
        print('\n')
    