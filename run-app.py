#!/python3/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from app import app

if __name__ == '__main__':
    # Running app in debug mode
    HOST = os.environ.get('HOST')
    PORT = int(os.environ.get('PORT'))
    app.run(debug=True, host=HOST, port=PORT)
