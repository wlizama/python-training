
def palindromo(sstr):
    if len(sstr) < 2:
        return True
    if sstr[0] != sstr[-1]:
        return False
    return palindromo(sstr[1:-1])


def main():
    sstr = input("Palabra a evaluar: ").lower()
    str_if_p = "SI" if palindromo(sstr) else "NO"
    print(f"La palabra \"{sstr}\" {str_if_p} es palindromo")


if __name__ == "__main__":
    main()