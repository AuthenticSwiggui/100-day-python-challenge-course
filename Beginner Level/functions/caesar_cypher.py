import sys

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def ui():
    should_continue = True
    while should_continue:
        option = get_option()
        message = input("Message: ").lower()
        shift = get_shift()
        message = operacion_cesar(
            original_message=message, 
            shift=shift, 
            option=option)

        print(message)
        repeat = input("Do you want to continue? Yes/No \n")
        if repeat.lower() == "no":
            print("Bye")
            should_continue = False
        
def get_option() -> str:
    while True:
        option = input("What do you want to do?: ").lower()
        if option in ["encode", "decode"]:
            return option
        print("Sea serio mano, encriptar o decodificar")

def get_shift() -> int:
    while True:
        try:
            shift = int(input("Shift to encode: "))
            if shift > 0:
                return shift
            print("Inserte un número mayor a 0 wn")
        except ValueError:
            print("Inserte un número weon")
        
   

def operacion_cesar(original_message: str,
        shift: int,
        option: str) -> str:
    proccessed_message = []
    if option == "decode":
        option = "decoded"
        shift *= -1
    if option == "encode":
        option = "encoded"
    for letter in original_message:
        if letter not in alphabet:
            proccessed_message.append(letter)
            continue
        shifted_position = alphabet.index(letter) + shift
        shifted_position %= len(alphabet)
        proccessed_message.append(alphabet[shifted_position])
    
    proccessed_message = "".join(proccessed_message)
    return f"Here is the {option} message: {proccessed_message}"
    
    
def print_message(message: str) -> None:
    print(message)

def main():
    ui()

if __name__ == '__main__':
    sys.exit(main())