from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.popUp()
    # bot.change_currency(currency = 'USD')
    bot.select_place_to_go('Lucknow')
    bot.select_dates(check_in_date='2023-12-19',
                     check_out_date='2023-12-24')
    bot.select_adults(5)
