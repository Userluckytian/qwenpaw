# qwenpaw-keepalive

QwenPaw 云沙箱保活：每 6 小时向 AgentScope Platform 上报一次心跳，防止 48 小时无操作自动关机。零 LLM token 消耗。

## 部署

1. Settings → Secrets and variables → Actions，添加：
   - `QP1_ACCOUNT` / `QP1_PASSWORD`（你的平台账号密码）
   - 多台沙箱时再加 `QP2_ACCOUNT` / `QP2_PASSWORD`，并取消 workflow 中 `acc2` 的注释
2. Actions 页手动 Run workflow 验证，之后全自动。

## 说明

- 每次运行自动提交时间戳文件 `.last-run`，防止仓库因不活跃被 GitHub 停用定时任务
- 任务失败标红并邮件通知，红灯同时意味着某台沙箱可能已被关机
- 凭证一律放 Actions Secrets，日志自动脱敏，不要硬编码进脚本
