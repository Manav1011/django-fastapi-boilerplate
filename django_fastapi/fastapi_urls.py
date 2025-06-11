from fastapi import APIRouter
from django.contrib.auth import get_user_model

User = get_user_model()

base_router = APIRouter()