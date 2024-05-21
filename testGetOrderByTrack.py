# Марина Заборовская, 16 когорта - Финальный проект. Инженер по тестированию плюс

# файл для теста
import data
import script
import pytest

def test_get_order_by_track_return_success_response():

    # создаем новый заказ
    new_order = script.create_order(data.order_body)

    # проверяем, что нам пришло подтверждение в виде ответа 201, что заказ успешно создан
    assert new_order.status_code == 201, "Ответ сервера неверный, возможно заказ не создан"

    # сохраняем номер заказа
    track_id = (new_order.json()["track"])

    # получаем заказ по ранее полученному номеру заказа
    new_order_by_track = script.getOrderByOrderTrack(track_id)

    # проверяем, что нам пришло подтверждение в виде ответа 200, что мы получили заказ по его номеру
    assert new_order_by_track.status_code == 200, "Ответ сервера неверный"

    # проверям, что номер заказа тот же, что мы получили при создании заказа выше
    assert new_order_by_track.json()["order"]["track"] == track_id, "Номер заказа неверен, должен быть " + track_id + "а мы получили " + new_order_by_track.json()["order"]["track"]

    # проверяем некоторые другие поля в заказе
    assert new_order_by_track.json()["order"]["firstName"] == data.order_body["firstName"]
    assert new_order_by_track.json()["order"]["lastName"] == data.order_body["lastName"]
    assert new_order_by_track.json()["order"]["address"] == data.order_body["address"]
    assert new_order_by_track.json()["order"]["metroStation"] == str(data.order_body["metroStation"])
    assert new_order_by_track.json()["order"]["phone"] == data.order_body["phone"]
    assert new_order_by_track.json()["order"]["comment"] == data.order_body["comment"]

test_get_order_by_track_return_success_response()

