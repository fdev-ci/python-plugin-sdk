# -*- coding: utf-8 -*-

# 输出输出位置和文件名存储的环境变量名称
CI_DATA_DIR = "ci_data_dir"
CI_DATA_INPUT = "ci_data_input"
CI_DATA_OUTPUT = "ci_data_output"

#  插件输出状态
CI_PLUGIN_STATUS = {
    "SUCCESS": "success",
    "FAILURE": "failure",
    "ERROR": "error"
}

#  插件输出模版类型
CI_OUTPUT_TEMPLATE_TYPE = {
    "DEFAULT": "default"
}

#  插件输出字段类型
CI_OUTPUT_FIELD_TYPE = {
    "STRING": "string"
}


class Status:
    """
    @summary:  插件执行结果定义
    """
    ERROR = CI_PLUGIN_STATUS.get("ERROR", None)
    FAILURE = CI_PLUGIN_STATUS.get("FAILURE", None)
    SUCCESS = CI_PLUGIN_STATUS.get("SUCCESS", None)


class OutputTemplateType:
    """
    @summary:  插件输出模版类型
    """
    DEFAULT = CI_OUTPUT_TEMPLATE_TYPE.get("DEFAULT", None)


class OutputFieldType:
    """
    @summary:  插件输出字段类型
    """
    STRING = CI_OUTPUT_FIELD_TYPE.get("STRING", None)
