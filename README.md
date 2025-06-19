<div align="center">
  <a href="https://github.com/miaowuawa/MyGO" target="_blank">
<img src="https://img.picui.cn/free/2025/06/19/6852ee5eb6324.jpg" alt="mygo.jpg" title="mygo.jpg" />  
  </a>
  <h1 id="koishi">MyGO</h1>

<p>
  <!-- GitHub Downloads -->
  <a href="https://github.com/miaowuawa/MyGO/releases">
    <img src="https://img.shields.io/github/downloads/miaowuawa/MyGO/total" alt="GitHub all releases">
  </a>
  <!-- GitHub Release Version -->
  <a href="https://github.com/miaowuawa/MyGO/releases">
    <img src="https://img.shields.io/github/v/release/miaowuawa/MyGO" alt="GitHub release (with filter)">
  </a>
  <!-- GitHub Issues -->
  <a href="https://github.com/miaowuawa/MyGO/issues">
    <img src="https://img.shields.io/github/issues/miaowuawa/MyGO" alt="GitHub issues">
  </a>
  <!-- GitHub Stars -->
  <a href="https://github.com/miaowuawa/MyGO/stargazers">
    <img src="https://img.shields.io/github/stars/miaowuawa/MyGO" alt="GitHub Repo stars">
  </a>
</p>

起源于MikuMifa的biliTickerBuy，让会员购抢票不再迷路
</div>

<br>
<b>在此通知移除前，此项目仅供技术分析，您也不应该在此时将MyGO作为正式环境使用的抢票软件。</b>
<br>
<b>在此感谢原作者MikuMifa为BW而做出的一切努力！这么多年来，你辛苦了！</b>

<br>
<br>

## 注意事项

本项目没有云控，但我们仍然不允许您使用此项目进行盈利性/商业化批量抢票。除非您承认，您失去了父母。
为防止黄牛滥用和自动化脚本泛滥，本项目暂不提供ctoken/ticket生成的核心代码实现。我们理解这可能会给正常用户带来一些不便，但这一措施能有效限制大规模自动化抢票行为。


### 如何获取ctoken/ticket？

您有以下两种方式获取ctoken/ticket：

#### 1. 自行逆向实现API

您需要自行逆向分析并实现以下API接口：

**生成ctoken接口**:
```
POST http://localhost:8080/generate
Content-Type: application/json

请求体:
{
  "screen_width": 1920,
  "screen_height": 1080
}

响应:
{
  "ctkid": "xXxXxXxXxXxXxXxXxXxX",
  "ctoken": "something"
}
```

**ctoken刷新接口**:
```
GET http://localhost:8080/get/xXxXxXxXxXxXxXxXxXxX

响应:
{
  "ctoken": "something"
}
```

** ticket获取接口 **

```
POST http://localhost:8080/getticket
Content-Type: application/json

请求体:
{
  "user_agent": string,        // 必填，用户代理字符串
  "cookies": [                 // 必填，Cookie数组
    {
      "name": string,           // Cookie名称
      "value": string,          // Cookie值
      "path": string,           // 可选，Cookie路径
      "domain": string,         // 可选，Cookie域名
      "expires": string         // 可选，过期时间
    }
  ],
  "ctkid": string              // 可选，CToken会话ID（非必须）
}

响应:
{
  "ticket": "获取到的B站Ticket",
  "error": string              // 错误时返回
}

```


#### 2. 通过官方API服务

我们提供稳定的官方API服务：
- Telegram联系: @miaowuawa
- 特点: 低延迟、高并发、免费使用
- 要求: 需要提供一些基本信息以验证身份

### 使用建议

1. 对于技术用户: 建议自行逆向实现，这样可以获得最佳性能和灵活性
2. 对于普通用户: 推荐使用官方API服务，简单可靠
3. 请合理使用，避免频繁请求

我们保留根据使用情况调整API访问策略的权利，以确保服务的公平性和可持续性。


## 💻 快速安装

[下载链接](https://github.com/miaowuawa/MyGO/releases) 

## 👀 使用说明书
没写好

## ❗ 项目问题

程序使用问题： [点此链接前往discussions](https://github.com/mikumifa/biliTickerBuy/discussions)

反馈程序BUG或者提新功能建议： [点此链接向项目提出反馈BUG](https://github.com/mikumifa/biliTickerBuy/issues/new/choose)



## 🤩 项目贡献者
### 前项目贡献者（BiliTickerBuy）
<a href="https://github.com/mikumifa/biliTickerBuy/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mikumifa/biliTickerBuy&preview=true&max=&columns=" />
</a>
<br /><br />

### 本项目贡献者（MyGO）
<a href="https://github.com/miaowuawa/MyGO/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=miaowuawa/MyGO&preview=true&max=&columns=" />
</a>
<br /><br />

## ⭐️ Star History

### 前项目History（BiliTickerBuy）
[![Star History Chart](https://api.star-history.com/svg?repos=mikumifa/biliTickerBuy&type=Date)](https://www.star-history.com/#mikumifa/biliTickerBuy&Date)

### 本项目History（BiliTickerBuy）
[![Star History Chart](https://api.star-history.com/svg?repos=miaowuawa/MyGO&type=Date)](https://www.star-history.com/#miaowuawa/MyGO&Date)

## 📩 免责声明

详见[MIT License](./LICENSE)。
** 黄牛自重。 ** 
《治安管理处罚法》规定，伪造、变造、倒卖车票、船票、航空客票、文艺演出票、体育比赛入场券或其他有价票证、凭证的，处十日以上十五日以下拘留，可以并处一千元以下罚款；情节较轻的，处五日以上十日以下拘留，可以并处五百元以下罚款。
切勿进行盈利，所造成的后果与本人无关。

