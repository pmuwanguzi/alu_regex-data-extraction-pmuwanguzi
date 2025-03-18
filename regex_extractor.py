import re
"""
This is a regex extractor file, 
it helps pick credit card numbers,
Phone Numbers, Email Addresses and Urls.
"""
def regex_data_extractor(text):
    """
        This function holds the different patters
        to be checked for and returns each in the
        right category.
    """
    # Matching regex for creditcards 
    creditcards = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    # Matching regex for email addresses
    emails = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Matching regex for phone numbers
    phone_numbers= r'(\+\d{1,3}[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})'
    # Matching regex for urls
    urls = r'https?://[^\s/$.?#].[^\s]*'

    # Regex pattern checker object
    regex_patterns = {
        'Credit Cards': creditcards,
        'Emails': emails,
        'Phone Numbers': phone_numbers,
        'URLs': urls
    }
    for data_label, regex in regex_patterns.items():
        print(f"{data_label}: {re.findall(regex, text)}")


# Randomly generated test text:
text =""" 
https://www.abcdxyz.com +441234567890  +256782348523 test data sample python world random 4256 3847 1234 8723 tbmgurzyx@example.com world hello generate random 4762-2947-8320-6573 https://www.sdklop.net pqldmvscw@yahoo.com +12-987-654-3210 generate python test sample 4267-3829-4958-9283 https://www.bocijkh.com vlknxyf@example.com +33-234-567-8912"""

regex_data_extractor(text)