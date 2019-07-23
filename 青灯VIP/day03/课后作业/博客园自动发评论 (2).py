'''
功能：实现博客园：https://www.cnblogs.com/ 自动发评论
    分析：1、要实现这个功能，首先要在登录后才能操作
          2、找到发评论的接口，实现该功能
          3、发送博客的帖子：https://www.cnblogs.com/listenfwind/p/11079061.html
步骤：
    通过抓包工具得到：
    1、登录地址为：https://account.cnblogs.com/signin
        登录数据的发送接口为：https://account.cnblogs.com/Account/SignIn?returnurl=https%3A%2F%2Fhome.cnblogs.com
        form表单内容为：LoginName: nj96xcWn7SAPHmdkxKumcfnIChPSIt//fiDNDFSxEHuWCf2TNwJl3RP6c4YF1o+uOBA0T6EiC47htyHOFJs4MRSlOw1Rn51CGw22jRO8yvbBfdhOAseNJirvjBDdQ/pgVwQ5oEDX0bD3DzWo9W1makGs2O9wSnJ+xXD5lyhMN80=
                        Password: S1ZIcmMfQue0Uk9M0DqWaBi4r5rHKD4K0q8Q+uXg+vpAh/rFneZLsEXZNp51feaMbT6XkP0gMYJsG/hl1rSa37vARQoPDXpFMgnEvEIj3NjpDrJDNSeFIigN9IOaGmeNGIkPgaE3PRubso8JAxny53m8nguebQ0q8+mo7UURyGM=
                        PublicKey: MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCp0wHYbg/NOPO3nzMD3dndwS0MccuMeXCHgVlGOoYyFwLdS24Im2e7YyhB0wrUsyYf0/nhzCzBK8ZC9eCWqd0aHbdgOQT6CuFQBMjbyGYvlVYU2ZP7kG9Ft6YV6oc9ambuO7nPZh+bvXH0zDKfi02prknrScAKC0XhadTHT3Al0QIDAQAB
                        EnableCaptcha: true
                        __RequestVerificationToken: CfDJ8D8Q4oM3DPZMgpKI1MnYlrmkppZc6t-3dYN9E8uvEUUHx4IExxwVNT9r_adjNKXtgsBsvd0MdL4fno8ybc_i5qg2SHXWE5AheB1ouJQw6FEVXGdJ3n_78nQoznDEZKUAOpal2Y0JTY6GWrTKYGWUOMU
                        IsRemember: false
                        EnableCaptcha: false
                        isEncrypted: true
                        geetest_challenge: f0fbd4d52186edaf1431cafc079a93f8gx
                        geetest_validate: 7b645db3a32805a489842e44a5aa0d6a
                        geetest_seccode: 7b645db3a32805a489842e44a5aa0d6a|jordan
        以上内容中，geetest_challenge、geetest_validate、geetest_seccode目前无法获取，放弃这种自动登录方式
    2、因为上述有些内容无法获取，所以通过browsercookie方式进行登录，前提是先在浏览器中登录
    3、自动发评论的接口为：https://www.cnblogs.com/mvc/PostComment/Add.aspx，方式为post方式；
                发送的数据为：{blogApp: "java-chen-hao", postId: 11076176, body: "Java在大学
                    学过，现在又改学Python", parentCommentId: 0}，这个是json格式的数据，按照这个
                    格式，编写相关内容，然后发送请求，实现自动发送评论
'''

import time
import requests
import browsercookie


def send_msg(msg):
    send_msg_url = 'https://www.cnblogs.com/mvc/PostComment/Add.aspx'
    form_data = {
        'blogApp': 'listenfwind',
        'postId': '11079061',
        'body': msg,
        'parentCommentId': 0
    }
    cookiejar = browsercookie.chrome()
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    }
    return requests.post(send_msg_url, data=form_data, cookies=cookiejar, headers=headers)


if __name__ == '__main__':
    msg = input('请输入需要评论的内容:')
    res = send_msg(msg)
    if msg in res.text:
        print('发送成功')
    else:
        print('发送失败')

