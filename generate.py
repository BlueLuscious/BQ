from jinja2 import Environment, FileSystemLoader

# Configura Jinja
env = Environment(loader=FileSystemLoader("templates"))

# Lista de templates que quieres renderizar
templates = ["index.html", ]

for template_name in templates:
    # Carga cada plantilla
    template = env.get_template(template_name)
    
    # Renderiza la plantilla con variables opcionales
    output = template.render()
    
    # Guarda el HTML generado en un archivo con el mismo nombre
    with open(template_name, "w") as f:
        f.write(output)

    print(f"{template_name} generated successfully!")