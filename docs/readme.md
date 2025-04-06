### 一、说明
    1. 使用pytest框架结合requests库实现接口自动化测试
    2. 使用allure插件生成测试报告 
### 二、结构
- base 存放基类，基础方法实现
- libs 存放业务类，继承基类实现业务操作
- tests 存放测试用例实现
- utils 存放工具类及方法
- out 存放输出文件，报告和日志等
- configs 存放配置文件
- testCases 存放测试用例文件
- docs 存放说明文档、接口文档等文档
- dependentTools 存放依赖工具，如allure插件