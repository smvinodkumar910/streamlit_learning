from google.cloud import firestore

client = firestore.Client()

#doc_ref = client.document('users','user_details')
#user_details = doc_ref.get();


class userObject:
    
    def __init__(self,credentials,name,key,expiry_days,preauthorized,role):
        self.credentials=credentials
        self.name=name
        self.expiry_days=expiry_days
        self.preauthorized=preauthorized
        self.role = role
        self.key = key


user = userObject('k.shanthi910','Vinodkumar Madhavan','randomkey',5,)
new_user = dict()
new_user['user_email']='vmadhavan@gmail.com'
new_user['user_name']='Vinodkumar Madhavan'
new_user['role']='admin'
new_user['password']='k.shanthi910'


#coll_ref = client.collection('users').add(new_user,new_user['user_email'])

city_list={'city_list':['chennai','mumbai','pune','hyderabad','bengaluru','surat','kolkata','ahmedabad','visakhapatnam','madurai','virudunagar']
            }
doc_ref = client.collection('cities').document('city_list') 

doc_ref.set(city_list)

doc_ref.update(city_list)

