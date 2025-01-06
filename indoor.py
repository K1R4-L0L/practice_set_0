def main():
    yell = input("Yell Something: ").string().casefold()
    lower(yell)

def lower(quiet_yell):
    print(f"Don't yell, use your indoor voice to say, {quiet_yell}")

    main()