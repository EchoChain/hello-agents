# test_simple_agent.py
from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM, ToolRegistry
from hello_agents.tools import CalculatorTool
from my_simple_agent import MySimpleAgent

# 加载环境变量
load_dotenv()

# 创建LLM实例
llm = HelloAgentsLLM()

# 测试1：基础对话Agent（无工具）
print("=== 测试1：基础对话 ===")
basic_agent = MySimpleAgent(
    name="基础助手",
    llm=llm,
    system_prompt="你是一个友好的AI助手，请用简洁明了的方式回答问题。"
)

response1 = basic_agent.run("你好，请介绍一下自己")
print(f"基础对话响应: {response1}\n")

# 测试2：带工具的Agent
print("=== 测试2：工具增强对话 ===")
tool_registry = ToolRegistry()
calculator = CalculatorTool()
tool_registry.register_tool(calculator)

enhanced_agent = MySimpleAgent(
    name="增强助手",
    llm=llm,
    system_prompt="你是一个智能助手，可以使用工具来帮助用户。",
    tool_registry=tool_registry,
    enable_tool_calling=True
)

response2 = enhanced_agent.run("请帮我计算 15 * 8 + 32")
print(f"工具增强响应: {response2}\n")

# 测试3：流式响应
print("=== 测试3：流式响应 ===")
print("流式响应: ", end="")
for chunk in basic_agent.stream_run("请解释什么是人工智能"):
    pass  # 内容已在stream_run中实时打印

# 测试4：动态添加工具
print("\n=== 测试4：动态工具管理 ===")
print(f"添加工具前: {basic_agent.has_tools()}")
basic_agent.add_tool(calculator)
print(f"添加工具后: {basic_agent.has_tools()}")
print(f"可用工具: {basic_agent.list_tools()}")

# 查看对话历史
print(f"\n对话历史: {len(basic_agent.get_history())} 条消息")
for i, history in enumerate(basic_agent.get_history()):
    print(f"[{i+1}]: {history}")

'''
对话历史: 4 条消息
[1]: [user] 你好，请介绍一下自己
[2]: [assistant] 你好！我是一个友好的AI助手。

我的目标是协助你解决问题，包括回答疑问、提供信息、进行文字创作或翻译等。

请问有什么我可以帮你的吗？
[3]: [user] 请解释什么是人工智能
[4]: [assistant] 简单来说，**人工智能（Artificial Intelligence，简称 AI）**就是让计算机或机器表现出类似人类智慧的技术。

你可以把它理解为：**教机器像人一样去“看、听、说、想和做”。**

它主要包含以下几个核心能力：

1.  **学习：** 通过分析大量数据，自动掌握规律（例如：看了几万张猫的照片后，学会识别猫）。
2.  **推理：** 根据已知信息做出判断或决策。
3.  **感知：** 能够识别图像（计算机视觉）和理解语言（自然语言处理）。

**常见的AI应用场景：**
*   **日常生活中的AI：** 手机面部解锁、智能助手（如Siri）、购物软件的个性化推荐。
*   **高阶AI：** 自动驾驶汽车、像ChatGPT这样的对话机器人、医疗诊断辅助。

总而言之，AI就是**利用计算机科学模拟人类智能，帮助人类更高效地解决问题**。

'''