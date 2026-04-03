"""简单Agent实现 - 基于OpenAI原生API"""

from typing import Optional, Iterator

from ..core.agent import Agent
from ..core.llm import HelloAgentsLLM
from ..core.config import Config
from ..core.message import Message

class SimpleAgent(Agent):
    """简单的对话Agent"""
    
    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        system_prompt: Optional[str] = None,
        config: Optional[Config] = None
    ):
        super().__init__(name, llm, system_prompt, config)
    
    def run(self, input_text: str, **kwargs) -> str:
        """
        运行简单Agent
        
        Args:
            input_text: 用户输入
            **kwargs: 其他参数
            
        Returns:
            Agent响应
        """
        # 构建消息列表
        messages = []
        
        # 添加系统消息
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        
        # 添加历史消息
        for msg in self._history:
            messages.append({"role": msg.role, "content": msg.content})
        
        # 添加当前用户消息
        messages.append({"role": "user", "content": input_text})
        
        # 调用LLM
        response = self.llm.invoke(messages, **kwargs)
        
        # 保存到历史记录
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(response, "assistant"))
        
        return response
    
    def stream_run(self, input_text: str, **kwargs):
        """
        流式运行Agent
        
        Args:
            input_text: 用户输入
            **kwargs: 其他参数
            
        Yields:
            Agent响应片段
        """
        # 构建消息列表
        messages = []
        
        if self.system_prompt:
            messages.append({"role": "system", "content": self.system_prompt})
        
        for msg in self._history:
            messages.append({"role": msg.role, "content": msg.content})
        
        messages.append({"role": "user", "content": input_text})

        """
                可以这样理解：
                self.llm.stream_invoke(...)
                会不断产生文本片段（chunk）。
                每来一个
                chunk：
                先
                full_response += chunk（在内部拼接完整答案）
                再
                yield chunk（立刻把这个片段发给外部）
                外部拿到片段后可以马上显示（这就是“流式输出”）。
                下次循环时，函数从
                yield 后面继续跑，不会从头来。

                yield 和
                return 的区别（关键）
                return x：函数直接结束，只返回一次。
                yield x：函数变成“生成器”，可以多次产出，每次产出后暂停，再继续。
                所以你的
                stream_run
                不是一次性返回完整字符串，而是“边生成边吐出”。"""

        # 流式调用LLM
        full_response = ""
        for chunk in self.llm.stream_invoke(messages, **kwargs):
            full_response += chunk
            yield chunk

        # 保存完整对话到历史记录
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(full_response, "assistant"))





        
