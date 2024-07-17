def make_call(phone_num:str):
    """
    function to call a phone number

    Inputs:
        phone_num (str): a phone number to call

    Outputs:
        No output (prints to the screen instead)

    """
    print("Making phone call to {}...number dialed.".format(phone_num))
    print("Survey issued.\nCall Complete.\n##########")

list_of_numbers = [
    "505-503-4455",
    "618-625-8313",
    "719-266-2837",
    "951-262-3062"
]

for phone_num in list_of_numbers:
    make_call(phone_num)
