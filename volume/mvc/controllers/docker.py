import web

render = web.template.render("mvc/views/")

class Docker():
    def GET (self):
        try:
            return render.docker()
        except Exception : 
            return "Error"
