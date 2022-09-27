import time
import random
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


web = webdriver.Chrome(executable_path=r'C:/Users/User/chromedriver_win32/chromedriver.exe')
web.get("https://townhall.virginia.gov/L/entercomment.cfm?GdocForumID=1953")

time.sleep(2) # Let the user actually see something + page load time

boob = ['Leave trans kids alone', 'I oppose this bill', 'This bill is garbage', 'Quit using kids as political tools. I oppose this bill!', 'I strongly oppose this bill', 'You cant legislate trans people away',
    'Trans Rights are human rights', 'Please reconsider pushing this bill', 'Oppose Gov Youngkins Transgender and Anti-CRT Policies', 'Trans rights matter', 'Trans people are real!! Do we have to say this?', 'Trans Liberation now', 'GOP hate on full display',
   'DNC hate on full display! Parental right ARE human rights & LGBTQIA isn’t under attack here! Read!!!', 'I strongly disagree with this policy. Trans rights ARE human rights and we will not be silenced.', 'Persecuting Trans Kids is a shameful political stunt'
   'Trans rights!!', 'THESE POLICIES WILL KILL KIDS !!!', 'STRONGLY OPPOSE - This will harm children', 'I STRONGLY OPPOSE This Policy', 'Oppose! This bill is insanity and will harm trans youth!', 'You’re going to get kids killed doing this', 'Trans kids are awesome and deserve the same respect we all want',
   'Bigotry has no place in law', 'As a Libertarian I STRONGLY oppose this government OVERREACH', 'How is this supposed to be small government??', 'Why dont you pass laws that ACTUALLY HELP PEOPLE']

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

    y = random.randint(0, 48)
    fname = fnames[random.randint(0, flen-1)]
    sname = surnames[random.randint(0, slen-1)]
    name = fname + " " + sname
    print(name)

    cum = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[1]/div[1]/input')
    cum.send_keys(name)

    addComment = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[1]/div[2]/select')
    addComment.send_keys(Keys.TAB)
    print("tab")

    time.sleep(1)
    addComment.send_keys(Keys.ARROW_DOWN * y)
    print('tab')
    #state = web.find_element('xpath', '//*[@id="content"]/div[6]/form/div[1]/div[1]/div[2]/select')
    #state.send_keys(Keys.ARROW_DOWN * y)
     
fill()

time.sleep(1)

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
    addComment.send_keys(Keys.TAB + posty)
    time.sleep(1)

    submit = web.find_element('xpath', '//*[@id="submit"]')
    #submit.send_keys(Keys.ENTER + Keys.ENTER)
    submit.click()
    time.sleep(3)
    web.get('https://townhall.virginia.gov/L/entercomment.cfm?GdocForumID=1953')
    time.sleep(5)
    fill()
    time.sleep(2)
    filler()
    time.sleep(1)
    poster()


poster()


    
    




