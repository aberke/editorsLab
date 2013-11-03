from flask import Flask, Blueprint


app = Flask(__name__)
app.config.from_object('config')


from splash import splash
app.register_blueprint(splash, url_prefix='')

