from jinja2 import Environment, FileSystemLoader
import os

def render_readme(context, template_path="templates", template_file="README_template.md"):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_file)
    return template.render(context)
