from scheduler import scheduler


def main():

    price_alert = scheduler(5)
    while True:
        price_alert.animation()

if __name__ == "__main__":
    main()   






