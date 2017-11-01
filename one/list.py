

A = ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday']
B = ['Fish', 'Dog', 'Cat', 'Sheep', 'Fish']

#-------- concat ----------

A+B
print(A+B)
  # ['Monday', 'Tuesday', 'Wednessday', 'Thursday', 'Friday', 'Fish', 'Dog', 'Cat', 'Sheep', 'Fish']

#-------- pop, append ----------

A.pop(1)
print(A)
  # ['Monday', 'Wednessday', 'Thursday', 'Friday']

A.append('WOW')
print(A)
  # ['Monday', 'Wednessday', 'Thursday', 'Friday', 'WOW']

#-------- filter, map, sorted ---- 

sArray = [
  {
    'day':'Monday',
    'animal': 'Fish',
    'id': 0
  }, 
  {
    'day':'Tuesday',
    'animal': 'Dog',
    'id': 1
  },
  {
    'day':'Wednessday',
    'animal': 'Cat',
    'id': 2
  }
]

demo = list( filter( lambda x: x['animal'] == 'Fish' , sArray) ) 
print(demo)
  # [{'day': 'Monday', 'animal': 'Fish', 'id': 0}]

demo = list( map( lambda x: x['day'], sArray) )
print(demo)
  # ['Monday', 'Tuesday', 'Wednessday']

demo = sorted( sArray, key = lambda x: x['id'], reverse=True )
print(demo)
  # [
  #   {'day': 'Wednessday', 'animal': 'Cat', 'id': 2}, 
  #   {'day': 'Tuesday', 'animal': 'Dog', 'id': 1}, 
  #   {'day': 'Monday', 'animal': 'Fish', 'id': 0}
  # ]

# -------- Quick filter and map

demo = [ x for x in sArray if x['animal'] == 'Fish' ]
print(demo)

demo = [ x['day'] for x in sArray ]
print(demo)


# -------- Loop --------
for eachItem in sArray:
  if eachItem['day'] == 'Monday':
    print(eachItem['animal'] + 'Boom!!')










