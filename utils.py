import random
class Utils:

    def guess_number(minimun, maximun, number_to_guess) -> bool:
        successes_counter = 0

        while successes_counter < 3:
            random_number = random.randint(minimun, maximun)

            if random_number == number_to_guess:
                print(f"El número {random_number} es el correcto")
                return True
            elif random_number < number_to_guess:
                print(
                    f"El número {random_number} es menor que el número que se quiere adivinar"
                )
                minimun = random_number + 1
            elif random_number > number_to_guess:
                print(
                    f"El número {random_number} es mayor que el número que se quiere adivinar"
                )
                maximun = random_number - 1

            successes_counter += 1
            print(f"Llevas {successes_counter} desacierto(s)")

        print(f"Perdiste, el número a adivinar era {number_to_guess}")
        return False
