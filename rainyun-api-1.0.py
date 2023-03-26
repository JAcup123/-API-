#导入库
import requests
import json
api_key_now=None
#Api信息
api_key_now = input("请输入新的用户AIP密钥")
#请求用户信息
url = "https://api.v2.rainyun.com/user/"
payload={}
headers_yh = {
   'X-Api-Key': api_key_now
}
res_points = requests.request("GET", url, headers=headers_yh, data=payload)
zh_json = res_points.json()
##print(zh_json)
points = zh_json['data']['Points']
ID = zh_json['data']['ID']
name = zh_json['data']['Name']
print(f'雨云ID：{ID}',f'雨云用户名{name}')
print(f'账户剩余积分：{points}','约等于',points/2000,'元')
print('==============================')
#签到部分
url_lqjf = 'https://api.v2.rainyun.com/user/reward/tasks'
headers_lqjf = {
    'content-type':"application/json",
    'X-Api-Key':api_key_now
    }
body_lqjf = {
    "task_name" : '每日签到',
    "verifyCode" : ''
    }
res_lqjf = requests.request("POST", url_lqjf, headers=headers_lqjf, data = json.dumps(body_lqjf))
if res_lqjf.text == points + 300:
    print(f'签到成功，当前剩余积分：{points + 300}')
else:
    print(f'签到失败，返回值：{res_lqjf.text}')
print('==============================')
#自动申请提现部分
url_zdtx = 'https://api.v2.rainyun.com/user/reward/withdraw'
headers_zdtx = {
    'content-type':"application/json",
    'X-Api-Key':api_key_now
    }
body_zdtx = {
    "points": points,
    "target": api_key_now
    }
if points + 300 >= 60000:
    res_zdtx = requests.request("POST", url_zdtx, headers=headers_zdtx, data = json.dumps(body_zdtx))
    print(f'已发起提现')
else:
    print(f'提现发起失败，当前积分：{points}')
print('==============================')
#提现列表部分
#输入你的options
options='{"columnFilters":{},"sort":[],"page":1,"perPage":20}'
url_txsq = 'https://api.v2.rainyun.com/user/reward/withdraw?options='+options
headers_txsq = {
    'content-type':"application/json",
    'X-Api-Key':api_key_now
    }
res_txsq = requests.request("GET", url_txsq, headers=headers_txsq)
txsq_json = res_txsq.json()
tmp_1 = txsq_json['data']
tmp_2 = tmp_1['Records']
tmp_3 = tmp_2[0]
if tmp_3["status"] == 'finished':
    print('上一次提现记录：')
    print(f'提现ID：{tmp_3["id"]}')
    print(f'提现账户：{tmp_3["account"]}')
    print(f'提现方式：{tmp_3["target"]}')
    print(f'提现积分：{tmp_3["points"]}')
    print(f'提现金额：{tmp_3["money"]}')
    print(f'提现状态：{tmp_3["status"]}')
else:
    print('本次提现记录：')
    print(f'提现ID：{tmp_3["id"]}')
    print(f'提现账户：{tmp_3["account"]}')
    print(f'提现方式：{tmp_3["target"]}')
    print(f'提现积分：{tmp_3["points"]}')
    print(f'提现金额：{tmp_3["money"]}')
    print(f'提现状态：{tmp_3["status"]}')
points=None
if input('是否保留API密钥信息？yes or else:') == 'yes':
    print('别想了，这个功能还没做出来')
else:
    print=None
    api_key_now=None
    print('您的API密钥已清除')