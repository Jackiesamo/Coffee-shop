# Coffee Shop Domain Model

## Description
The Coffee Shop Domain Model is a Python application that simulates a coffee shop's business logic using object-oriented programming principles. The application manages relationships between customers, coffees, and orders, allowing customers to place orders, track their purchase history, and analyze coffee popularity and pricing. The domain model demonstrates class design, object relationships, and data management through three interconnected entities.

## Author
Jacklyne Owuor

## Setup Instructions
1. Clone this repository
2. Navigate to the project directory: `cd coffee_shop`
3. Install pipenv if not already installed: `pip install pipenv`
4. Create and activate virtual environment: `pipenv install` then `pipenv shell`
5. Install testing dependencies: `pipenv install pytest`
6. Run the debug file to test functionality: `python debug.py`
7. Run tests (optional): `pytest`

## BDD (Behavior Driven Development)

1. **Input:** Customer name (string between 1-15 characters)
   * **Output:**Customer instance created successfully

2. **Input:** Customer name (invalid - empty or >15 characters)
   * **Output:** Exception raised with error message

3. **Input:** Coffee name (string with at least 3 characters)
   * **Output:** Coffee instance created successfully

4. **Input:** Coffee name (invalid - less than 3 characters)
   * **Output:** Exception raised with error message

5. **Input:** Order with customer, coffee, and price (float between 1.0-10.0)
   * **Output:** Order instance created and associated with customer and coffee

6. **Input:** Order with invalid price (price < 1.0 or price > 10.0)
   * **Output:** Exception raised with error message

7. **Input:** Call `customer.orders()` method
   * **Output:** List of all orders placed by the customer

8. **Input:** Call `coffee.num_orders()` method
   * **Output:** Total count of orders for that coffee

9. **Input:** Call `Customer.most_aficionado(coffee)` class method
   * **Output:** Customer instance who spent the most on that coffee, or None if no orders exist

## Technologies Used
* Python 3.x
* Pipenv (virtual environment and dependency management)
* Pytest (testing framework)
* Object-Oriented Programming (OOP) principles

## Contact Information
**GitHub:** [Jackiesamo]  


## License
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.