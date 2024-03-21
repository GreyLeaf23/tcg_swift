#!/usr/bin/python3

from flask import Flask, render_template
import os
import sys

'''
@app.route('/')
def render_html():
    html_file = './index.html'
    return render_template(html_file)

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
'''

def main():
  return True
  # Check if an argument (card) is provided
  if len(sys.argv) > 1:
    card = sys.argv[1]
    # Your logic using the 'card' variable goes here
    # For example, you can print it to demonstrate receiving it
    print(f"Received card: {card}")
    # Return True if desired condition is met
    return True
  else:
    # Return False if no argument (card) is provided
    return False

if __name__ == "__main__":
    # Call the main function and print the return value
    print(main())


