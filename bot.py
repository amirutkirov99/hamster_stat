from random import choice
from hamster_client import BOOST_ENERGY, HamsterClient, sleep, logging
from config import TOKENS
from strings import DELIMITER
from hamster_client import send_tg
from background import keep_alive

keep_alive()


   
clients = [HamsterClient(**options) for options in TOKENS]

def main():
    while True:
        for client in clients:
            DELIMITER_TG1 = (
                f"===================\n"
                f"_______{client.name}_______\n"
            )
            DELIMITER_TG2 = (
                f"_______{client.name}_______\n"
                f"==================="
            )
            print(DELIMITER)
            send_tg(DELIMITER_TG1)
            client.sync()
            client.claim_daily_cipher()
            client.tap()
            # client.buy_upgrades()
            client.upgrdades_list()
            client.check_task()
            client.claim_combo_reward()
            if client.is_taps_boost_available:
                client.boost(BOOST_ENERGY)
            logging.info(client.log_prefix + " ".join(f"{k}: {v} |" for k, v in client.stats.items()))
            
            send_tg(f"<b>Статистика</b>\n\n" + "".join(f"{k}: <b><i>{v}</i></b>\n" for k, v in client.stats.items()))
            print(DELIMITER)
            send_tg(DELIMITER_TG2)
            sleep(choice(range(1, 10)))
        sleep(60 * 10)

if __name__ == "__main__":
    main()