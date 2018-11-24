import requests
def calc_age(uid):
    url_need = 'https://api.vk.com/method/'
    vk_method_need = 'friends.get'
    payload = {'v'              :'5.71', 
               'access_token'   :'17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
               'user_id'        :uid,
               'order'          :'name',
               'fields'         :'bdate',
               }
    return requests.get(url_need+vk_method_need,params=payload)
    
print(__name__)

if __name__ == '__main__':
    res = calc_age('176667991')
    try:
        j = res.json()
    except JSONDecodeError:
        print('net Dannyh')

    for i in j['response']['items']:
        id = i['id']
        first_name = i['first_name']
        last_name = i['last_name']
        try:
            bdate = i['bdate']
        except KeyError:
            bdate  = 'qqqqq'
        print(str(first_name)+';'+str(last_name)+';'+str(id)+';'+str(bdate))

