# falcon test
# Try to learn falcon framework
import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class TestFirstExample(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('This is my first example \n')

    def on_post(self, req, resp):
        body = req.stream.read()  # Assumes JSON
        if not body:
            raise falcon.HTTPBadRequest(
                "Empty Request Body, A valid JSON document is required.")
        else:
            resp.status = falcon.HTTP_200
            with open("first_example.log", "w") as ft:
                msg = f"{body}\n"
                ft.write(msg)
            ft.close()

# falcon.API instances are callable WSGI apps
app = falcon.API()
# Resources are represented by long-lived class instances
test = TestFirstExample()
# test will handle all requests to the '/test' URL path
app.add_route('/test', test)
