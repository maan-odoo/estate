import xmlrpc.client

db = "test"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

# print(common.version())

# if uid:
#     print ("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

# if models.execute_kw(db, uid, password, 'estate.properties', 'create', [{'name': 'Xmlrpc', 'state': 'new','excepted_price':'5000','postcode':'382870','date_avalibility':'2022-03-24','bedrooms':'3',}]):
#     print("Successfully created property")


# to_confrim_ids = models.execute_kw(db, uid, password, 'estate.properties', 'search', [['|', ('name', '=', 'new'), ('name', '=', 'Xmlrpc')]])
# print ("\n\nto_confrim_id ::: ", to_confrim_ids)

# result = models.execute_kw(db, uid, password, 'estate.properties', 'cancel_property', [to_confrim_ids])

# result = models.execute_kw(db, uid, password, 'estate.properties', 'search_read', [[], ['name', 'description', 'state']])

# print ("\n\nresult is ::: ", result)

# if models.execute_kw(db, uid, password, 'estate.properties', 'write', [{'name': 'Xmlrpc', 'state': 'new','excepted_price':'5000','postcode':'382870','date_avalibility':'2022-03-24','bedrooms':'3',}]):
#     print("Successfully created property")

# s =  models.execute_kw(db, uid, password,
#     'estate.properties', 'search',
#     [[['state', '=', 'cancel']]],{'limit':1})
# print("Cancelled Properties",s)

# models.execute_kw(db, uid, password, 'estate.properties', 'write', [[s], {'name':'canceled'}],{'raise_exception': False})
# get record name after having changed it
# models.execute_kw(db, uid, password, 'estate.properties', 'state_get', [[id]])

# s = models.execute_kw(db, uid, password,
#     'estate.properties', 'search_count',
#     [[['state', '=', 'cancel']]])


# print("Cancelled Properties count : ",s)






# if models.execute_kw(db, uid, password,'res.partner', 'check_access_rights',['unlink'], {'raise_exception': False}):
#     if models.execute_kw(db, uid, password, 'estate.properties', 'create', [{'name': 'Xmlrpc', 'state': 'new','excepted_price':'5000','postcode':'382870','date_avalibility':'2022-03-24','bedrooms':'3',}]):
#         print("Property Deleted")
#     else:
#         print('Property not found')


id = models.execute_kw(db, uid, password,
    'estate.properties', 'search',
    [[['name', '=', 'new 1']]],{'limit':1})
print(id)
# models.execute_kw(db, uid, password, 'estate.properties', 'unlink', [[id]])



