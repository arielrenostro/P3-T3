from flask import request
from flask_restful import Resource

from rest.controller.order import OrderController
from rest.exceptions.request import RequestException
from rest.models.order import Order
from rest.utils.wrappers import exception_handler, authenticated


class OrderApi(Resource):

    _controller: OrderController = OrderController()

    @exception_handler
    @authenticated
    def get(self):
        orders = self._controller.find_all()
        return list(
            map(lambda e: order_to_dict(e), orders)
        )

    @exception_handler
    @authenticated
    def post(self):
        if not request.is_json:
            raise RequestException(400, 'Must be JSON request')

        body = request.json

        order = self._controller.new_order(body)

        return order_to_dict(order), 201


class OrderParamApi(Resource):

    _controller: OrderController = OrderController()

    @exception_handler
    @authenticated
    def put(self, id_):
        if not id_:
            raise RequestException(400, 'ID path param is required')

        if not request.is_json:
            raise RequestException(400, 'Must be JSON request')

        id_ = int(id_)
        order = self._controller.find(id_)
        if not order:
            raise RequestException(404, 'Order not founded')

        body = request.json
        self._controller.update_order_data(order, body)

        return order_to_dict(order)

    @exception_handler
    @authenticated
    def delete(self, id_):
        if not id_:
            raise RequestException(400, 'ID path param is required')

        id_ = int(id_)
        order = self._controller.find(id_)
        if not order:
            raise RequestException(404, 'Order not founded')

        self._controller.delete(order)

        return {
            'success': {
                'text': 'Comanda removida'
            }
        }


def order_to_dict(entity: Order):
    return {
        'id': str(entity.id),
        'idusuario': str(entity.user_id),
        'produtos': entity.products,
        'valortotal': str(entity.total_value)
    }
