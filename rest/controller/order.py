from rest.controller.base import Controller
from rest.dao.order import OrderDAO
from rest.exceptions.request import RequestException
from rest.models.order import Order


class OrderController(Controller):

    _dao = OrderDAO()

    def new_order(self, body: dict):
        user_id = int(self.get_required_value(body, 'idusuario'))
        products = self.get_required_value(body, 'produtos')
        total_value = float(self.get_required_value(body, 'valortotal'))

        from rest.controller.user import UserController
        user = UserController().find(user_id)

        if not user:
            raise RequestException(404, 'User not founded')

        order = Order(
            user=user,
            products=products,
            total_value=total_value
        )

        self._dao.update(order)

        return order

    @classmethod
    def get_required_value(cls, body, key):
        value = body.get(key)

        if not value:
            raise RequestException(400, f'{key} is required')

        return value

    def update_order_data(self, order: Order, body: dict):
        keys = body.keys()

        if 'idusuario' in keys:
            user_id = body.get('idusuario')

            from rest.controller.user import UserController
            user = UserController().find(user_id)

            if not user:
                raise RequestException(404, 'User not founded')

            order.user = user

        if 'produtos' in keys:
            order.products = body.get('produtos')

        if 'valortotal' in keys:
            order.total_value = float(body.get('valortotal'))

        self._dao.update(order)
