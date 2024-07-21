from fastapi import HTTPException, status

class BaseException(HTTPException):
    status_code = 500  
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
 
 
class UserCannotFindException(BaseException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Пользователь не найден"       
        
class UserAlreadyExistsException(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Пользователь с таким email уже существует"
    
class UserChangeEmailException(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Новая почта совпадает с текущей почтой"
    
class IncorrectEmailOrPasswordException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неправильный email или пароль"


class TokenExpiredException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED 
    detail="Токен истек"


class TokenAbsentException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Токен отсутствует"


class IncorrentTokenFormatException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    detail="Неправильный формат токена"


class UserIsNotPresentException(BaseException):
    status_code=status.HTTP_401_UNAUTHORIZED
    
class RoomCannotBeBooked(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Не осталось своббдных номеров"


class DateFromCannotBeAfterDateTo(BaseException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Дата заезда не может быть позже даты выезда"

class CannotBookHotelForLongPeriod(BaseException):
    status_code=status.HTTP_400_BAD_REQUEST
    detail="Невозможно забронировать отель сроком более месяца"

class CannotAddDataToDatabase(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось добавить запись"
    
    
class RoomFullyBooked(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Не осталось свободных номеров"


class CannotDeleteDataFromDatabase(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось удалить запись"
    
    
class CannotUpdateDataInDatabase(BaseException):
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    detail="Не удалось изменить запись"
    
class NotFoundException(BaseException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Запись не найдена"
    
class NotFoundHotelsException(BaseException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Отель не найден"
    
class HotelAlreadyException(BaseException):
    status_code=status.HTTP_409_CONFLICT
    detail="Отель с таким названием уже существует"
    
class NotFoundRoomsException(BaseException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Номера не найдены"
    

class NotFoundBookingsException(BaseException):
    status_code=status.HTTP_404_NOT_FOUND
    detail="Бронирования не найдены"