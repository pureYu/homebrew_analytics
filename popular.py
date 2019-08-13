import json

def install_sort(package):
    return package["analytics"]["365d"]

with open('package_info.json', 'r') as f:
    data = json.load(f)

# use only packages that have the word 'video' in the descr
# list comprehension
data = [item for item in data if 'video' in item['desc']]
data.sort(key=install_sort, reverse=True)

data_str = json.dumps(data[:5], indent=4) # print 5 first items
print(data_str)

# ################
# try:
#     f = open('package_info.json')
#     #var = bad_var
# except FileNotFoundError as e:
#     print(e)   # [Errno 2] No such file or directory: 'package_infoo.json'
# except Exception as e:
#     print(e)   # name 'bad_var' is not defined
# else:   # runs if there is no exception!
#     print(f.read())
#     f.close()
# finally:
#     print("Executing Finally... e.g. closing DB. Runs anyway")
#
#
# f.close()