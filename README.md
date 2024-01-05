# 免费定时任务
原理：使用Github Action功能，运行python程序 实现无服务器的免费定时任务

### 视频教程

作者 **技术爬爬虾** 全网同名，转载请注明作者

## Part1 构建画爱心为可执行程序
构架Windows 可执行程序:
Fork本项目，Actions-->画爱心Windows版-->run work flow-->结束后查看结果
-->Artifacts-->下载love_heart

构架Ubuntu 可执行程序:
Fork本项目，Actions-->画爱心Ubuntu版-->run work flow-->结束后查看结果
-->Artifacts-->下载love_heart

## Part2 天气推送

### 申请公众号测试账户

使用微信扫码即可
https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

进入页面以后我们来获取到这四个值 
#### appID  appSecret openId template_id
![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/bdb27abd-39cb-4e77-9b89-299afabc7330)

想让谁收消息，谁就用微信扫二维码，然后出现在用户列表，获取微信号（openId）
 ![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/1327c6f5-5c92-4310-a10b-6f2956c1dd75)

新增测试模板获得  template_id（模板ID）
 ![image](https://github.com/tech-shrimp/FreeWechatPush/assets/154193368/ec689f4d-6c0b-44c4-915a-6fd7ada17028)

模板标题随便填，模板内容如下，可以根据需求自己定制

模板内容：
```copy
今天：{{date.DATA}} 
地区：{{region.DATA}} 
天气：{{weather.DATA}} 
气温：{{temp.DATA}} 
风向：{{wind_dir.DATA}} 
对你说的话：{{today_note.DATA}}
```

### 项目搭建 
Fork本项目，进入自己项目的Settings  ----> Secrets and variables ---> Actions --> New repository secret
配置好以下四个值

<img width="590" alt="image" src="https://github.com/tech-shrimp/GithubActionSample/assets/154193368/9e6b799d-9230-4d3e-8966-6c6f49e9b89f">



