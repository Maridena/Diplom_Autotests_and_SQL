# добавляем модуль requests для выполнения запросов на сервер,
# модуль data с данными для заказа и модуль с настройками

import requests
import data
import configuration

# функция для создания заказа клиентом
# должна возвращать номер трекера заказа (поле Orders.track в базе)
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                  json = body,
                  headers = data.headers)

# функция для получения заказа по номеру track заказа
# на входе должна получать номер заказа
def getOrderByOrderTrack(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t=" + str(track),
                        headers = data.headers)


