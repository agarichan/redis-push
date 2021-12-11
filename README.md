# Redis を通して命令するためのプロトコル

## Logger

```python
import asyncio
from redis_push import Logger

logger = Logger(channel="test", channel="error-test")

async main():

    try:
        1 / 0
    except Exception:
        await logger.error(origin="sample")

    await logger.info(message="*テストメッセージ*")

asyncio.run(main())
```
