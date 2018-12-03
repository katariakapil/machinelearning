# redis insert key
import redis
r = redis.StrictRedis(host='localhost', port=12000, db=0)
print ("..set key1 123")
r.set('key1', '123')
r.set('key2', '2123')
r.set('key3', '3123')
r.set('key4', '4123')
print ( r.set('key1', '123'))
print ("get key1")
print(r.get('key1'))


#dynamo db insert item 
import boto3

dynamoDb  = boto3.resource('dynamodb')

dynamoTable = dynamoDb.Table('product')

dynamoTable.put_item (

    Item = {
        "productId" :  "12345",
        "productName" : "Tee Shirt",
        "SKU" : "SKU1234"
    }

)
