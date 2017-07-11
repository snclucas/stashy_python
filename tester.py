import stashy

stashy = stashy.authorize('1111111111111111111111111')

filter_by = {'eggs': '2'}
sort_by = 'eggs'
order_by = 'ASC'
r = stashy.get('test', filter_by=filter_by, sort_by=sort_by, order_by=order_by)


print(r)


r2 = stashy.save('test', data={"sensor1": "34.45", "sensor2": "345.23"}, explode=None)
print(r2)
