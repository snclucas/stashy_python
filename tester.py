import stashyio

stashy = stashyio.authorize('1111111111111111111111111')

docs_to_insert = {"docs": [
    {"sensor1": "34.45", "sensor2": "345.23"},
    {"sensor1": "134.45", "sensor2": "1345.23"}
]}

r = stashy.save('test', data=docs_to_insert, explode="docs")
print(r)


filter_by = {'sensor1': '34.45', 'sensor2': '345.23'}
filter_by_json = {'st::filter': {'sensor1': '34.45', 'sensor2': '345.23'}}
sort_by = 'sensor1'
order_by = 'ASC'
r = stashy.get('test', filter_by=filter_by, sort_by=sort_by, order_by=order_by)
print(r)

r = stashy.delete('test', filter_by=filter_by)
print(r)

r = stashy.delete_all('test')
print(r)
