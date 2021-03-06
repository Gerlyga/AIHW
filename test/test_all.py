import pytest
from app.model.input_model_from_config import InputModelFromConfig
from app.model.input_model_from_config_web import InputModelFromConfigWeb
from app.controller.process_flow import ProcessFlow
from app.service.url_provider import UrlProvider
import mock


@pytest.fixture()
def check_config():
    CheckConfig = InputModelFromConfig()
    return CheckConfig


@pytest.fixture()
def check_config_web():
    _check_config_web = InputModelFromConfigWeb()
    return _check_config_web


def test_config_web(check_config_web):
    check_config_web.config_file_web == 'configs/configurations_web.ini'


def test_config(check_config):
    check_config.config_file == 'configs/configurations.ini'


def test_base_url(check_config_web):
    check_config_web.base_url == 'https://www.aihw.gov.au/reports-data/health-welfare-services/homelessness-services/data'


def test_base_dir(check_config):
    check_config.base_dir


def test_temp_dir(check_config):
    check_config.temp_dir


def test_work_dir(check_config):
    check_config.work_dir


def test_output_dir(check_config):
    check_config.output_dir


def test_file_name(check_config_web):
    check_config_web.file_name == 'Data tables: Historical tables'


def test_output_file(check_config):
    check_config.output_file


def test_get_download_link(check_config, check_config_web):
    processor = ProcessFlow(config_model=check_config, config_model_web=check_config_web)
    assert processor._get_link() == 'https://www.aihw.gov.au/getmedia/5e16ec41-9bfa-4a33-bffa-9081a759cd9b/aihw-hou-299-historical.xlsx.aspx'


def test_download_file(check_config, check_config_web):
    processor = ProcessFlow(config_model=check_config, config_model_web=check_config_web)
    assert processor.download_file()


def test_get_convert_to_csv(check_config, check_config_web):
    processor = ProcessFlow(config_model=check_config, config_model_web=check_config_web)
    assert processor.get_convert_to_csv()


def test_get_converter(check_config, check_config_web):
    processor = ProcessFlow(config_model=check_config, config_model_web=check_config_web)
    assert processor.get_converter()
