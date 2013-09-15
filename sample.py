from fm_rest_class import FmRestApi

freshmail = FmRestApi('e067628c1632dc586858d6f7504ebd1f', '774f8a5fa2e197b3dd4fb54db13d8c12bd772a4e')


# Ping
response = freshmail.do_request('ping')


# Add subsriber
#data = {'email': 'szymanski.lukasz88@gmail.com', 'list': '61m6ckzazt'}
#response = freshmail.do_request('subscriber/add', data)


print response
