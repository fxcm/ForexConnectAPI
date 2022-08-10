# example code how to change order, it can be used for any waiting order, attached stop or limit
#the AMOUNT field is optional,


import argparse
from time import sleep
from threading import Event

from forexconnect import fxcorepy, ForexConnect, Common

import common_samples


def parse_args():
    parser = argparse.ArgumentParser(description='Process command parameters.')
    common_samples.add_main_arguments(parser)
    common_samples.add_instrument_timeframe_arguments(parser, timeframe=False)
    common_samples.add_direction_rate_lots_arguments(parser)
    common_samples.add_account_arguments(parser)
    args = parser.parse_args()

    return args


class OrdersMonitor:
    def __init__(self):
        self.__order_id = None
        self.__orders = {}
        self.__event = Event()

    def on_added_order(self, _, __, order_row):
        order_id = order_row.order_id
        self.__orders[order_id] = order_row
        if self.__order_id == order_id:
            self.__event.set()

    def wait(self, time, order_id):
        self.__order_id = order_id

        order_row = self.find_order(order_id)
        if order_row is not None:
            return order_row

        self.__event.wait(time)

        return self.find_order(order_id)

    def find_order(self, order_id):
        if order_id in self.__orders:
            return self.__orders[order_id]
        else:
            return None

    def reset(self):
        self.__order_id = None
        self.__orders.clear()
        self.__event.clear()


class Args:
    l = "username"
    p = "password"
    u = "http://www.fxcorporate.com/Hosts.jsp"
    c = "Demo"
    i = 'CAD/JPY'
    session = None
    pin = None
    lots = 10
    r = 104.568
    stop_ord = 'S'
    limit_ord = 'L'
    account = 'account id'
    order_id = 'order_id'


def main():
    args = Args
    str_user_id = args.l
    str_password = args.p
    str_url = args.u
    str_connection = args.c
    str_session_id = args.session
    str_pin = args.pin
    str_instrument = args.i
    str_rate = args.r
    lots = args.lots
    str_account = args.account
    str_order_type = args.limit_ord
    order_id = args.order_id


    with ForexConnect() as fx:
        fx.login(str_user_id, str_password, str_url, str_connection, str_session_id, str_pin, common_samples.session_status_changed)

        try:
            account = Common.get_account(fx, str_account)
            if not account:
                raise Exception("The account '{0}' is not valid".format(str_account))

            else:
                str_account = account.account_id
                print("AccountID='{0}'".format(str_account))

            offer = Common.get_offer(fx, str_instrument)

            if offer is None:
                raise Exception("The instrument '{0}' is not valid".format(str_instrument))

            login_rules = fx.login_rules
            trading_settings_provider = login_rules.trading_settings_provider 
            base_unit_size = trading_settings_provider.get_base_unit_size(str_instrument, account)
            amount = base_unit_size * lots

            request = fx.create_order_request(
                command=fxcorepy.Constants.Commands.EDIT_ORDER,
                order_type=str_order_type,
                OFFER_ID=offer.offer_id,
                ACCOUNT_ID=str_account,
                RATE=str_rate,
                AMOUNT=lots,
                ORDER_ID=order_id,
            )

            orders_monitor = OrdersMonitor()

            orders_table = fx.get_table(ForexConnect.ORDERS)
            orders_listener = Common.subscribe_table_updates(orders_table, on_add_callback=orders_monitor.on_added_order)

            try:
                resp = fx.send_request(request)

            except Exception as e:
                common_samples.print_exception(e)
                orders_listener.unsubscribe()

        except Exception as e:
            common_samples.print_exception(e)
        try:
            fx.logout()
        except Exception as e:
            common_samples.print_exception(e)


if __name__ == "__main__":
    main()
    input("Done! Press enter key to exit\n")
