import requests
from bs4 import BeautifulSoup

from write import write_to_excel

def get_links(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  links = soup.find_all('a')
  return links

url = 'https://www.ey.com'
links = get_links(url)
arr=[]
for link in links:
      
      # if 'https:' not in link['href']:
      #     # print('https://www.ey.com'+link['href'])
      #     arr.append('https://www.ey.com'+link['href'])
      # else:
      #     # print(link['href'])
      #     arr.append(link['href'])
      try:
        print(link['href'])
      except:
        continue
      
# temp=[]
# final=[]    
# for a in arr:
#   if 'https://www.ey.com' in a:
#     # print(a)
#     temp.append(a)
#   final.append(temp)
#   temp=[]

# print(final)

# while([] in final):
#     final.remove([])

# write_to_excel(final)