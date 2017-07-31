# pip install facebook-sdk
import facebook

app_id = '1323041221074517'
app_secret = '8a146be4fa693a903e6b44d8a5fbf68b'
access_token = 'EAASzTIoBXlUBAAtZCu0jmhuv6hzboasI8UPChO2JXtwujD4ov6HUidj1zupbuDhEyysUUPIsVir5jX4Y0fOrGJWnqEKQ531djkvj' \
               'Vuq0pT7YFhierZA6bNRj9eXBvAojUKCq9VmXpsUZCZAZA5ZAMKlhUXWAqYsZA4rmB5rtSj4Ur4tmpAzVFu4qBxdZBSb3gawZD'
#connection to GraphAPI
graph = facebook.GraphAPI(access_token=access_token, version='2.7')

"""extend token (2m)"""
# newToken = newTokengraph.extend_access_token(app_id=app_id, app_secret=app_secret)
# print(newToken)

"""token status"""
# gDAT = graph.debug_access_token(token=access_token, app_id=app_id,app_secret=app_secret)
# print(dDAT)

"""posting to facebook"""
# graph.put_object('347168878964525', 'feed', message='Hello World')

"""get object"""
# fields = 'feed{comments{comments,created_time,message},message,likes,created_time}'
# post = graph.get_object(id='347168878964525', fields=fields)
# print(post)

'''not done'''
# graph.put_object(
#     parent_object='347168878964525',
#     connection_name='feed',
#     message='',
#     link=''
# )


