

from app.hotels.models import Hotels
from app.repositories.base import BaseRepositories


class HotelsRepository(BaseRepositories):
    model = Hotels