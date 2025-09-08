print('                contact book')
contacts={
    "aya":'01027801018',
    "ahmed":'0102389656',
    "ali":'01028090876'
}
print(contacts.keys())
search_name=input("enter the name:")
if search_name in contacts:
    print(f"{contacts[search_name]}")
else:
    print('something is wrong')
    
