# checks that users enter a valid response (eg yes / no)
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_response):

    while True:

        response = input(question).lower()

        for iten in valid_responses:

# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
