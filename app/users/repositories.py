

from app.repositories.base import BaseRepositories
from app.users.models import Users


class UserRepository(BaseRepositories):
    model = Users