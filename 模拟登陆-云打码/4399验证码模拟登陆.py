import time
from selenium import webdriver
from PIL import Image  # 截图，保存图片需要使用
from configparser import ConfigParser  # 读取配置文件需要使用
from ctypes import *  # 加载下面的.dll文件需要

# captchaId获取验证码ID，在验证码验证失败的情况下使用;其他变量是打码函数需要的参数
global captchaId
YDMApi = windll.LoadLibrary('yundamaAPI-x64')
appId = 1  # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appKey = b'22cc5376925e9387a23cf797cb9ba745'  # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
username = b'xzlmark'
password = b'zlhyysxf'


# 得到验证码
def getcode():
    print('\r\n>>>打码平台正在一键识别...')
    # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 1004
    # 分配30个字节存放识别结果
    result = c_char_p(b"                              ")
    # 识别超时时间 单位：秒
    timeout = 60
    # 验证码文件路径
    filename = b'a.png'  # 可以使用完整路径，但是要注意使用转义字符\\,这里不能用r
    # 一键识别函数，无需调用YDM_SetAppInfo和YDM_Login，适合脚本调用，captchaId获取验证码ID，在验证码验证失败的情况下使用
    captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    print("一键识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
    result = str(result.value, encoding='utf-8')  # 返回的结果是字节，需要转换成字符串
    return str(result)


def main():
    driver.get('http://4399.com')
    # 最大化窗口
    driver.maximize_window()
    """
    implicitly_wait():隐式等待。当使用了隐士等待执行测试的时候，如果 WebDriver没有在 DOM中找到元素，将继续等待，
    超出设定时间后则抛出找不到元素的异常，换句话说，当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间
    再查找 DOM，默认的时间是0。一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个
    正常响应的应用的测试变慢， 它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。 """
    driver.implicitly_wait(2)
    # 通过xpath进行查询，找到登录按钮然后点击
    driver.find_element_by_xpath('//*[@id="login_tologin"]').click()
    #  截取全屏，保存为图片
    driver.save_screenshot('dl_button.png')
    # 保存登录框图片
    save_pic('popup_login_frame', 'dl_button.png', 'b.png')

    # 将指正返回到iframe,这个一定要注意，然后找到用户名和密码框，并输入值
    driver.switch_to.frame('popup_login_frame')
    # 输入用户名  还有一个用户名  2038743521 2039851366  密码123456
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('2038743521')

    # 读取配置文件,密码保存在配置文件中
    target = ConfigParser()
    target.read('pwd.ini', encoding='utf-8')
    pwd = target.get('pwd', 'password')
    # 输入密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(pwd)

    # 找到验证码的位置,如果没有要求输入验证码，则直接登录
    if save_pic('captcha', 'b.png', 'a.png') == 1:
        code = getcode()  # 得到验证码
        time.sleep(1)
        # 输入验证码,并点击登录按钮
        driver.find_element_by_xpath('//*[@id="inputCaptcha"]').send_keys(code)
        driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[6]/input').click()
        time.sleep(1)
        # 判断验证码是否错误，如果错误，则将信息反馈给打码平台，如果没有错误，则登录成功
        try:
            res = driver.find_element_by_id('Msg').text
            if res == '验证码错误':
                res = YDMApi.YDM_EasyReport(username, password, appId, appKey, captchaId, False)
                print('云打码错误，反馈结果：' + res)
        except:
            print('登录成功！')
    else:
        driver.find_element_by_xpath('//*[@id="login_form"]/fieldset/div[5]/input').click()
        print('登陆成功！')


# xpath_id:是传入的html参数中的id值；open_file:要打开的图片文件；save_file:图片保存再什么地方，需要指定文件名
def save_pic(xpath_id, open_file, save_file):
    try:
        element = driver.find_element_by_id(xpath_id)  # 选中表单iframe位置,这就相当于选中了这个iframe框，有大小，宽度
        f_left = element.location['x']  # 返回的是起始点的x坐标
        f_top = element.location['y']  # 返回的是起始点的y坐标
        f_right = element.location['x'] + element.size['width']  # 返回的是iframe框右下角点的x坐标
        f_below = element.location['y'] + element.size['height']  # 返回的是iframe框右下角点的y坐标
        image = Image.open(open_file)  # 打开图片文件
        image = image.crop((f_left, f_top, f_right, f_below))  # 用指定的坐标进行截取，注意参数是元组类型
        image.save(save_file)  # 保存文件
        return 1  # 如果上面执行都没有问题，则返回1，表示成功执行
    except Exception as ex:
        print('异常信息：%s' % ex)
        return 0


if __name__ == '__main__':
    # 启动浏览器
    driver = webdriver.Chrome()
    main()
