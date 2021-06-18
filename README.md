# Fampay (Backend Assignment)

## Important Commands
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
## Basic Requirements
- [ ] Server should call the YouTube API continuously in background (async) which some intervals (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- [ ] A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- [ ] A basic search API to search the stored videos using their title and description.
- [x] Dockerize the project.
- [ ] It should be scalable and optimised.

## Bonus Points
- [ ] Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- [ ] Make a dashboard to view the stored videos with filters and sorting options (optional)
- [ ] Optimise search api, so that it's able to search videos containing partial match for the search query in either video title or description.
