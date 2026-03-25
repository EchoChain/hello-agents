"""配置管理"""

import os
from typing import Optional, Dict, Any
from pydantic import BaseModel

class Config(BaseModel):
    """HelloAgents配置类"""

    """
    Pydantic 自动处理初始化
    # ✅ 可以这样创建实例
        config = Config(default_model="gpt-4", temperature=0.9)
    # ✅ 也可以这样（使用默认值）
    config = Config()
    # ✅ 可以从字典创建
    config = Config(**data_dict)
    简而言之：Pydantic
    用类属性 + 类型注解替代了手工
    __init__，提供了自动初始化、验证、序列化等功能，代码更简洁，功能更强大。
    """
    
    # LLM配置
    default_model: str = "gpt-3.5-turbo"
    default_provider: str = "openai"
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    
    # 系统配置
    debug: bool = False
    log_level: str = "INFO"
    
    # 其他配置
    max_history_length: int = 100
    
    @classmethod
    def from_env(cls) -> "Config":
        """从环境变量创建配置"""
        return cls(
            debug=os.getenv("DEBUG", "false").lower() == "true",
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            temperature=float(os.getenv("TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("MAX_TOKENS")) if os.getenv("MAX_TOKENS") else None,
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        return self.dict()
