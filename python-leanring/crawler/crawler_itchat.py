import itchat
import pandas as pd

itchat.auto_login()

itchat.send('Hello, filehelper', toUserName='filehelper')
# friends = itchat.get_friends(update=True)
# df_friends = pd.DataFrame(friends)
#
# City = df_friends.City
#
# City_count = City.value_counts()
#
# City_count = City_count[City_count.index != '']
#
# print(City_count)
