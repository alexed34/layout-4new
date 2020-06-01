from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape



env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    cap1_title="Красная кепка",
    cap1_text="$ 100.00",
    cap2_title="Чёрная кепка",
    cap2_text="$ 120.00",
    cap3_title="Ещё одна чёрная кепка",
    cap3_text="$ 90.00",
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)

server.serve_forever()


# Traceback (most recent call last):
#   File "C:\Users\asus\PycharmProjects\layout-4new\main.py", line 28, in <module>
#     server.serve_forever()
#   File "C:\Users\asus\anaconda3\lib\socketserver.py", line 232, in serve_forever
#     ready = selector.select(poll_interval)
#   File "C:\Users\asus\anaconda3\lib\selectors.py", line 323, in select
#     r, w, _ = self._select(self._readers, self._writers, [], timeout)
#   File "C:\Users\asus\anaconda3\lib\selectors.py", line 314, in _select
#     r, w, x = select.select(r, w, w, timeout)
# KeyboardInterrupt

