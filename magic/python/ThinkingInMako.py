__author__ = 'JohnLiu'

from mako.template import Template


#python mako code
t = Template("My favorite ice cream is ${name}")
print t.render(name="Herrell's")
context = {'name': "Herrell's"}
print t.render(**context)

s = Template("My favorite coffee is ${name | entity}")
print s.render(name="Cappuccino")
