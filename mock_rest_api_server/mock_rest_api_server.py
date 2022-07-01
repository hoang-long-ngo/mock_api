from flask import Flask, json, request
import logging

api = Flask(__name__)
logging.basicConfig(filename="log.log", level=logging.DEBUG, format=f'%(asctime)s %(message)s')


def file_ops(fn:str, ops:str='r', data:dict=None)->dict:
    with open(fn, ops) as fh:
        if ops == 'r':
            return json.load(fh)
        elif ops == 'w':
            if not data: raise Exception('no data given!')
            json.dump(data, fh, indent=2)
            return {'status': 'ok'}


@api.route('/test', methods=['GET'])
def get_test():
    api.logger.info(list(request.__dict__.keys()))
    return json.dumps({'hello':'world!'})

@api.route('/adminconfig/v2/indexes', methods=['GET'])
def get_indexes_list():
    try:
        data = file_ops('mock_indexes.json', 'r')
        return json.dumps(data)
    except Exception as e:
        api.logger.exception(e)

@api.route('/adminconfig/v2/indexes', methods=['POST'])
def post_indexes_list():
    try:
        # du musst "request" auswerten
        # zb request[???] --> muss payload steht
        # is it valid?

        # 2. eigentlich direkt payload an rest api ABER weil umweg mit file im dev
        # 2.1 data aus file laden

        # 2.2 neuen index ins data-object mergen


        # 2.3 zurück in die file schreiben

        response = file_ops('mock_indexes.json', 'w', data=data)
        return json.dumps(response)
    except Exception as e:
        api.logger.exception(e)


if __name__ == '__main__':
    api.run()