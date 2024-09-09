from django.urls import path
from note_api import views
from drf_spectacular import views as schema_views

# write you urls here.
urlpatterns = [
    path('notes/', views.NoteList.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteList.as_view(), name='notes'),
    path('notes', views.QueryNoteListByTitle.as_view(), name='note-query'),

    # Optional: Add schema view
    path('schema/', schema_views.SpectacularAPIView.as_view(), name='schema'),
    # Optional: Add Swagger UI
    path('schema/swagger-ui/', schema_views.SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Optional: Add Redoc UI
    path('schema/redoc/', schema_views.SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]