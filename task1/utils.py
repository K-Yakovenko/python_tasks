import json

class Utils:
  @staticmethod
  def load_test_data(file_path='task1/testdata.json'):
    with open(file_path, 'r') as f:
      return json.load(f)
