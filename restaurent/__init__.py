from flask import Flask

### create app ########
app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysecretkey'
#######################


#######################
#### Blueprints #######
from restaurent.core.views import core

app.register_blueprint(core)
#######################