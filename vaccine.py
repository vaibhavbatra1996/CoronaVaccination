import json
import requests
import datetime

def sendSMS(text):
    url = "https://www.fast2sms.com/dev/bulk"

    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'FSTSMS',

        # Put your message here!
        'message': text,

        'language': 'english',
        'route': 'p',

        # You can send sms to multiple numbers
        # separated by comma.
        'numbers': '9953412700'
    }

    # create a dictionary
    headers = {
        'authorization': 'kfmJhDln8GIw0T6BYVuqoZPNbXy7iCdKH2xaRLzjpW34rgMFAenSfKote3Wb1gRkXIOq9CpQ0vUrcZ8G',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST",
                                url,
                                data=my_data,
                                headers=headers)

    returned_msg = json.loads(response.text)

    # print the send message
    print(returned_msg['message'])


url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=142&date="
f_url = url+str(format(datetime.date.today(),'%d-%m-%Y'))
payload={}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.request("GET", f_url, headers=headers, data=payload)
f_dict = json.loads(response.text)
centers = f_dict['centers']
#print(centers[0]['sessions'][1])

for i in centers:
    session = i['sessions']
    for j in session:
        age_limit = j['min_age_limit']
        if(age_limit==18):
            available = j['available_capacity']
            if(available>0):
                msg = 'Center: '+ i['name']+'---'+'Available: '+ str(available)+'---'+ 'Vaccine: '+ j['vaccine']+'---'+'Date: '+j['date']
                print(msg)
                if(available>50):
                    sendSMS(msg)
