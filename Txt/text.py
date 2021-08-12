from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)
template = env.get_template('hello.txt')

params = {}
params['girl'] = 'Daniela!!!!'
params['me'] = 'Richard'

colors = ['Amarillo', 'Azul', 'Rojo']

output = template.render(data=params, bandera=colors, cierto=True)
print(output)
#self.response.write(output)
