import random

class Stock(object):

	def __init__(self, company_name, ticker_symbol):
		self.company_name = company_name
		self.ticker_symbol = ticker_symbol
		self.bid_price = 0
		self.ask_price = 0

	@property
	def midmarket_value(self):
		return (self.bid_price + self.ask_price) * 0.5

class Exchange(object):
	securities = {} #keys are ticker symbols and the values are instances of the Stock class.

# Imagine, for simplicity's sake, that we're operating in a world where we have just one exchange. 
# The module will instantiate exactly one exchange and this exchange is available as a global attribute of the module in any of your classes defined therein.

	def __init__(self, name ):
		self.name = name

	def add_security(self, stock):
		self.securities[stock.ticker_symbol] = stock

	def set_price(self):
		for key in self.securities:
			ask = random.uniform(0,1000)
			bit = ask * (1 - random.uniform(0.5, 2)/100)
			self.securities[key].bid_price = bit
			self.securities[key].ask_price = ask 

class Broker(object):
	def __init__(self, name, per_share_commission_amount):
		self.name = name
		self.per_share_commission_amount = per_share_commission_amount

class Portfolio(object):
	def __init__(self, name):
		self.name = name # purpose of the portfolio
		self.holdings = {} # keys are ticker symbols and the values represent the number of shares
	
	@staticmethod
	def get_bid_price(ticker_symbol): # suppose we have just one exchange
		return exchange.securities[ticker_symbol].bid_price

	@staticmethod
	def get_ask_price(ticker_symbol):
		return exchange.securities[ticker_symbol].ask_price


	def update_position(self, ticker_symbol, shares_purchased):
		if ticker_symbol in self.holdings:
			self.holdings[ticker_symbol] += shares_purchased
		else:
			self.holdings[ticker_symbol] = shares_purchased


	def current_value(self):
		sum = 0
		for key in self.holdings:
			if self.holdings[key] > 0:
				sum = sum + self.holdings[key]* Portfolio.get_ask_price(key)
			else:
				sum = sum + self.holdings[key]* Portfolio.get_bid_price(key)
		return sum


class Investor(object):

	def __init__(self, name, cash_balance):
		self.name = name
		self.cash_balance = cash_balance
		self.portfolios = {} # keys are portfolio names, values are instances of the Portfolio class.

	def execute_trade(self, broker, ticker_symbol, portfolio_name, quantity, exchange):

		if portfolio_name in self.portfolios:
			self.portfolios[portfolio_name].update_position(ticker_symbol, quantity)
		else:
			self.portfolios[portfolio_name] = Portfolio(portfolio_name)
			self.portfolios[portfolio_name].update_position(ticker_symbol, quantity)

		if quantity > 0: # positive --> buy
			self.cash_balance -= (exchange.securities[ticker_symbol].ask_price + broker.per_share_commission_amount) * quantity
		else: # negative --> sell
			self.cash_balance -= (exchange.securities[ticker_symbol].bid_price - broker.per_share_commission_amount) * quantity


	def net_worth(self):
		sum = 0
		for name in self.portfolios:
			sum = sum + self.portfolios[name].current_value()
		return sum













