## How to run the application
### Pre-requisites
- Install [Docker](https://docs.docker.com/engine/install/)
- Install an API testing client. I used [Postman](https://www.postman.com/downloads/)

### Steps:
1. Clone the repository, navigate to the application, and run the Docker containers
```bash
$ git clone https://github.com/domjoeymoncada/wingz-django-assessment
$ cd wingz-django-assessment/
$ docker compose up -d
```

You can check the docker container's status by running:
```bash
$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED      STATUS                  PORTS                                         NAMES
82a269c1bc75   wingz-django-assessment-web   "python manage.py ru…"   5 days ago   Up 2 seconds            0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   wingz-django-assessment-web-1
170d06298131   postgres:latest               "docker-entrypoint.s…"   5 days ago   Up 2 seconds (healthy)  0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp   wingz-django-assessment-db-1
```

### Commonly used endpoints

`RideViewSet` and `UserViewSet` are `ModelViewSet`s, so full CRUD is available. The routes below are the ones used most for testing.

**Authentication:** every API call must use **HTTP Basic Auth** (`username` / `password`). The authenticated user **must** have `role` set to **`admin`**.

#### `GET /api/rides/`

Returns a paginated list of rides.

| Query param | Purpose |
| --- | --- |
| `status` | Filter by ride status |
| `rider__email` | Filter by the rider's email |
| `ordering=pickup_time` | Sort by pickup time (`-pickup_time` for descending) |
| `page`, `page_size` | Pagination |

#### `POST /api/users/`

Creates a user. Send JSON like:

```json
{
    "username": "test_admin",
    "password": "admin123",
    "phone_number": "1000000002",
    "role": "admin",
    "first_name": "Admin",
    "last_name": "Nimda",
    "email": "admin.nimda@gmail.com"
}
```

`role` is `admin` or `user`.

---

## Remaining tasks and challenges during development
- [ ] Sorting by pickup GPS location distance
- [ ] Bonus SQL statement to return driver's rides that took more than 1 hour