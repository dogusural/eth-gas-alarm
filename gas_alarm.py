from scheduler import scheduler


def main():

    price_alert = scheduler(10)
    while True:
        price_alert.animation()

if __name__ == "__main__":
    main()   






