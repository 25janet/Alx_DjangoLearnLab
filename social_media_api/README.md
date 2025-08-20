# Social Media API

A social media backend built with Django REST Framework. This project demonstrates advanced REST API design, user engagement features, and notifications.

## Features
- JWT authentication.
- CRUD for posts and comments.
- Like/unlike functionality.
- Follow/unfollow users.
- Notifications (likes, comments, follows).
- Post feed from followed users.
- Pagination, filtering, and search.

## API Endpoints

### Authentication
| Method | Endpoint              | Description               |
|--------|------------------------|---------------------------|
| POST   | `/auth/register/`      | Register a new user       |
| POST   | `/auth/login/`         | Login and obtain JWT      |
| POST   | `/auth/logout/`        | Logout and blacklist JWT  |

### Posts
| Method | Endpoint               | Description                     |
|--------|-------------------------|---------------------------------|
| GET    | `/posts/`              | List all posts (paginated)      |
| POST   | `/posts/create/`       | Create a new post               |
| GET    | `/posts/<id>/`         | Retrieve post details           |
| PUT    | `/posts/<id>/update/`  | Update a post                   |
| DELETE | `/posts/<id>/delete/`  | Delete a post                   |

### Comments
| Method | Endpoint                        | Description                          |
|--------|----------------------------------|--------------------------------------|
| POST   | `/posts/<id>/comment/`           | Add a comment to a post              |
| GET    | `/posts/<id>/comments/`          | Retrieve comments for a post         |

### Likes
| Method | Endpoint                  | Description           |
|--------|----------------------------|-----------------------|
| POST   | `/posts/<id>/like/`       | Like a post           |
| POST   | `/posts/<id>/unlike/`     | Unlike a post         |

### Followers
| Method | Endpoint                         | Description                  |
|--------|-----------------------------------|------------------------------|
| POST   | `/users/<id>/follow/`            | Follow a user                |
| POST   | `/users/<id>/unfollow/`          | Unfollow a user              |

### Notifications
| Method | Endpoint                 | Description                         |
|--------|---------------------------|-------------------------------------|
| GET    | `/notifications/`         | Retrieve user notifications         |
| GET    | `/notifications/unread/`  | Retrieve unread notifications only  |

## Learning Outcomes
- JWT authentication in DRF.
- User relationship features (follows, likes).
- Notification system.
- Scalable REST API design.
