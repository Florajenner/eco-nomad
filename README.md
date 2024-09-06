# Eco-Nomad Blog

## About The Eco-Nomad Blog
Eco-Nomad is a platform aimed at promoting sustainable travel. The blog shares engaging posts on topics such as alternatives to flying, how to reduce your plastic use when not at home, and other tips that help eco-conscious travellers maintain their green standards on the move.

## Screenshots
![Screenshot of Mockup](/assets/media/mockup.png)

## User Stories
- As a user, I can upload videos to my blog posts so that I can share dynamic content.
- As a user, I can like a blog post so that I can show my appreciation for the content.
- As an admin, I can delete inappropriate comments so that I can maintain the quality of discussions.
- As a user, I can delete my blog post so that I can remove content I no longer want to share.

## Design
The straightforward design and generous use of white space improve the site's readability and user experience. The choice of colours and visuals is in harmony with the brand's environmentally conscious values, creating a sense of eco-friendliness.

### Colour Scheme
Eco-Nomad uses a palette that reflects the natural world, featuring green tones evoking a feel of eco-friendliness. The gentle, muted colours help maintain focus on the content without overwhelming the reader.

![Screenshot of Colour Scheme](/assets/media/colour_scheme.png)

### Typography
Headings and subheadings use a modern sans-serif font that complements the site's minimal design, while paragraphs use a serif font for readability.

## Features

![Screenshot of Comment Section](/assets/media/comment_section.png)

- **Fully Responsive Design**: The blog is designed to be responsive to a variety of devices, such as mobile phones, tablets, laptops, and desktop computers.
- **Comment Section**: Readers can engage with the content by leaving comments.

- **Post Like**: Readers can quickly like posts without having to write a comment, providing feedback to the writer.

- **Delete Comment**: Readers can delete their comments after submission.

- **Update Comment**: Comments can be updated after submission.

- **Comment Approval**: Comments are shown once they are approved, giving admins full control.

## Future Features
- **User Engagement**: We aim to introduce social media integration, allowing readers to engage with content and share it easily with others.
- **Content Organization**: Posts categorized to help users easily explore different topics related to sustainability and eco-friendly living.
- **Search Functionality**: Users can quickly search for specific posts or keywords, enhancing accessibility.

## Technologies Used
- **Django (4.2.16)**: A high-level Python web framework that promotes rapid development and clean, pragmatic design. It is used as the core framework for the Eco-Nomad blog.
- **PostgreSQL**: A powerful, open-source object-relational database system that is used as the database for this project.
- **Gunicorn (23.0.0)**: A Python WSGI HTTP server used to run the application in production.
- **Whitenoise (5.3.0)**: Allows the serving of static files directly from Django without needing a separate web server.
- **Heroku**: A cloud platform used for deploying the Eco-Nomad blog.
- **Git & GitHub**: For version control and repository hosting, enabling collaborative development.

## Libraries
- **Crispy Forms (2.3)**: A Django application that provides elegant form rendering.
- **Crispy Bootstrap 5 (0.7)**: Adds Bootstrap 5 support for Django Crispy Forms.
- **Django Allauth (0.57.2)**: A package that provides authentication, registration, and third-party (social) account authentication.
- **Django Summernote (0.8.20.0)**: A WYSIWYG editor for text fields in Django, used to enhance content management.
- **Python JWT (2.9.0)**: Handles JSON Web Tokens (JWT) for secure token-based authentication.
- **OAuthlib (3.2.2)** & **Requests OAuthlib (2.0.0)**: These libraries provide support for OAuth 1.0 and OAuth 2.0, enabling secure third-party authentication.
- **PyOpenID (3.2.0)**: An implementation of the OpenID standard used for authentication purposes.
- **SQLparse (0.5.1)**: A non-validating SQL parser for Python, used by Django to handle SQL queries.
- **Dj-database-url (0.5.0)**: A utility that simplifies database configurations, particularly useful for deployment on platforms like Heroku.

## Validator Testing
## HTML & CSS Validation

For validating the HTML and CSS in this project, I used **HTMLHint** to ensure the quality of the code.

During the validation process, the only errors detected were related to the usage of **Django template tags** (such as `{% extends %}`, `{% load %}`, and `{{ variable }}`) in the HTML files. These tags are required by Django for dynamic rendering of templates, and as such, they are not recognized by HTMLHint, which expects pure HTML syntax.

The specific errors, such as:
- **"Doctype must be declared first"**
- **"Special characters must be escaped"**

are a result of Django template syntax and do not affect the functioning of the project or its compliance with HTML standards.

### Tools Used:
- **HTMLHint** for validating HTML files.
- **Stylelint** for validating CSS (if applicable).

All static HTML and CSS passed validation successfully, with only template-related warnings being flagged.

Lighthouse showed low performance due to the ammount of large images used.

![Lighthouse](/assets/media/lighthouse.png)

## Code Linting

During the development of the project, the code was checked for style and syntax issues using **Flake8**. Below are some of the common issues that were flagged and addressed:

### Issues Detected

./blog/migrations/0001_initial.py:20:80: E501 line too long (117 > 79 characters)
./blog/migrations/0001_initial.py:25:80: E501 line too long (101 > 79 characters)
./blog/migrations/0003_alter_comment_options_alter_post_options_like.py:27:80: E501 line too long (117 > 79 characters)
./blog/views.py:5:1: F401 '.models.Like' imported but unused
./blog/views.py:96:5: F841 local variable 'post' is assigned to but never used

### Fixes Applied

- **F401**: Unused imports were removed from the files.
- **F841**: Removed unused variables.
- **W293**: Removed unnecessary whitespace in blank lines.
- **E231**: Added missing whitespace after commas where necessary.

### Deployment Tools
- **Heroku**: The platform used to deploy the Eco-Nomad blog.
- **Git** & **GitHub**: Used for version control and collaborative development.

## Deployment
Here’s the deployment instructions with the code sections in plain text:

### **Deployment Instructions for Heroku**

#### **Pre-requisites:**
- Ensure you have a GitHub account and Heroku account.
- Install Git, Heroku CLI, and Python on your local machine.

#### **Deploying on Heroku**

1. **Clone the GitHub Repository:**
   - Open your terminal and clone the repository:

   `git clone <GitHub-repository-URL>`

   `cd <project-folder>`

2. **Set Up the Virtual Environment:**
   - Create and activate a virtual environment:

   `python3 -m venv venv`

   `source venv/bin/activate` (On Windows, use `venv\Scripts\activate`)

3. **Install Requirements:**
   - Install the necessary packages from `requirements.txt`:

   `pip install -r requirements.txt`

4. **Create a New Heroku App:**
   - Log in to Heroku from the terminal:

   `heroku login`

   - Create a new Heroku app:

   `heroku create <your-app-name>`

5. **Prepare for Deployment:**
   - Ensure you have a `Procfile` that tells Heroku how to run your app.
   - Make sure your `runtime.txt` specifies the correct Python version.

6. **Add Heroku Remote:**
   - Add Heroku as a remote to your project:

   `heroku git:remote -a <your-app-name>`

7. **Set Up Environment Variables:**
   - Use the following command to add your environment variables (like `SECRET_KEY`, `DEBUG`, and database settings):

   `heroku config:set SECRET_KEY=<your-secret-key> DEBUG=False ALLOWED_HOSTS=<your-app-name>.herokuapp.com`

8. **Push the Code to Heroku:**
   - Commit any changes if necessary and deploy to Heroku:

   `git add .`

   `git commit -m "Initial Heroku deployment"`

   `git push heroku main`

9. **Apply Migrations:**
   - Once the app is deployed, apply the database migrations:

   `heroku run python manage.py migrate`

10. **Create a Superuser (Optional for Admin Access):**
    - Create a superuser to access the Django admin panel:

   `heroku run python manage.py createsuperuser`

11. **Open the App:**
    - After deployment, you can open your Heroku app in the browser:

   `heroku open`

#### **Forking the GitHub Repository**
If you wish to create a safe copy of the project to experiment with changes:

1. Log in to GitHub and navigate to the GitHub Repository.
2. Click the "Fork" button near the top of the page to create a copy of the repository.

#### **Making a Local Clone**
1. Under "Clone with HTTPS", click the clipboard icon to copy the link.
2. Open Git Bash and change the current working directory to the location where you want the cloned directory.
3. Type `git clone`, add a space, and paste the URL that was copied earlier (in step 1). Press enter to create a clone.

## Testing:
The site was tested on various devices and browsers to ensure responsiveness and compatibility.

## Credits
- The like model was inspired by [Django Like Button Tutorial](https://learndjango.com/tutorials/django-like-button-tutorial).
- The colour palette was generated by [Coolors](https://coolors.co/).

## Acknowledgments
- **Mentors & Support**: Special thanks to my mentor Spencer Barriball, for invaluable feedback, and to the support team at Code Institute for assistance.
