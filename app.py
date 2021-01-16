from flask import Flask, render_template, request, url_for

app = Flask(__name__)


class Fizzbuzz:
  def __init__(self, input):
    self.input = input
  
  def make_numslist(self) -> list:
    nums = list(range(1, int(self.input) + 1))
    return nums

  
  def filter(self) -> list:
    nums = self.make_numslist()

    numlist = [str(num) for num in nums]

    for num in numlist:
      if '3' in num:
        numlist[numlist.index(num)] = "Sorry bitch"
      elif '2' in num:
        numlist[numlist.index(num)] = "That's hot"
      elif '1' in num:
        numlist[numlist.index(num)] = "Loves it P"

    result = ", ".join(numlist)
    return result

  def __repr__(self):
    return self.filter()


@app.route('/', methods=["POST", "GET"])
def home():
  if request.method == 'POST':
    input = request.form['input']
    Paris = Fizzbuzz(input)
    
    while True:
      try:
        if int(input):
          if input < 1:
            print("Please enter a number greater than 0.")
      except:
        return "Not a valid input"
      else:
        break
  # if request.method == 'GET'
  else:
    # if Paris:
    #   return render_template('index.html', Paris=Paris)
    Paris = 0
    return render_template('index.html', Paris=Paris)
    




@app.route('/', methods=["POST", "GET"])
def home():
  if request.method == 'POST':
    input = request.form['input']
    Paris = Fizzbuzz(input)
    
    while True:
      try:
        if int(input):
          if input < 1:
            print("Please enter a number greater than 0.")
      except:
        return "Not a valid input"
      else:
        break
  # if request.method == 'GET'
  else:
    Paris = Fizzbuzz(input)
    return render_template('index.html', Paris=Paris)
    

      
if __name__== "__main__":
  app.run()