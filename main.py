import bs4
import requests
import time
import smtplib

website = 'https://in.indeed.com/jobs?q=software%20developer&l=Goa&vjk=32dd1d4fa36260fe'
result = requests.get(website)
content= result.text
soup = bs4.BeautifulSoup(content,'lxml')

Preferred_JoTitles=['Fullstack Backend Developer','Software Engineer','React Native Developer']
Days =['1 days ago','2 days ago','3 days ago','Just posted','Today']
Loc = ['Verna, Goa','Goa','Panaji, Goa','Margao, Goa','Margao']

def details(JobTitle,Company_Name,Location,Date,Summary):
    fp=open('JobDetails.txt','a')
    content = "JobTitle : "+JobTitle+"\nCompany Name : "+Company_Name+"\nLocation : "+Location+"\nBreif Summary : "+Summary+"Posted : "+Date+"\n______________________________________________________________________________________________________________________________________________\n"
    fp.write(content)

def send_email(message):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("ravindrasawant095@gmail.com","rs095rs@")
    s.sendmail("ravindrasawant095@gmail.com","praptisawant25@gmail.com",message.encode('ascii','ignore').decode('ascii'))
    s.quit()

def email_details():
    fr=open('JobDetails.txt','r')
    msg = fr.read()
    send_email(msg)

while True:
    for jobs in soup.find_all(class_= 'job_seen_beacon'):
        JobTitle = jobs.find(class_='heading4 color-text-primary singleLineTitle tapItem-gutter').get_text()
        JT=JobTitle.replace("new","")
        date = jobs.find('span',class_='date').get_text()
        dt = date.replace("Posted","")
        Comp = jobs.find(class_='companyName').get_text()
        Location = jobs.find(class_='companyLocation').get_text()
        Summary = jobs.find(class_='job-snippet').get_text()
        if dt in Days:
            if JT in Preferred_JoTitles:
                if Location in Loc:
                    details(JT,Comp,Location,dt,Summary)

    email_details()
    fp=open('JobDetails.txt','w')
    fp.write("")
    time.sleep(264000)






