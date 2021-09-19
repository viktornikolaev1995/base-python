import functools, json
def to_json(func):
    @functools.wraps(func)
    def wrapped(*args,**kwargs):
        return json.dumps(func(*args,**kwargs))
    return wrapped

@to_json
def get_data(*args,**kwargs):
  if args and not kwargs:
      return args
  elif kwargs and not args:
      return kwargs
  else:
      return None








