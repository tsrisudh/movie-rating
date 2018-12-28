# moview-rating
Movie-rating is a simple dockerized python application to get Rotten Tomotaoes rating for a given movie using the open source OMDB api http://www.omdbapi.com/.

### Build
You can build using the docker image tsrisudh/movie-rating
```
docker pull tsrisudh/movie-rating
```

Alternatively you can build locally using the Dockerfile provided

```
docker build -t movie-rating .
```

### Usage

To get the Rotten Tomatoes rating for a movie you can run as below
```
docker run tsrisudh/movie-rating <movie name>
```
For example
```
docker run tsrisudh/movie-rating The Godfather
```
would give the below output
```
Rotten Tomatoes rating for Movie 'The Godfather' is 98%
```
