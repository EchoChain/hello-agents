import re

class TestParser:
    def _parse_action(self, action_text: str):
        """解析Action字符串，提取工具名称和输入。
        """
        # 清理反引号和多余空格
        action_text = action_text.strip().strip('`')
        match = re.match(r"(\w+)\[(.*)\]", action_text, re.DOTALL)
        return (match.group(1), match.group(2)) if match else (None, None)

# 测试
parser = TestParser()
test_cases = [
    '`Search[华为最新款手机 2024]`',
    'Search[华为最新款手机 2024]',
    '`Search[test]`',
    'Search[test input with spaces]',
]

for test in test_cases:
    tool_name, tool_input = parser._parse_action(test)
    print(f"输入: {test}")
    print(f"  工具名: {tool_name}, 参数: {tool_input}\n")

