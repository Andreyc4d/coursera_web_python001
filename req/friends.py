import requests
import sys
def calc_age(uid):
    url_need = 'https://api.vk.com/method/'
    vk_method_need = 'friends.get'
    if not uid.isdigit():
        payload = {'v'              :'5.71', 
                   'access_token'   :'17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
                   'user_ids'       :uid,
                   'order'          :'name',
                  }
        r = requests.get(url_need+'users.get',payload)
        try:
            tmp = r.json()
            tmp = tmp['response'][0]
            uid = tmp['id']
        except JSONDecodeError:
            print('No data in json screen_name')

            
    payload = {'v'              :'5.71', 
               'access_token'   :'17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
               'user_id'        :uid,
               'order'          :'name',
               'fields'         :'bdate',
              }
    res = requests.get(url_need+vk_method_need,params=payload)
    try:
        j = res.json()
    except JSONDecodeError:
        print('No data in json friens.get')
                                                                              
    lst = dict()
                                                                              
    for i in j['response']['items']:
        id = i['id']
        first_name = i['first_name']
        last_name = i['last_name']
        try:
            bdate = i['bdate']
        except KeyError:
            bdate  = 'qqqqq'
        if bdate.count('.') == 2:
            age  = 2018 - int(bdate[len(bdate)-4:])
            #if age >= 100:
            #    print(first_name+' ' + last_name+ ' : '+str(age)+': ' + str(bdate))
            #try:
                #lst[age] = lst[age]+1
            #except KeyError:
                #lst[age] = 1
            lst[age] = lst.setdefault(age,0) + 1 #replace 4 string upper
        #print(str(first_name)+';'+str(last_name)+';'+str(id)+';'+str(bdate))
    return lst
    

if __name__ == '__main__':
    try:
        user_id = str(sys.argv[1])
    except IndexError:
        user_id = '12254363'
    res = calc_age(user_id)
    print(res)
