import panel as pn

def f(x):
  return x * x
pn.interact(f, x=10)
