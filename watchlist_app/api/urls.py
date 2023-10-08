from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS, UserReview, WatchListGV


router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('list2/', WatchListGV.as_view(), name='watch-list'),
    
    path('', include(router.urls)),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
    
    # path('review', ReviewList.as_view(), name='review_list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    
    path('<int:pk>/review/', ReviewList.as_view(), name='review_list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),
    path('reviews/', UserReview.as_view(), name='user_review_detail'),

]
