from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaNumericUnderscoreValidator:
    def __init__(self, message: str = None) -> None:
        self.message = message
    
    @property
    def message(self) -> str:
        return self.__message
    
    @message.setter
    def message(self, value: str):
        # if value is None:
        #     self.__message = "Ensure this value contains only letters, numbers, and underscore."
        # else:
        #     self.__message = value

        self.__message = value or "Ensure this value contains only letters, numbers, and underscore."

    def __call__(self, value: str) -> None: # call every time an instance is created
        if not value.replace("_", "").isalnum():
            raise ValidationError(self.message)
