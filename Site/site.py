from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('child.html')

output = template.render(title = 'Primer Sitio', body='Contenido')
print(output)
