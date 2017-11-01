#%%
from function import testData
import oracle.query as q

sql = """select * from test"""
result = q.query(sql, [], False)

print(result)

#%%
data = testData()
print(data)

#%%
sql = """
    insert into test (NAME, LV, SKILL) 
    values (:name, :LV, :skill)
"""
result = q.queryWrite(sql, [ data['name'], 26, data['skill'] ])
print(result)