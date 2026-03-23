import re

# 测试输入
action_text = '`Search[华为最新款手机 2024]`'
print(f"输入: {action_text}")
print(f"输入首字符: {repr(action_text[0])}")

# 当前正则
match = re.match(r"(\w+)\[(.*)\]", action_text)
print(f"\n使用 re.match: {match}")

# 使用 re.search
match = re.search(r"(\w+)\[(.*)\]", action_text)
print(f"使用 re.search: {match}")
if match:
    print(f"工具名: {match.group(1)}, 输入: {match.group(2)}")

# 清理反引号后
action_text_clean = action_text.strip().strip('`')
print(f"\n清理后: {action_text_clean}")
match = re.match(r"(\w+)\[(.*)\]", action_text_clean)
print(f"清理后使用 re.match: {match}")
if match:
    print(f"工具名: {match.group(1)}, 输入: {match.group(2)}")

