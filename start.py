from api import Application
from app_demo import demo1, demo2

app = Application(8080)
app.set_path('', demo1)
app.set_path('', demo2)
app.run()
