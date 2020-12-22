# -*- coding: utf-8 -*-
from .log import logger, getLogger
from .input import ParseParams
from .output import SetOutput
from .const import Status, OutputTemplateType, OutputFieldType

log = logger()
params = ParseParams().get_input()
status = Status()
output_template_type = OutputTemplateType()
output_field_type = OutputFieldType()


def get_input():
    """
    @summary: 获取 插件输入参数
    @return dict
    """
    return params


def get_project_name():
    """
    @summary: 获取项目英文名
    """
    return params.get("project.name", None)


def get_project_name_cn():
    """
    @summary: 获取项目中文名
    """
    return params.get("project.name.chinese", None)


def get_pipeline_id():
    """
    @summary: 获取流水线ID
    """
    return params.get("pipeline.id", None)


def get_pipeline_name():
    """
    @summary: 获取流水线名称
    """
    return params.get("pipeline.name", None)


def get_pipeline_build_id():
    """
    @summary: 获取buildId
    """
    return params.get("pipeline.build.id", None)


def get_pipeline_build_num():
    """
    @summary: 获取buildno
    """
    return params.get("pipeline.build.num", None)


def get_pipeline_start_type():
    """
    @summary: 获取流水线启动类型
    """
    return params.get("pipeline.start.type", None)


def get_pipeline_start_user_id():
    """
    @summary: 获取流水线启动人
    """
    return params.get("pipeline.start.user.id", None)


def get_pipeline_start_user_name():
    """
    @summary: 获取流水线启动人
    """
    return params.get("pipeline.start.user.name", None)


def get_workspace():
    """
    @summary: 获取工作空间
    """
    return params.get("bkWorkspace", None)


def set_output(output):
    """
    @summary: 设置输出
    """
    setOutput = SetOutput()
    setOutput.set_output(output)


if __name__ == "__main__":
    pass
