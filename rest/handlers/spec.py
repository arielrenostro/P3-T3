from http import HTTPStatus

from flask import render_template
from flask.views import View


class SpecApi(View):

    def dispatch_request(self):
        headers = {
            'Content-Type': 'text/yaml'
        }

        return render_template("spec.yaml"), HTTPStatus.OK, headers
