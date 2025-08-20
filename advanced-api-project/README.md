# Advanced API Project

A Django REST Framework project showcasing advanced concepts like custom serializers, role-based permissions, filtering, searching, ordering, and pagination.

## Features
- Custom DRF serializers and viewsets.
- Role-based permissions.
- Filtering, searching, and ordering.
- Pagination for large datasets.
- Modular and extensible API structure.

## API Endpoints (Example)

| Method | Endpoint                | Description                               |
|--------|--------------------------|-------------------------------------------|
| GET    | `/items/`               | List all items (with pagination & filters)|
| POST   | `/items/create/`        | Create a new item                         |
| GET    | `/items/<id>/`          | Retrieve item details                     |
| PUT    | `/items/<id>/update/`   | Update an item                            |
| DELETE | `/items/<id>/delete/`   | Delete an item                            |

## Learning Outcomes
- Mastery of DRF features (pagination, filters, search).
- Implementation of role-based permissions.
- Advanced API architecture for scalability.
