import web

render = web.template.render("mvc/views/")

class View():
    def GET (self):
        try:
            return render.View()
        except Exception: 
            return "Error"