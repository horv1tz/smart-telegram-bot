from utils.SearchEngine.google import get_data_from_google
from utils.Neural.handlerData import handle_data

query = 'Привет, какая погода в ростове на дону сегодня'
# query = 'Напиши код на python, который работает с разными типами данных'
search = get_data_from_google(query)
print(handle_data(query, search))
