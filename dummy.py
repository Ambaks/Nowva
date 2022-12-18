import pickle
from set import Set
import connector as cn

a = Set('Squat', 5, 7, [1,1,1,1,1], [1,1,1,1,1], None)
conn, cursor = cn.connect()
# cn.create_table(conn)
# print(cn.has_table(cursor, 'data'))

# # data = cn.serialize(a)
# # print(data)
# # cn.commit_to_table(conn, data)
rows = cn.get_all_sets(cursor, 'data')


for key, item in rows:
    obj = pickle.loads(item)
    obj.get_summary()

# # data.get_summary()
# key, item = cn.get_last_set(cursor, 'data')

# obj = pickle.loads(item)
# print(obj.rep_time)