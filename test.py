import pytest
from app.model.input_config_model import InputDataModelFromConfig
from app.service.flie_url_loader import UrlProvider
from app.controller.processing import ProcessFlow

@pytest.fixture()
def checkConfig():
    CheckConfig = InputDataModelFromConfig()
    return CheckConfig

def test_server_url(checkConfig):
    checkConfig.config_file=='Configurations.ini'


def test_base_url(checkConfig):
    checkConfig.base_url=='https://www.aihw.gov.au/reports-data/health-welfare-services/homelessness-services/data'


def test_base_dir(checkConfig):
    checkConfig.base_dir


def test_temp_dir(checkConfig):
    checkConfig.temp_dir


def test_work_dir(checkConfig):
    checkConfig.work_dir


def test_output_dir(checkConfig):
    checkConfig.output_dir


def test_file_name(checkConfig):
    checkConfig.file_name=='Data tables: Historical tables'


def test_output_file(checkConfig):
    checkConfig.output_file


# def test_main():
#     data_model = InputDataModelFromConfig('Configurations.ini')
#     processor = ProcessFlow(config_model=data_model)
