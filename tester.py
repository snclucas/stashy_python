import stashy

stashy = stashy.authorize('1111111111111111111111111')

docs_to_insert = {"docs": [
    {"sensor1": "34.45", "sensor2": "345.23"},
    {"sensor1": "134.45", "sensor2": "1345.23"}
]}

r2 = stashy.save('test', data=docs_to_insert, explode="docs")
print(r2)


filter_by = {'sensor1': '134.45'}
sort_by = 'sensor1'
order_by = 'ASC'
r = stashy.get('test', filter_by=filter_by, sort_by=sort_by, order_by=order_by)
print(r)


r3 = stashy.delete_all('test')
print(r3)
