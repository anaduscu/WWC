from domain import RecipientAccountDetails, metaClass

class CreateRecipientRequest(metaclass=metaClass.AutoGetSet):
    _attributes = ['accountHolderName', 'currency', 'type', 'details']

    def __init__(self, accountHolderName, currency, ty, details):
        self._accountHolderName = accountHolderName
        self._currency = currency
        self._type = ty
        self._details = details

    def __init__(self):
        self._accountHolderName = None
        self._currency = None
        self._type = None
        self._details = None

    def to_dict(self):
        return self.__dict__