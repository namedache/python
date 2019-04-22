from logging import exception
import logging
from selenium import webdriver
import time
import re

#全局变量
driver = webdriver.Chrome("/Users/zhoukun/Downloads/chromedriver")

# 登陆微博
# param usernam,password
def loginWeibo(username, password):

    driver.get('https://passport.weibo.cn/signin/login')
    time.sleep(3)

    driver.find_element_by_id("loginName").send_keys(username)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_id("loginAction").click()


# 获得用户资料
# param userId
def visitUserInfo(userId):
    driver.get('http://weibo.cn/' + userId)

    logging.debug('********************')
    logging.debug('用户资料')

    # 1.用户id
    logging.debug('用户id:' + userId)

    # 2.用户昵称
    strName = driver.find_element_by_xpath("//div[@class='ut']")
    strlist = strName.text.split(' ')
    nickname = strlist[0]
    logging.debug('昵称:' + nickname)

    # 3.微博数、粉丝数、关注数
    strCnt = driver.find_element_by_xpath("//div[@class='tip2']")
    pattern = r"\d+\.?\d*"  # 匹配数字，包含整数和小数
    cntArr = re.findall(pattern, strCnt.text)
    logging.debug(strCnt.text)
    logging.debug("微博数：" + str(cntArr[0]))
    logging.debug("关注数：" + str(cntArr[1]))
    logging.debug("粉丝数：" + str(cntArr[2]))

    logging.debug('\n********************')
    # 4.将用户信息写到文件里
    with open("userinfo.txt", "w", encoding="UTF-8") as file:
        file.write("用户ID：" + userId + '\r\n')
        file.write("昵称：" + nickname + '\r\n')
        file.write("微博数：" + str(cntArr[0]) + '\r\n')
        file.write("关注数：" + str(cntArr[1]) + '\r\n')
        file.write("粉丝数：" + str(cntArr[2]) + '\r\n')


# 获得用户发表微博的数据
# param userId
def visitWeiboContent(userId):
    pageList = driver.find_element_by_xpath("//div[@class='pa']")
    logging.debug(pageList.text)
    pattern = r"\d+\d*"  # 匹配数字，只包含整数
    pageArr = re.findall(pattern, pageList.text)
    totalPages = pageArr[1]  # 总共有多少页微博
    logging.debug(totalPages)

    pageNum = 1  # 第几页
    numInCurPage = 1  # 当前页的第几条微博内容
    curNum = 0  # 全部微博中的第几条微博
    contentPath = "//div[@class='c'][{0}]"
    # while(pageNum <= 3):
    while (pageNum <= 10):
        try:
            contentUrl = "http://weibo.cn/" + userId + "?page=" + str(pageNum)
            driver.get(contentUrl)
            content = driver.find_element_by_xpath(contentPath.format(numInCurPage)).text
            # print("\n" + content)                  # 微博内容，包含原创和转发
            if "设置:皮肤.图片.条数.隐私" not in content:
                numInCurPage += 1
                curNum += 1
                with open("weibocontent.txt", "a", encoding="UTF-8") as file:
                    file.write(str(curNum) + '\r\n' + content + '\r\n\r\n')
            else:
                pageNum += 1  # 抓取新一页的内容
                numInCurPage = 1  # 每一页都是从第1条开始抓
                time.sleep(30)  # 要隔25秒，否则会被封
        except exception as e:
            logging.debug("curNum:" + curNum)
            logging.debug(e)
        finally:
            pass
    logging.debug("Load weibo content finished!")
    return True


def topmblog():
    driver.get('http://weibo.cn/pub/topmblog')
    cont = driver.find_element_by_xpath("//div[@class='ctt']")
    pass


# 主函数调用
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s\t%(levelname)s\t%(message)s")
