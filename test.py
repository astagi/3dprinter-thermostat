import unittest
import mock
from mock import patch
import thermostat

class TestPsyduck(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('thermostat.heat_on')
    @patch('thermostat.get_threshold')
    @patch('thermostat.get_temperature')
    def test_thremostat_on(self, get_temperature_mock, get_threshold_mock,
        heat_on_mock):
        get_temperature_mock.return_value = 20
        get_threshold_mock.return_value = 15
        thermostat.check(12)
        heat_on_mock.assert_called_once()

    @patch('thermostat.heat_off')
    @patch('thermostat.get_threshold')
    @patch('thermostat.get_temperature')
    def test_thremostat_off(self, get_temperature_mock, get_threshold_mock,
        heat_off_mock):
        get_temperature_mock.return_value = 15
        get_threshold_mock.return_value = 20
        thermostat.check(12)
        heat_off_mock.assert_called_once()