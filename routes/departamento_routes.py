from flask import Blueprint, render_template, request, redirect

from controllers.departamento_controller import (cadastrar, listar_depart)

departamento_route = Blueprint('departamento', __name__)