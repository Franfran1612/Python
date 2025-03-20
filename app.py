from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime

app = Flask(__name__)

spec = FlaskPydanticSpec(
    'flask-pydantic-spec',
    title = "Controle de datas",
    version = "1.0"

)

spec.register(app)
@app.route('/data_/<data>', methods=['GET'])
def presente_data(data):

    #Converter a string da data para o formato datetime
    """
        API para calcular a diferença entre duas datas

        #Endpoint:
        `Get / dias/<data_str>`

        #Parãmetros:
        - `data_str` (str): **Data no formato "DD-MM-YYYY"**(exemplo: "15-03-2025).
            -** Qualquer outro formato resultará em erro**

        ## Resposta(JSON):
        ```json
        {
        "dias": 100,
        "meses": 12,
        "ano": 2015,
        "tempo":"passado"
        }
        ```
    #Erros possíveis:
    - Se `data_str` não estiver no formato correto, retorna erro **400 Bad Request**:
    ```json

    """

    data_informada = datetime.datetime.strptime(data, '%d-%m-%Y')
    data_atual = datetime.datetime.now()

    if data_informada < data_atual:
        resultado = 'Passado'
    elif data_informada > data_atual:
        resultado = 'Futuro'
    else:
        resultado = 'Presente'



    dias = abs(data_atual - data_informada).days
    anos = abs(data_atual.year - data_informada.year)
    meses = abs(data_atual.month - data_informada.month) + (12 * anos)



    dados = {
        'dias': dias,
        'meses': meses,
        'anos': anos,
        "resultado": resultado
    }
    return  jsonify(dados)




# @app.route('/passado/ano/mes/data/dia', methods=['GET'])
# def passado():
#     ano = int('ano')
#     mes = int('mes')
#     data = str('data')
#     dia = int('dia')










if __name__ == '__main__':
    app.run(debug=True)