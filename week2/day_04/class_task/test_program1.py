def test_program(*args, **kwargs):
  print(args)
  print(kwargs)
if __name__ == "__main__":
  name = list(('sunil','ghimire'))
  test_program(*name, age = 'kina chaiyo')