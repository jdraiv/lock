
from jinja2 import Environment, PackageLoader
from sanic.response import html


def set_templates_env(filename, templates_dir):
    env = Environment(loader=PackageLoader(filename, templates_dir))
    
    return env


def render_template(template_name, env):
    template = env.get_template('%s.html' % template_name)
    html_content = template.render()

    return html(html_content)