import unittest
import mock
from mock import patch, Mock
import sys
sys.modules['ds18b20'] = Mock()
sys.modules['RPi'] = Mock()
import thermostat

class TestPsyduck(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('thermostat.get_heat_pin')
    @patch('thermostat.get_temperature')
    @patch('thermostat.get_threshold')
    @patch('thermostat.heat_off')
    def test_heat_off(self, get_heat_pin, get_temperature_mock,
        get_threshold_mock, heat_off_mock):
        get_temperature_mock.return_value = 20
        get_threshold_mock.return_value = 15
        thermostat.check()
        heat_off_mock.assert_called_once()
        get_heat_pin.assert_called_once()

    @patch('thermostat.get_heat_pin')
    @patch('thermostat.get_temperature')
    @patch('thermostat.get_threshold')
    @patch('thermostat.heat_on')
    def test_heat_on(self, get_heat_pin, get_temperature_mock,
        get_threshold_mock, heat_on_mock):
        get_temperature_mock.return_value = 15
        get_threshold_mock.return_value = 20
        thermostat.check()
        heat_on_mock.assert_called_once()
        get_heat_pin.assert_called_once()