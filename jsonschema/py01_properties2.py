import jsonschema

# 导包

# 准备校验数据


schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "address": {"type": "null"},
        "data":{
            "type": "object",
            "properties":{
                            "name":{"type": "string"},
                            "age":{"type": "integer"},
                            "height":{"type": "number"}
            }
                }
    }
}
# 准备测试数据
data = {
    "success": True,
    "code": 10000,
    "message": "操作成功",
    "address": None,
    "data": {
        "name":"tom",
        "age":18,
        "height":1.78
    }
}

# 调用方法进行校验
resp = jsonschema.validate(instance=data, schema=schema)
print("结果：", resp)
