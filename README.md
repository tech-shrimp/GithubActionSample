# Github Action功能样例

原理：使用Github Action功能，运行python程序，实现无服务器的免费任务，比如天气推送，薅羊毛，签到

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

### 项目配置 
Fork本项目
进入自己项目的Settings  ----> Secrets and variables ---> Actions --> New repository secret
配置好以下四个值（见上文）

<img width="590" alt="image" src="https://github.com/tech-shrimp/GithubActionSample/assets/154193368/9e6b799d-9230-4d3e-8966-6c6f49e9b89f">

进入自己项目的Action  ----> 天气预报推送 ---> weather_report.yml --> 修改cron表达式的执行时间
<img width="503" alt="image" src="https://github.com/tech-shrimp/GithubActionSample/assets/154193368/badcc0fa-def5-428f-9238-fa6b549baefc">

## Part3 签到薅羊毛
Fork本项目
网页上打开：www.jd.com/ 再按F12打开控制台，再点击切换模式，切换到手机模式，刷新一下页面。如图所示
![image](https://github.com/tech-shrimp/GithubActionSample/assets/154193368/44d01795-8c1e-4a56-bb0e-a36f74062dcb)
在网络->m.jd.com找到Cookie

<img width="935" alt="image" src="https://github.com/tech-shrimp/GithubActionSample/assets/154193368/97139add-a410-4e73-82d3-055c8136ed57">

将其填入  Settings  ----> Secrets and variables ---> Actions --> New repository secret
<img width="685" alt="image" src="https://github.com/tech-shrimp/GithubActionSample/assets/154193368/e28ee156-642a-4c25-94ff-d42af072aa15">

进入自己项目的Action  ----> 签到薅羊毛 ---> daily_sign.yml --> 修改cron表达式的执行时间
