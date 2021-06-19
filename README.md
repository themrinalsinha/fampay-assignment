# Fampay (Backend Assignment)

## Available Commands
Pre-requisite: `docker`, `docker-compose` & `make`

- To run the application
  ```shell
  $ make
  ```
- To run django shell
  ```shell
  $ make shell
  ```
- To run `migrations` and `migrate`
  ```shell
  $ make syncdb
  ```
- To open `db` shell
  ```shell
  $ make psql
  ```
----
**Local application setup**
- To run all the application
  ```shell
  $ make
  ```
- once the application is up and running, in another shell run
  ```shell
  $ make syncdb
  ```
  It will run and apply all the database migration
- Then, we'll create a superuser, just run
  ```
  $ make user
  ```
  it will create a superuser user username (`admin`) and password (`admin`).
- Login to admin panel, goto `http://127.0.0.1:9090/admin/`
- Under `YT_APP` there is `Key Manager` just your YouTube access key there.
- The system will pick the keys from here and use to data polling
- Done!

**Observation**
- Under `CELERY RESULTS` > `Task Results` you can see what is the task status
- Default search params and frequency
  ```ini
  SEARCH_QUERY=bitcoin # default
  QUERY_PER_PAGE=20
  REFRESH_FREQUENCY=30 # 30 second frequency
  ```
  you can override these settings by adding `environment` variables in `docker-compose.yml` or `local.env`


APIs
- List API
  ```
  http://127.0.0.1:9090/api/v1/list/
  ```
  ```json
  {
    "count": 120,
    "next": "http://127.0.0.1:9090/api/v1/list/?limit=10&offset=10",
    "previous": null,
    "results": [
        ... data
    ]
  }
  ```
- Search Filter (works on `title` and `description`)
  ```
  http://127.0.0.1:9090/api/v1/list/?search=bitcoin%20death
  ```
  ```json
  {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        ... data
    ]
  }
  ```

----
## Basic Requirements
- [x] Server should call the YouTube API continuously in background (async) which some intervals (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [x] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [x] A basic search API to search the stored videos using their title and description.
- [x] Dockerize the project.
- [x] It should be scalable and optimised.

## Bonus Points
- [x] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [ ] Make a dashboard to view the stored videos with filters and sorting options (optional) **NOTE** `Implemented using django admin`
- [x] Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
