# Shopping_Cart_System

🛒 Shopping Cart System

📌 Project Overview

The Shopping Cart System is a console-based application developed using Python 3. It allows users to manage their shopping cart by viewing available products, adding items, removing items, and generating a final bill.

The system automatically calculates the subtotal, applicable discount, GST, and grand total.

🎯 Objectives

- Develop a simple shopping cart using Python.
- Display available products and their prices.
- Allow users to add and remove products.
- Validate product names and quantities.
- Calculate subtotal, discount, GST, and grand total.
- Generate an accurate final bill.

🛠️ Technologies Used

- Programming Language: Python 3
- Concepts Used:
  - Lists
  - Dictionaries
  - Functions
  - Conditional Statements
  - Loops
  - Input Validation

🛍️ Product Catalogue

Product| Price
Pen| ₹10
Notebook| ₹50
Bag| ₹500

💰 Billing Rules

- GST: 18%
- Discount: 10% when the subtotal is greater than ₹500.
- No discount is applicable when the subtotal is ₹500 or less.
- The grand total is calculated after applying the discount and GST.

Billing Formula

- Subtotal = Sum of all product prices × quantities
- Discount = 10% of subtotal (if subtotal > ₹500)
- GST = 18% of the amount after discount
- Grand Total = Subtotal - Discount + GST

⚙️ Features

1. View available products.
2. Add products to the shopping cart.
3. Remove products from the cart.
4. Validate product names.
5. Validate minimum quantity.
6. Calculate subtotal automatically.
7. Apply discounts based on purchase amount.
8. Calculate GST and generate the final bill.

🧪 Test Cases

Test Case| Scenario| Expected Result
1| Add 2 Notebooks| Subtotal: ₹100
2| Add 1 Bag| Subtotal: ₹500, GST: ₹90, Total: ₹590
3| Add invalid product or negative quantity| Display validation error
4| Add 2 Bags, add 5 Pens, remove Pens| Subtotal: ₹1000, Discount: ₹100, GST: ₹162, Total: ₹1062

▶️ How to Run the Project

Step 1: Clone the repository.

git clone YOUR_REPOSITORY_URL

Step 2: Open the project folder.

cd Shopping-Cart-System

Step 3: Run the Python program.

python main.py

📂 Project Structure

Shopping-Cart-System/
│
├── main.py
└── README.md

🎓 Academic Information

- University: Rungta International Skills University
- School: School of Information Technology
- Course: Bachelor of Computer Application (BCA)
- Project Title: Shopping Cart System
- Programming Language: Python 3

👨‍💻 Author

Developed as an academic project for the Bachelor of Computer Application (BCA) programme.

---

⭐ Thank you for visiting this repository!



[@SATYAPRAKASHSETHY] (https://github.com/SATYAPRAKASHSETHY)
