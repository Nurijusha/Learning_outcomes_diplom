import logger_utils

from flask import Flask, request, jsonify, Response
from flask_restful import Api

from check_solution import SolutionTests

# Set logging
logger = logger_utils.setup_applevel_logger()

app = Flask(__name__)
api = Api(app)


@app.route('/api/do_tests/', methods=['GET'])
@app.route('/api/do_tests', methods=['GET'])
def add_message():
    data = request.get_json()

    if not data:
        return Response(status=404)

    url = data.get('github_url')
    if not url:
        return Response(status=404)

    logger.info(f'New url: {url}')

    solution = SolutionTests(url)
    result, timeout_count = solution.run_tests()

    if isinstance(result, bool):
        return jsonify({
            'github_url': url,
            'result': 'error'
        })

    if result >= 95:
        result = 5
    elif result >= 80:
        result = 4
    elif result >= 70:
        result = 3
    else:
        result = 2

    return jsonify({
        'github_url': url,
        'result': result,
        'timeout_count': timeout_count
    })


if __name__ == '__main__':
    app.run(port=5001, debug=False)
