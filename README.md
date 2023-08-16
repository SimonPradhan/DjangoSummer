# Blog Application Summer Django Class
Summer 2023
During my Summer Class I created a django web application about blog website.

To download and use the project in your local machine. Follow the below mentioned steps:
- Clone the project
  - If the SSH is not set in your local machine and github you can go with option 1 otherwise option 2
    - Option 1
    ```
    git clone https://github.com/SimonPradhan/DjangoSummer.git summerproject
    ```
    - Option 2
    ```
    git clone  git@github.com:SimonPradhan/DjangoSummer.git summerproject
    ```
      
- Setup the environment
  - Go to the folder
  ```
  cd summerproject
  ```
  - Create the virtual environment
    - You can create the virtualenv with virtualenv library or the pythonenv
      - You can click [here](https://virtualenv.pypa.io/en/latest/installation.html) for the documentation to know more about the virtual environment.
      - You can also skip this step and go with installing the library step.
    - Installing the library
      - Install from requirements.txt
      ```
      pip install -r requirements.txt
      ```
  - Setting up the environmental variables
    - In the root project create a **.env** file
    - You can open the project with VS Code
    ```
    code summerproject
    ```
    - Populate the file with below variables
      - SECRET_KEY= YOUR-SECRET-KEY
      - DATABASE= YOUR-DATABASE-URL
      - EMAIL-HOST-USER= YOUR-EMAIL
      - EMAIL-HOST-PASSWORD= PASSWORD-EMAIL
      - EMAIL-PORT= EMAIL-PORT
      - DEFAULT-FROM-EMAIL= YOUR-EMAIL
- Run the project
  - Migrate the database
  ```
  python manage.py migrate
  ```
  - Runserver
  ```
  python manage.py runserver
  ```

# Main Features
- User Management System
- Dynamic Email Sending
- CRUD operation for the blog

# Want to Collaborate
- You can add the features and push to the new branch andhi send the pull request.

# **Sayonara 👋👋**
