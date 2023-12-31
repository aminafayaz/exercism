EXPECTED_BAKE_TIME = 40 
PREPARATION_TIME = 2

def bake_time_remaining(time_elapsed):
    
    """Calculate the bake_time_remaining

 
    :param time_elapsed: int - baking time already elapsed.
    :return: int - time_left (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_elapsed
  
  
def preparation_time_in_minutes(no_of_layers):

    """Calculate the preparation time remaining

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time for preparation.
 
    Function that takes the actual no of layers to be added as
    an argument and returns how many minutes the preparation time is.
    """
    return no_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(no_of_layers, time_elapsed):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(no_of_layers) + time_elapsed
