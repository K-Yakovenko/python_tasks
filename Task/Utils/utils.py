import json

class Utils:
  @staticmethod
  def load_test_data():
    with open('test_data.json') as f:
      return json.load(f)
