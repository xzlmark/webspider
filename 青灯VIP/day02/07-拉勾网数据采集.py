'''
post请求中，query string parameters就是追加到URL后面的参数
form-data 中内容是隐藏的数据，不在网址中反映
post传递的是字典格式数据
content-type:application/x-www-form-urlencoded 表单类型,采用data传递数据
content-type:application/json    json格式传递数据，接受一个字典，也可以采用data=json.dumps()转换为字典

'''
import requests
url ='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
data = {
    'first':'false',
    'pn':4,
    'kd':'python'
}
headers ={
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '26',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'user_trace_token=20190620221751-e18d44b3-d69a-4375-9396-74d0209eb8c5; _ga=GA1.2.760622170.1561040279; LGUID=20190620221800-35ab5309-9366-11e9-b396-525400f775ce; _gid=GA1.2.1836750433.1561040319; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1561040278,1561123369; LGSID=20190621212251-ab7372ea-9427-11e9-a442-5254005c3644; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0QW9b0FNkUs0hv6kI00000cTH27C00000Vqeeo3.THL0oUhY1x60UWdBmy-bIy9EUyNxTAT0T1dbn1czmyPBnj0snHTkuy790ZRqnWKAfHDvPRParjmdrHT1fHR4fYRLPjPafWDvPWbdfWR0mHdL5iuVmv-b5HnzPjnknHfsrH6hTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8UA7MULR8mvqVQvk9UhwGUhTVTA7Muiqsmzq1uy7zmv68pZwVUjqdIAdxTvqdThP-5ydxmvuxmLKYgvF9pywdgLKWmMf0mLFW5HRdPWR4%26tpl%3Dtpl_11534_19968_16032%26l%3D1512575879%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3243114098_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D120%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3Duseragent%26inputT%3D3336%26bs%3Duseragent; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; JSESSIONID=ABAAABAAAGFABEF83589E217144312B80BFC348A21F6908; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=f15993b520bc414cb959554664966d84; X_HTTP_TOKEN=5da9ddcd269a89240833211651b60cf4108114d7b5; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1561123379; LGRID=20190621212301-b154d578-9427-11e9-b4c3-525400f775ce',
'Host': 'www.lagou.com',
'Origin': 'https://www.lagou.com',
'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
'X-Anit-Forge-Code': '0',
'X-Anit-Forge-Token': 'None',
'X-Requested-With': 'XMLHttpRequest',
}
res = requests.post(url,data=data,headers=headers)
print(res.text)
