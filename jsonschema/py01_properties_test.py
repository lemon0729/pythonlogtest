import jsonschema
# 导包

# 准备校验数据
schema = {
    "type": "object",
    "requirde": ["success", "code", "message", "data"],
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"pattern": "登录成功$"},

        "data": {
            "type": "object",
            "requirde": ["name", "age"],
            "properties": {
                "age": {"const": 20},
                "name": {"const": "lily"}
            }
        }
    }

}
# 准备测试数据
data = {
    "success": False,
    "code": 10000,
    "message": "xxx登录成功",
    "data": {
        "age": 20,
        "name": "lily"
    }
}

# 调用方法进行校验
resp = jsonschema.validate(instance=data, schema=schema)
print("结果：", resp)
