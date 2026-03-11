import falcon
import statsd

stats_client = statsd.StatsClient("localhost", 8125)


class HelloResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        stats_client.incr("hello_requests")
        resp.media = {
            "quote": "I've always been more interested in the future than in the past.",
            "author": "Grace Hopper",
        }


app = falcon.App()
app.add_route("/", HelloResource())
