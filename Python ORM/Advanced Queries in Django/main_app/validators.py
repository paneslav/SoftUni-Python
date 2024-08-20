from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


class RangeValidator:
    def __init__(self, min_value: int, max_value: int, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}"
        else:
            self.__message = value

    def __call__(self, value: int):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.RangeValidator',
            [self.min_value, self.max_value],
            {'message': self.message},
        )

# @deconstructible
# class RangeValidator:
#     def __init__(self, min_value, max_value, message):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.message = message
#
#     def __call__(self, value):
#         if not self.min_value <= value <= self.max_value:
#             raise ValidationError(self.message)
#
#     def __eq__(self, other):
#         return (
#                 isinstance(other, RangeValidator) and
#                 self.min_value == other.min_value and
#                 self.max_value == other.max_value and
#                 self.message == other.message
#         )
#
#     def deconstruct(self):
#         return (
#             self.__class__.__qualname__,
#             (self.min_value, self.max_value, self.message),
#             {}
#         )
