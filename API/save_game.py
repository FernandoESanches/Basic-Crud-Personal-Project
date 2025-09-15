from flask import jsonify, Blueprint, request

save_bp = Blueprint('save', __name__, url_prefix='/api')

@save_bp.route("/save", methods=["POST"])
def saveGame():
    data = request.get_json()
    print(data)
    return jsonify({'message': 'Jogo adicionado com sucesso'}), 200