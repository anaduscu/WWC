
from domain import CreateQuoteRequest, CreateRecipientRequest, RecipientAccountDetails, Address
from service import transferService

class DemoApplication:
    def main(self):
        token = transferService.TransferService.generateToken()
        print(token)
        createQuoteRequest = self.getQuoteRequest()
        response = transferService.TransferService.createQuote(createQuoteRequest, token)
        if(response.status_code != 200) :
            print("Quote creation failed")
        else:
            print("Created quote id ",response.json()["id"])

        self.createRecipient(createQuoteRequest._targetCurrency, token)
        if targetCurrency == "EUR":
            recipient.id = 148762936
        elif targetCurrency == "GBP":
            recipient.id = 148762968
        self.updateQuote()


    def getQuoteRequest(self):
        sourceCurrency = input("From which currency would you like to transfer? Please enter the currency code. (e.g., GBP)")
        targetCurrency = input("What currency do you want to transfer to (e.g. EUR)?")
        sourceAmount = input("How much would you like to transfer? Please enter the amount in numbers (up to 50,000).")
        print("Creating a quote...")
        quote = CreateQuoteRequest.CreateQuoteRequest(sourceCurrency=sourceCurrency, targetCurrency=targetCurrency, targetAmount=None, sourceAmount=sourceAmount)
        quote.sourceCurrency = sourceCurrency
        quote.targetCurrency= targetCurrency
        quote.sourceAmount = sourceAmount
        return quote
    

    def createRecipient(self, targetCurrency, token):
        print("Please enter recipient account details:")
        accountNumber = input("Account number")
        email = input("Email")
        accountType = input("Account type:(eg CHECKING)")
        print("Creating receiver account...")
        recipient = CreateRecipientRequest.CreateRecipientRequest()
        recipient._currency = targetCurrency
        recipient._type = "ABA"
        recipient._accountHolderName = "Receiver Account"
        details = RecipientAccountDetails.RecipientAccountDetails()
        details._accountNumber = accountNumber
        details._email=email
        details._accountType=accountType
        details._address=Address.Address()
        recipient._details=details
        response = transferService.TransferService.createRecipient(recipient, token)
    
        if(response.status_code != 200) :
            print("Creation failed")
        else:
             print("SUCCESSFUL!")


bb = DemoApplication()
bb.main()



