
from main import index, requirements

def test_index():
    assert index() == "Welcome, to my final winc assignment: CD! I hope it will work, yes!"

def test_requirments():
    assert requirements() == "The requirments are: build a continuous deployment using Git Actions"



