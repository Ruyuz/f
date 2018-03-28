from brokerage import *

# instantiate Stock class
ali  = Stock('Alibaba_Group', 'ABAB')
atnt = Stock('AT&T_INC', 'T')
boa  = Stock('Bank_of_America_Corporation', 'BAC')
banc = Stock('Banc_of_California', 'BANC')
citi = Stock('Citigroup', 'C')
fdx  = Stock('FedEx_Corporation', 'FDX')
ibm  = Stock('International_Business_Machines_Corporation', 'IBM')
macy = Stock('Macy_Inc', 'M')
ms   = Stock('Morgan_Stanley', 'MS')
twitter = Stock('Twitter', 'TWTR')

# instantiate Exchange class
exchange = Exchange('New_York_Stock_Exchange')

exchange.add_security(ali)
exchange.add_security(atnt)
exchange.add_security(boa)
exchange.add_security(banc)
exchange.add_security(citi)
exchange.add_security(fdx)
exchange.add_security(ibm)
exchange.add_security(macy)
exchange.add_security(ms)
exchange.add_security(twitter)

exchange.set_price()

# Returns the average of the bid_price and ask_price of every stock as a list
[ali.midmarket_value,
atnt.midmarket_value,
boa.midmarket_value,
banc.midmarket_value,
citi.midmarket_value,
fdx.midmarket_value,
ibm.midmarket_value,
macy.midmarket_value,
ms.midmarket_value,
twitter.midmarket_value]


# instantiate Broker class
Reid  = Broker('Reid Wharton', 1.23)
Theda = Broker('Theda Richards', 2.02)
Sunny = Broker('Sunny Rice', 1.67)
Joane = Broker('Joane Stubbs', 1.44)
Kate  = Broker('Katelyn Squires', 1.25)
Sarai = Broker('Sarai Lister', 0.98)
Gita  = Broker('Gita Terry', 3.21)

# instantiate Portfolio
port1 = Portfolio('port1')
port1.holdings = {'ABAB': 1000, 'IBM': 800, 'TWTR':700}

port2 = Portfolio('port2')
port2.holdings = {'BAC': 800, 'BANC': 60, 'C':100}

port3 = Portfolio('port3')
port3.holdings = {'T': 300, 'FDX': 200, 'M':800}

# instantiate Investor
Rouie = Investor('Rouie', 50000)
Rouie.portfolios = {'port1': port1, 'port2': port2}


# execute some trades
Rouie.net_worth()
Rouie.execute_trade( Sunny, 'TWTR', 'port1', 100, exchange)
Rouie.net_worth()
Rouie.cash_balance

Rouie.execute_trade( Joane, 'C', 'port2', -200, exchange)
Rouie.net_worth()
Rouie.cash_balance

Rouie.execute_trade( Gita, 'T', 'port3', 100, exchange) # add a new portfolio to investor's portfolios
Rouie.net_worth()
Rouie.cash_balance

# show the investor's holdings of every portfolio after trades
for port in Rouie.portfolios:
	print(Rouie.portfolios[port].holdings)



