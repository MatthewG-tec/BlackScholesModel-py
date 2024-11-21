# BlackScholesTest.py
import unittest
from unittest.mock import patch
from blackscholes import black_scholes_call, black_scholes_put, black_scholes_call_div, black_scholes_put_div

class TestBlackScholes(unittest.TestCase):

    @patch('main.get_manual_inputs', return_value=(
        'AAPL',        # stock_name
        150,           # stock_price
        155,           # strike_price
        0.02,          # risk_free_rate
        0.5,           # time_to_maturity
        0.25,          # volatility
        0.03,          # dividend_yield
        5.00,          # call_market_price
        7.00           # put_market_price
    ))
    def test_get_manual_inputs(self, mock_get_manual_inputs):
        stock_name, stock_price, strike_price, risk_free_rate, time_to_maturity, volatility,dividend_yield, call_market_price, put_market_price = mock_get_manual_inputs()

        # Assert that the function returns the correct values
        self.assertEqual(stock_name, 'AAPL')
        self.assertEqual(stock_price, 150)
        self.assertEqual(strike_price, 155)
        self.assertEqual(risk_free_rate, 0.02)
        self.assertEqual(time_to_maturity, 0.5)
        self.assertEqual(volatility, 0.25)
        self.assertEqual(dividend_yield, 0.03)
        self.assertEqual(call_market_price, 5.00)
        self.assertEqual(put_market_price, 7.00)

    # Test for call price calculation (no dividend)
    def test_black_scholes_call(self):
        result = black_scholes_call(150.0, 145.0, 1.0, 0.05, 0.2)
        self.assertAlmostEqual(result, 18.49, places=2)

    # Test for put price calculation (no dividend)
    def test_black_scholes_put(self):
        result = black_scholes_put(150.0, 145.0, 1.0, 0.05, 0.2)
        self.assertAlmostEqual(result, 6.42, places=2)

    # Test for call price calculation with dividend
    def test_black_scholes_call_div(self):
        result = black_scholes_call_div(150.0, 145.0, 1.0, 0.05, 0.03, 0.2)
        self.assertAlmostEqual(result, 15.52, places=2)

    # Test for put price calculation with dividend
    def test_black_scholes_put_div(self):
        result = black_scholes_put_div(150.0, 145.0, 1.0, 0.05, 0.03, 0.2)
        self.assertAlmostEqual(result, 7.88, places=2)

