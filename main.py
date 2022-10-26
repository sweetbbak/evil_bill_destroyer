import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()

driver = webdriver.Chrome(executable_path=r'C:/Users/User/chromedriver_win32/chromedriver.exe')
driver.get("https://townhall.virginia.gov/L/entercomment.cfm?GdocForumID=1953")

names = fake.name()


## check if its the right page by looking at the title and add a name
assert "Virginia Regulatory Town Hall Enter A Comment" in driver.title
elem = driver.find_element(By.NAME, "UUName")
elem.clear()
elem.send_keys(names)

boob = ['Leave trans kids alone', 'I oppose this bill', 'This bill is garbage', 'Quit using kids as political tools. I oppose this bill!', 'I strongly oppose this bill', 'You cant legislate trans people away',
    'Trans Rights are human rights', 'Please reconsider pushing this bill', 'Oppose Gov Youngkins Transgender and Anti-CRT Policies', 'Trans rights matter', 'Trans people are real!! Do we have to say this?', 'Trans Liberation now', 'GOP hate on full display',
   'DNC hate on full display! Parental right ARE human rights & LGBTQIA isn’t under attack here! Read!!!', 'I strongly disagree with this policy. Trans rights ARE human rights and we will not be silenced.', 'Persecuting Trans Kids is a shameful political stunt'
   'Trans rights!!', 'THESE POLICIES WILL KILL KIDS !!!', 'STRONGLY OPPOSE - This will harm children', 'I STRONGLY OPPOSE This Policy', 'Oppose! This bill is insanity and will harm trans youth!', 'You’re going to get kids killed doing this', 'Trans kids are awesome and deserve the same respect we all want',
   'Bigotry has no place in law', 'As a Libertarian I STRONGLY oppose this government OVERREACH', 'How is this supposed to be small government??', 'Why dont you pass laws that ACTUALLY HELP PEOPLE']


time.sleep(.5)

states = random.randint(0, 48)
addComment = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[1]/div[1]/div[2]/select')
addComment.send_keys(Keys.ARROW_DOWN * states)

mails = fake.email()
email = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[1]/div[2]/input')
email.send_keys(mails)

subjects = random.choice(boob)
comment = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[1]/div[3]/input')
comment.send_keys(subjects)

bodyx = ["The consequences of not affirming a child’s gender identity can be severe, and it can interfere with their ability to develop and maintain healthy interpersonal relationships. In the school context, that distress will also hinder a transgender student’s focus in class and ability to learn. The longer a transgender youth is not affirmed, the more significant and long-lasting the negative consequences can become, including loss of interest in school, heightened risk for alcohol and drug use, poor mental health and suicide. -Gender Spectrum et al., 2015, Schools in Transition—A Guide for Supporting Transgender Students in K-12 Schools 8 (2015)", 
"When transgender students are denied access to facilities that align with their gender identity, they often avoid participating in sports, gym and refrain from using the bathroom altogether. Bathroom avoidance is a common problem for transgender students and is linked to medical problems and diminished educational outcomes. For instance, in a 2013 study conducted by the Williams Institute, 54 percent of transgender respondents reported some sort of health problem related to bathroom avoidance, including dehydration, urinary tract infections, kidney infections and other kidney problems.", "Students will not be the only ones harmed by the proposed guidance. Too often educators are required to enforce needlessly discriminatory policies by those who lack direct contact or relationships with the students and parents harmed by such policies. Policies that segregate transgender students their peers are not self-executing: they compel individual administrators, educators, and other public school employees to carry them out. Educators suffer both professional and psychological harms when they are forced to watch, and participate in, the stigmatization and degradation that discriminatory policies inflict on children.",
"It has been shown that allowing students to use restrooms and locker rooms consistent with their gender identity is just one of a host of school policies that have been shown to improve the educational experiences of transgender, gender nonconforming, and cisgender students. In schools with policies that explicitly prohibit anti-LGBTQ bullying, students have better relationships with staff and as a result feel safer in the school. When transgender students are respected, they are able to engage fully and equitably with the educational experience, and when that happens, transgender students, like all students, are able to thrive", "School policies that respect transgender students not only benefit transgender students, but also promote a positive school climate for all students. School climate—that is, the “product of the interpersonal relationships among students, families, teachers, support staff and administrators” that sets the “norms, values, and expectations that support people feeling socially, emotionally, and physically safe” in school—is a key predictor of student engagement, student mental and physical health, and academic achievement, and is positively correlated with decreased absenteeism, dropout rates, and suspensions",
 "Allowing discrimination against one group infects antidiscrimination efforts against others. Schools cannot embrace diversity, tolerance, and mutual respect in some ways, but deny it in others and still obtain the benefits of inclusive classrooms. Students who see their transgender peers being treated as “less than” justifiably fear that they one day will be treated as “less than” as well."]

numby = random.choice(bodyx)
paragraph = comment.send_keys(Keys.TAB, numby) 


imageOne = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[4]/div[2]/table/tbody/tr/td[1]/img[1]')
imageTwo = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[4]/div[2]/table/tbody/tr/td[1]/img[2]')
#username = driver.find_element(By.NAME, 'username')
print(imageOne.get_attribute("outerHTML"))
print(imageTwo.get_attribute("outerHTML"))

imgString = imageOne.get_attribute("outerHTML")
img2String = imageTwo.get_attribute("outerHTML")

#<img src="../graphics/letters/LetterI.gif" style="vertical-align: middle" border="0" alt="letter">
#this might be  stupid for me but these dummies also made a captcha and put the letters in the html. Notice "LetterI.gif" lmao
#fight stupidity with stupidity

captcha = imgString.split("""<img src="../graphics/letters/Letter""")
print(captcha)

find_letter = imgString[36]
find_letter2 = img2String[36]
cappy = (find_letter + find_letter2)

print(cappy)

capbox = driver.find_element('xpath', '/html/body/div[5]/div[6]/form/div[4]/div[2]/table/tbody/tr/td[2]/input')
capbox.send_keys(cappy)

submit = driver.find_element('xpath', '//*[@id="submit"]')
#submit.click()
time.sleep(1)