import web

render = web.template.render("mvc/views/")

class Index():
    def GET (self):
        try:
            return render.index()
        except Exception: 
            return "Error"
