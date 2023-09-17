<div align="center">

[<img src="https://github.com/RMNorbert/Chat/blob/main/chatbot/convocat.png" alt="Convocat" width="300">](README.md)

[![Python](https://img.shields.io/badge/Python-00264D.svg?logo=python&logoColor=gold&labelColor=black&style=for-the-badge)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-navy.svg?logo=NumPy&logoColor=steelblue&labelColor=black&style=for-the-badge)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-008080.svg?logo=flask&logoColor=white&labelColor=black&style=for-the-badge)](https://flask.palletsprojects.com/en/2.3.x/)
[![PyTorch](https://img.shields.io/badge/PyTorch-812CE5.svg?logo=pytorch&logoColor=DE3412&labelColor=black&style=for-the-badge)](https://pytorch.org/)

[![License: MIT](https://img.shields.io/badge/-MIT-blue.svg?label=license&logoColor=white&labelColor=242526&style=for-the-badge)](LICENSE "License")

</div>


# Chat

[Table of content:](#description)
- [Used technologies](#used-technologies)
- [Features](#features)
- [Getting started](#getting-started)
- [License](#license)
---
## Description:

ConvoCat is a simple chatbot application to provide information and guidance to users about the application  
it supports. (The ConvoCat will undergo extensive enhancements to become an even more robust and complex chatbot in the future)

## Used technologies:

 Backend
  - Python
  - PyTorch
  - Flask
  - NLTK
  - NumPy

---
## Features

- **Provide realtime answers and guidance to user's questions**
 
---
## Getting Started

Follow these instructions to get a copy of the ConvoCat project up and running on your local machine for testing purposes.

---
## Prerequisites

**- To get started with ConvoCat, make sure you meet the following prerequisites:**

- Python installed on your machine. [Download Python](https://www.python.org/) from the official website and follow the installation instructions.
---
## Installation:

  Follow these steps to install ConvoCat:

#### 1. Clone the repository
    
#### 2. Initial Setup:
   Comment out the nltk.download('punkt') line in the nltk_utils.py file. This line is responsible for downloading the tokenization model for various languages.
   Create training data by navigating to the project's root chatbot directory in your terminal and running:
        ```
        python3 train.py
        ```
   This will generate a .pth file necessary for conversations.

#### 3. Run the project: 
   Open a terminal or command prompt, navigate to the project's root directory, and run the following command:
        ```
        python3 app.py
        ```
   Python will execute the app.py script, it will start a web server, resolve any necessary dependencies , 
   and make the application accessible through a specified port.
   ___

#### 4. Access the application:

  Once the server is up and running, you can make requests to ConvoCat through the appropriate URL (e.g., http://localhost:5000). 
  Please note that the URL and port number may vary based on your configuration.

---
## License

This project is licensed under the MIT License - see the [License](LICENSE) file for details.
