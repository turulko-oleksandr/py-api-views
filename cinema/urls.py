from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cinema.views import (
    movie_list,
    movie_detail,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallViewSet,
    MovieViewSet,
)

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")

cinema_hall_list = CinemaHallViewSet.as_view({
    "get": "list",
    "post": "create",
})
cinema_hall_detail = CinemaHallViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})

urlpatterns = [
    # FBV Movies
    path("movies-fbv/", movie_list, name="movie-list-fbv"),
    path("movies-fbv/<int:pk>/", movie_detail, name="movie-detail-fbv"),

    # APIView Genres
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # GenericAPIView Actors
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),

    # GenericViewSet CinemaHalls
    path("cinema-halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/",
         cinema_hall_detail, name="cinema-hall-detail"),

    # ModelViewSet Movies (using router)
    path("", include(router.urls)),
]

app_name = "cinema"
