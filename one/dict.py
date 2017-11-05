sArray = {
  'day':'Wednessday',
  'animal': 'Cat',
  'id': 2
}
print(sArray['day'])
  #Wednessday

del sArray['id']
print(sArray)
  #{'day': 'Wednessday', 'animal': 'Cat'}
 
sArray['id2'] = '00551'
print(sArray)
  #{'day': 'Wednessday', 'animal': 'Cat', 'id2': '00551'}
 
sArray.update({ 'id': '004156', 'newKey': 'value' })
print(sArray)
  #{'day': 'Wednessday', 'animal': 'Cat', 'id2': '00551', 'id': '004156', 'newKey': 'value'}
  
for eachKey in sArray:
  print(sArray[eachKey])
  #Wednessday
  #Cat
  #004156
  