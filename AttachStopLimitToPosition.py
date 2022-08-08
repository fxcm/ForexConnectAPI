# example code how to attach Stop or Limit to open position, each create_order_request() can attach one order, to attach stop and limit need to call this function 2 times
# this code shows how to attach Limit, for a Stop replace order_type='S'


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


def main():
    str_user_id = 'username'
    str_password = 'password'
    str_url = 'www.fxcorporate.com/Hosts.jsp'
    str_connection = 'Demo'
    str_session_id = None
    str_pin = None
    str_instrument = 'CAD/JPY'
    str_buy_sell = 'B'  # should be oposite direction than open position
    str_rate = 104.610
    str_lots = 10       # Quantity should be the same as open position
    str_account = 'account_id'
    trade_id = 'trade_id'
    stop_ord = 'S'
    limit_ord = 'L'


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
            amount = base_unit_size * str_lots

            request = fx.create_order_request(
                order_type=limit_ord,
                OFFER_ID=offer.offer_id,
                ACCOUNT_ID=str_account,
                BUY_SELL=str_buy_sell,
                AMOUNT=amount,
                RATE=str_rate,
                TRADE_ID=trade_id,
            )

            orders_monitor = OrdersMonitor()

            orders_table = fx.get_table(ForexConnect.ORDERS)
            orders_listener = Common.subscribe_table_updates(orders_table, on_add_callback=orders_monitor.on_added_order)

            try:
                resp = fx.send_request(request)
                order_id = resp.order_id

            except Exception as e:
                common_samples.print_exception(e)
                orders_listener.unsubscribe()

            else:
                # Waiting for an order to appear or timeout (default 30)
                order_row = orders_monitor.wait(30, order_id)
                if order_row is None:
                    print("Response waiting timeout expired.\n")
                else:
                    print("The order has been added. OrderID={0:s}, "
                          "Type={1:s}, BuySell={2:s}, Rate={3:.5f}, TimeInForce={4:s}".format(
                        order_row.order_id, order_row.type, order_row.buy_sell, order_row.rate,
                        order_row.time_in_force))
                    sleep(1)
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
