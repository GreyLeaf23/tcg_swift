# TCG Swift - Into The Action!

A learning experience to swiftly enjoy the world of trading card games!

![Showcase](https://github.com/GreyLeaf23/holbertonschool-higher_level_programming/blob/main/small.png)

## Motivation


As part of the Holberton's curriculum, Python is the main language that will demonstrate the abilities that I've acquired as a software
engineer.
Demonstrate my understanding and continue practice of the higher level field.



## Build status



[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

## Code style



[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Screenshots
Include logo/demo screenshot etc.

## Tech/framework used

<b>Built with</b>
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [MySQL](https://www.mysql.com/)

## Features
What makes your project stand out?

## Code Example
These are general functions for each of the featured languages.



Python -
```python
#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")

```


Javascript -
```javascript
// Select element with the 'add_item' id.
let add_item = document.getElementById('add_item');

// Listen for a click event on the html element 'add_item'.
add_item.addEventListener('click', function() {
    // Create a new element 'li'.
    let li = document.createElement('li');

    // Add the text 'Item' to the new element 'li'.
    li.textContent = 'Item';

    // Select the html element 'my_list'.
    let my_list = document.querySelector('.my_list');

    // Add the new element 'li' to the html element 'my_list'.
    my_list.appendChild(li);
});
```



MySQL -
```ruby
-- Shows the number of records with the same score in the 'second_table'.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
```



## Installation
Provide step by step series of examples and explanations about how to get a development env running.



## How to use?



Here's a general guide on how to use this repository for learning:

1. **Clone the Repository**: First, you need to clone the repository to your local machine. You can do this by running the following command in
your terminal:
   ```bash
   git clone https://github.com/GreyLeaf23/holbertonschool-higher_level_programming.git
   ```

2. **Explore the Projects**: Each directory in the repository represents a different project or exercise. You can navigate into each directory to see the specific tasks and challenges associated with that project.

3. **Read the README**: Most directories have a README file that provides context and instructions for the project. This is a good place to start before diving into the code.

4. **Study the Code**: Look at the code files (.py for Python, .sql for SQL) to understand how they solve the tasks outlined in the README. Try to understand the logic and techniques used.

5. **Run the Code**: Try running the code to see what it does. For Python files, you can usually run them with the command `python3 filename.py`. For SQL files, you'll need a SQL database like MySQL to run them.

6. **Modify the Code**: Once you understand how the code works, try making some changes. This could be as simple as changing variable values, or as complex as adding new features or functions.

7. **Check the Tests**: Some projects include test files that you can run to check your code. These are usually named `test_*` or `*_test`. Running these tests can help ensure your modifications didn't break anything.

Remember, the key to learning from this repository is active engagement. Don't just passively read the code; run it, modify it, and experiment with it to truly understand it.


## License

MIT © [Christian Rosario]()# Holberton School - Higher Level Programming


This is a fundational repository for learning languages considered 'Higher Level' at Holberton.
The repository feautures Python as the main language of learning choice. But we also tap into SQL and Javascript learning.

![Showcase](https://github.com/GreyLeaf23/holbertonschool-higher_level_programming/blob/main/small.png)

## Motivation


As part of the Holberton's curriculum, Python is the main language that will demonstrate the abilities that I've acquired as a software
engineer.
Demonstrate my understanding and continue practice of the higher level field.



## Build status



[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

## Code style



[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)

## Screenshots
Include logo/demo screenshot etc.

## Tech/framework used

<b>Built with</b>
- [Python](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [MySQL](https://www.mysql.com/)

## Features
What makes your project stand out?

## Code Example
These are general functions for each of the featured languages.



Python -
```python
#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")

```


Javascript -
```javascript
// Select element with the 'add_item' id.
let add_item = document.getElementById('add_item');

// Listen for a click event on the html element 'add_item'.
add_item.addEventListener('click', function() {
    // Create a new element 'li'.
    let li = document.createElement('li');

    // Add the text 'Item' to the new element 'li'.
    li.textContent = 'Item';

    // Select the html element 'my_list'.
    let my_list = document.querySelector('.my_list');

    // Add the new element 'li' to the html element 'my_list'.
    my_list.appendChild(li);
});
```



MySQL -
```ruby
-- Shows the number of records with the same score in the 'second_table'.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
```



## Installation
Provide step by step series of examples and explanations about how to get a development env running.



## How to use?



Here's a general guide on how to use this repository for learning:

1. **Clone the Repository**: First, you need to clone the repository to your local machine. You can do this by running the following command in
your terminal:
   ```bash
   git clone https://github.com/GreyLeaf23/holbertonschool-higher_level_programming.git
   ```

2. **Explore the Projects**: Each directory in the repository represents a different project or exercise. You can navigate into each directory to see the specific tasks and challenges associated with that project.

3. **Read the README**: Most directories have a README file that provides context and instructions for the project. This is a good place to start before diving into the code.

4. **Study the Code**: Look at the code files (.py for Python, .sql for SQL) to understand how they solve the tasks outlined in the README. Try to understand the logic and techniques used.

5. **Run the Code**: Try running the code to see what it does. For Python files, you can usually run them with the command `python3 filename.py`. For SQL files, you'll need a SQL database like MySQL to run them.

6. **Modify the Code**: Once you understand how the code works, try making some changes. This could be as simple as changing variable values, or as complex as adding new features or functions.

7. **Check the Tests**: Some projects include test files that you can run to check your code. These are usually named `test_*` or `*_test`. Running these tests can help ensure your modifications didn't break anything.

Remember, the key to learning from this repository is active engagement. Don't just passively read the code; run it, modify it, and experiment with it to truly understand it.


## License

MIT © [Christian Rosario]()
