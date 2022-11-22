from flask import Flask, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


# открываем папку uploads для отдачи пользователю
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


# регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.run()
