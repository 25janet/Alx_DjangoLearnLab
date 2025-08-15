Hi! My name is Janet John, an Alx student doing my final project. I am unsure of my work, feel free to correct me if there is any bugs/error.
This is my first ever big project to do,I am very excited

---

# Django Blog Project 💜

## **Overview**

`django_blog` is a fully functional blog application built with **Django**. It features:

* **User authentication** (registration, login, logout, profile management)
* **CRUD operations** for blog posts
* **Comment system**
* **Tagging system**
* **Search functionality**
* **Responsive, purple-themed design**

This project demonstrates core Django features such as class-based views, forms, templates, static files, and third-party packages (`django-taggit`) for tags.

---

## **Table of Contents**

1. [Setup Instructions](#setup-instructions)
2. [Project Structure](#project-structure)
3. [Authentication System](#authentication-system)
4. [Blog Post Management (CRUD)](#blog-post-management-crud)
5. [Comments System](#comments-system)
6. [Tagging & Search](#tagging--search)
7. [Templates & Static Files](#templates--static-files)
8. [Forms](#forms)
9. [URLs](#urls)
10. [Usage Examples](#usage-examples)
11. [Screenshots](#screenshots)
12. [Contributing & Notes](#contributing--notes)

---

## **Setup Instructions**

```bash
git clone https://github.com/yourusername/django_blog.git
cd django_blog
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
pip install -r requirements.txt
pip install django-taggit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **Project Structure**

```
django_blog/
│
├── blog/
│   ├── templates/blog/       # HTML templates
│   ├── static/blog/css/      # Purple-themed CSS
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── django_blog/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
```

---

## **Authentication System**

* **Registration:** Username, email, password
* **Login/Logout:** Django’s built-in authentication
* **Profile Management:** Update username/email
* **Forms:**

  * `CustomUserCreationForm` – registration
  * `UserUpdateForm` – profile update



---

## **Blog Post Management (CRUD)**

* **Post Model:** `title`, `content`, `author`, `published_date`, `tags`
* **Views:**

  * `PostListView` – list all posts
  * `PostDetailView` – single post
  * `PostCreateView` – create post (authenticated users)
  * `PostUpdateView` – edit own post
  * `PostDeleteView` – delete own post
* **Permissions:** Only author can edit/delete
* **Forms:** `PostForm` with `TagWidget()`

---

## **Comments System**

* **Model Fields:** `post`, `author`, `content`, `created_at`, `updated_at`
* **Views:**

  * `CommentCreateView` – add comment
  * `CommentUpdateView` – edit own comment
  * `CommentDeleteView` – delete own comment
* **Integration:** Displayed under posts in `post_detail.html`

---

## **Tagging & Search**

* **Tagging:**

  * `django-taggit` for multiple tags per post
  * Clickable tags filter posts (`PostByTagListView`)
* **Search:**

  * Search by title, content, or tags
  * Search form on post list page

 **Example of search bar style:**

```css
input[type="text"] {
    border: 2px solid #7209b7;
    border-radius: 8px;
    padding: 6px;
}
```

---

## **Templates & Static Files**

* **Templates:** `post_list.html`, `post_detail.html`, `search_results.html`, login/register/profile
* **CSS:** Purple theme, visually appealing
* **Static path:** `blog/static/blog/css/styles.css`

---

## **Forms**

| Form                     | Purpose          | Fields                                |
| ------------------------ | ---------------- | ------------------------------------- |
| `CustomUserCreationForm` | Registration     | username, email, password1, password2 |
| `UserUpdateForm`         | Update profile   | username, email                       |
| `PostForm`               | Create/Edit post | title, content, tags (TagWidget)      |
| `CommentForm`            | Add/Edit comment | content                               |

---

## **URLs**

| URL Pattern                    | View                | Purpose                 |
| ------------------------------ | ------------------- | ----------------------- |
| `/`                            | `PostListView`      | List all posts          |
| `/post/<int:pk>/`              | `PostDetailView`    | Post details + comments |
| `/post/new/`                   | `PostCreateView`    | Create post             |
| `/post/<int:pk>/update/`       | `PostUpdateView`    | Edit post               |
| `/post/<int:pk>/delete/`       | `PostDeleteView`    | Delete post             |
| `/register/`                   | `register_view`     | User registration       |
| `/login/`                      | `login_view`        | Login                   |
| `/logout/`                     | `logout_view`       | Logout                  |
| `/profile/`                    | `profile_view`      | Edit profile            |
| `/post/<int:pk>/comments/new/` | `CommentCreateView` | Add comment             |
| `/comment/<int:pk>/update/`    | `CommentUpdateView` | Edit comment            |
| `/comment/<int:pk>/delete/`    | `CommentDeleteView` | Delete comment          |
| `/search/`                     | `search_posts`      | Search posts            |
| `/tags/<slug:tag_slug>/`       | `PostByTagListView` | Filter posts by tag     |

---

## **Usage Examples**

* **Create Post:** Login → New Post → Add title, content, tags → Submit
* **Comment on Post:** Open post detail → Add comment
* **Edit Post/Comment:** Only visible if you are the author
* **Search Posts:** Enter keyword/tag → Press Search → Results
* **Filter by Tag:** Click tag → Posts with that tag

---





## **Contributing & Notes**

* Built with **Django 4.x** and **Python 3.11+**
* Tags managed with **django-taggit**
* Passwords securely hashed (PBKDF2)
* **CSRF protection** active on all forms
* Purple theme used throughout CSS for visual appeal




