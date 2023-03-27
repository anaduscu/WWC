from domain import metaClass

class CreateQuoteRequest(metaclass=metaClass.AutoGetSet):
    _attributes = ['sourceCurrency', 'targetCurrency', 'targetAmount', 'sourceAmount', 'profile']
    def __init__(self, sourceCurrency, targetCurrency, targetAmount, sourceAmount):
        self._sourceCurrency = sourceCurrency
        self._targetCurrency = targetCurrency
        self._targetAmount = targetAmount
        self._sourceAmount = sourceAmount
        # self._profile = 16727665

  
    
   
        

    
  

    
    