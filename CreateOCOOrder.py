import argparse
from distutils.cmd import Command
from time import sleep
from threading import Event
from tkinter import COMMAND

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
    l = "YOUR USERNAME/LOGIN"
    p = "LOGIN PASSWORD"
    u = "http://www.fxcorporate.com/Hosts.jsp"
    c = "Demo"
    i = 'EUR/USD'
    session = None


    pin = None
    amount = 10000
    r_up = 1.059
    r_dn = 1.051
    account = 'ACCOUNT ID'

def main():
    #args = parse_args()
    args = Args

    str_user_id = args.l
    str_password = args.p
    str_url = args.u
    str_connection = args.c
    str_session_id = args.session
    str_pin = args.pin
    str_instrument = args.i
    rate_up = args.r_up
    rate_dn = args.r_dn
    str_amount = args.amount
    str_account = args.account

    with ForexConnect() as fx:
        fx.login(str_user_id, str_password, str_url, str_connection, str_session_id,
                 str_pin, common_samples.session_status_changed)

        try:
            account = Common.get_account(fx, str_account)
            if not account:
                raise Exception(
                    "The account '{0}' is not valid".format(str_account))

            else:
                str_account = account.account_id
                print("AccountID='{0}'".format(str_account))

            offer = Common.get_offer(fx, str_instrument)

            if offer is None:
                raise Exception(
                    "The instrument '{0}' is not valid".format(str_instrument))

            login_rules = fx.login_rules

            trading_settings_provider = login_rules.trading_settings_provider

            base_unit_size = trading_settings_provider.get_base_unit_size(
                str_instrument, account)

            amount = base_unit_size * str_lots

            entry = fxcorepy.Constants.Orders.ENTRY

            valuemap_oco = fx.session.request_factory.create_value_map()
            valuemap_oco.set_string(fxcorepy.O2GRequestParamsEnum.COMMAND, fxcorepy.Constants.Commands.CREATE_OCO)

            valuemap_up = fx.session.request_factory.create_value_map()
            valuemap_up.set_string(fxcorepy.O2GRequestParamsEnum.COMMAND, fxcorepy.Constants.Commands.CREATE_ORDER)
            valuemap_up.set_string(fxcorepy.O2GRequestParamsEnum.ORDER_TYPE, fxcorepy.Constants.Orders.STOP_ENTRY)
            valuemap_up.set_string(fxcorepy.O2GRequestParamsEnum.ACCOUNT_ID, str_account)
            valuemap_up.set_string(fxcorepy.O2GRequestParamsEnum.OFFER_ID, offer.offer_id)
            valuemap_up.set_string(fxcorepy.O2GRequestParamsEnum.BUY_SELL, fxcorepy.Constants.BUY)
            valuemap_up.set_int(fxcorepy.O2GRequestParamsEnum.AMOUNT, str_lots)
            valuemap_up.set_double(fxcorepy.O2GRequestParamsEnum.RATE, rate_up)
            valuemap_oco.append_child(valuemap_up)

            valuemap_down = fx.session.request_factory.create_value_map()
            valuemap_down.set_string(fxcorepy.O2GRequestParamsEnum.COMMAND, fxcorepy.Constants.Commands.CREATE_ORDER)
            valuemap_down.set_string(fxcorepy.O2GRequestParamsEnum.ORDER_TYPE, fxcorepy.Constants.Orders.STOP_ENTRY)
            valuemap_down.set_string(fxcorepy.O2GRequestParamsEnum.ACCOUNT_ID, str_account)
            valuemap_down.set_string(fxcorepy.O2GRequestParamsEnum.OFFER_ID, offer.offer_id)
            valuemap_down.set_string(fxcorepy.O2GRequestParamsEnum.BUY_SELL, fxcorepy.Constants.SELL)
            valuemap_down.set_int(fxcorepy.O2GRequestParamsEnum.AMOUNT, str_amount)
            valuemap_down.set_double(fxcorepy.O2GRequestParamsEnum.RATE, rate_dn)
            valuemap_oco.append_child(valuemap_down)

            request = fx.session.request_factory.create_order_request(valuemap_oco)

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
