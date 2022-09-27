import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


web = webdriver.Chrome(executable_path=r'C:/Users/User/chromedriver_win32/chromedriver.exe')
web.get("https://townhall.virginia.gov/L/entercomment.cfm?GdocForumID=1953")
time.sleep(5) # Let the user actually see something + page load time

boob = ['Leave trans kids alone', 'I oppose this bill', 'This bill is garbage', 'Quit using kids as political tools. I oppose this bill!', 'I strongly oppose this bill', 'You cant legislate trans people away',
    'Trans Rights are human rights', 'Please reconsider pushing this bill']

fnames = [
    "Liam",
    "Anya",
    "Olivia",
    "Emma",
    "Charlotte",
    "Pari",
    "Anika",
    "Navya",
    "Angel",
    "Diya",
    "Myra",
    "Sara",
    "Iraa",
    "Amelia",
    "Ava",
    "Sophia",
    "Riya",
    "Isabella",
    "Mia",
    "Evelyn",
    "Eva",
    "Shanaya",
    "Kyra",
    "Harper",
    "Theodore",
    "Henry",
    "Lucas",
    "Vivian",
    "Benjamin",
    "William",
    "Will",
    "Robbie",
    "James",
    "Elijah",
    "Oliver",
    "Noah",
    "Hazel",
    "Violet",
    "Aurora",
    "Zoe",
    "Leah",
    "Sai",
    "Lillian",
    "Ruby",
    "Bella",
    "Sadie",
    "Anna",
    "Emery",
    "Adeline",
    "Ayla",
    "Rose",
    "Parker",
    "Lyla",
    "Remi",
    "Mackenzie",
    "Josie",
    "Melanie",
    "Daisy",
    "Kaylee"
  ]

surnames = [
    "Smith",
    "Johnson",
    "Williams",
    "Brown",
    "Jones",
    "Garcia",
    "Miller",
    "Davis",
    "Rodriguez",
    "Wilson",
    "Anderson",
    "Thomas",
    "Gill",
    "Taylor",
    "Moore",
    "Jackson",
    "Martin",
    "Lee",
    "Thompson",
    "White",
    "Harris",
    "Dillon",
    "Clark",
    "Sanchez",
    "Lewis",
    "Walker",
    "Robinson",
    "Young",
    "Allen",
    "King",
    "Wright",
    "Scott",
    "Torres",
    "Nguyen",
    "Hill",
    "Bhasin",
    "Adams",
    "Baker",
    "Hall",
    "Campbell",
    "Carter",
    "Ray",
    "Evans",
    "Turner",
    "Edwards",
    "Collins",
    "Reyes",
    "Cook",
    "Rogers",
    "Morgan"
  ]

flen = len(fnames)
slen = len(surnames)

def fill():


    fname = fnames[random.randint(0, flen-1)]
    sname = surnames[random.randint(0, slen-1)]
    name = fname + " " + sname
    print(name)

    cum = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[1]/div[1]/input')
    cum.send_keys(name)
     
fill()

time.sleep(2)

fboob = len(boob)

def filler():

    fcum = boob[random.randint(0, fboob-1)]
    commie = fcum 
    print(commie)

    scum = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[3]/input')
    scum.send_keys(commie)
     
filler()

def poster():

    spost = boob[random.randint(0, fboob-1)]
    posty = spost
    print(posty)

    addComment = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[3]/input')
    addComment.send_keys(Keys.TAB)

    #scrum = web.find_element('xpath', '')
    #scrum.send_keys(posty)
poster()



