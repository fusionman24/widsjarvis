import re


def phone_numbers(text):
    phone_no = r'\(\d{3}\)\s\d{3}\-\d{4}|\(\d{3}\)\-\d{3}\-\d{4}'

    phone_numbers = re.findall(phone_no, text)
    return phone_numbers


sample_text = """
    Here are some phone numbers:
    (123) 456-7890, 987-654-3210, (555)555-5555.
    Please call these numbers for assistance.
    """

extracted_numbers = phone_numbers(sample_text)

print(extracted_numbers)
