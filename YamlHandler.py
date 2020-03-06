import yaml

class YamlHandler:
    def __init__(self, path):
        self.path = path  # 文件路径

    # 获取yaml文件中的数据
    def get_data(self, key=None):
        with open(self.path, 'rb') as y:
            cont = y.read()  # 获取yaml文件中的所有信息
        yaml.warnings({'YAMLLoadWarning': False})  # 禁用加载器warnings报警
        cf = yaml.load(cont)  # 将bytes格式转成dict格式
        y.close()  # 关闭文件
        if key is None:
            return cf  # 返回所有数据
        else:
            return cf.get(key)  # 获取键为param的值

    def write_data(self,message):
        with open(self.path, "w", encoding="utf-8") as f:
            # 注：此模式为追加模式,若想直接重写则将open函数中的模式'a+'改为'w'
            yaml.dump(message, f)
        f.close()
