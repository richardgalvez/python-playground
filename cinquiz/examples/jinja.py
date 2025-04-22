from jinja2 import Environment

environment = Environment()
template = environment.from_string("Here is the first question: {{ question }}")

template.render(question="What is the Capital of New York?")
print(template.render(question="What is the Capital of New York?"))

