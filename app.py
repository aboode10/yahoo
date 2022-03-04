import requests
from flask import *
from user_agent import *
app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"]= True
app.config["JSON_AS_ACSII"] = False
@app.route("/")
def q():
 return jsonify(check=False, email=" ", Telegram="@JJJJzJJJ") 
@app.route("/check/yahoo/JJJJzJJJ/")
def f():
	eml = request.args.get("email")
	email=eml.replace('@yahoo.com','')
	url = 'https://login.yahoo.com/account/module/create?validateField=yid'
	headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '1410',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'B=ab7s1s1h1vf9n&b=3&s=dv; GUC=AQEBAQFiIQ5iKUIeZARf; A1=d=AQABBDe9H2ICEIEN_un3y5YEqNt6JeCBn6UFEgEBAQEOIWIpYgAAAAAA_eMAAAcIN70fYuCBn6U&S=AQAAAvPvi2S1DSi8VlpzULwv0oU; A3=d=AQABBDe9H2ICEIEN_un3y5YEqNt6JeCBn6UFEgEBAQEOIWIpYgAAAAAA_eMAAAcIN70fYuCBn6U&S=AQAAAvPvi2S1DSi8VlpzULwv0oU; A1S=d=AQABBDe9H2ICEIEN_un3y5YEqNt6JeCBn6UFEgEBAQEOIWIpYgAAAAAA_eMAAAcIN70fYuCBn6U&S=AQAAAvPvi2S1DSi8VlpzULwv0oU&j=WORLD; AS=v=1&s=fwEznEuF&d=A6221dc06|iuo_iTH.2ULLeNqk_uq6uGoc8ZaeE3ns3pBo5vY6yr3rI8tL_T5Dve1879VzJWNoF3lSPoO5q9kEjtYjSBxHIxWYW.geRrU6Yg.wf3.JdLCFc6Fsh6fjdIjUxSOl21gQVsYDCYiR.JKT2Do3NrQjNrk4vDGq32wOEuELn2LHpIahtuXxL8GC.f0YzWuRGs.R5e9UXtvk3bqiWhPyahkwfA9gJglppyYNAKMcwfEbrbaVIWoLNfRz.T361_vErnrbpvM6_HQ1_.X4.M4YOdg49o62EmvwQp0rzswiQExg3B6ZkhByjMdzlbdpCBHdowK66W6BkQqQvatmQZfoWQv4traUUyHzCO70e4Yk.qukntkVQq_CURcE8qlRivLIC5rng4Tm6_i_KQBDVECOjbGXptwckZegFDNL3kiU.eL0AuumehuCiQyEZwWAMseKde1Jwytw5Yv_M3LFPVCtmi.6lcDJfnyOkncSRLP4HcowNjrMn4MC3dZ1EfzZL1_dzBWtcdo2r2cFxsWjUvt7t7R8OgAOwQABzhQZTXF45z_KrDhSQM33_AFiyMXo0LN3NRWdCZyHQi1fL7jBt4zDUsI3GLkpKlFk8jE_nzq668BrzFb0L7HocIqO3ueEk9IjjhVBkeIL5hQrF6LaBuyJNdAs7KmcIcWUc7Ly3GweDmdqfvrM23yHU.Xf8sz0OBwGonCDH36R0dX5CJVHwrsDMgRFjstOUpIyzFMLnmRjcOuvt_gevXI39y8r15qSYCRCvK.wcW9Azq.BdNWwC72W87AvF1xlwYFc1wnSXUXuwBViSOlqkGnwsnxqhOWvDgTi5515VIvu1Bq43cPYiCsdclI.p8BuGpIOZw55XuvqnUMq_FfZkhh0r512cK92YJJMDTCIkwgjlqgb1tsYck3t0Ccwdj6neE6IcZLj8wAYXdhPQStla9PeAKWaM3O8hlIsnEZiM.Mw2pNo.JOniA2U95zckzixp.k3u6l2kEQuyBCvPA--~A|B6221dc07|82ufE5j.2So5EjvcXL8Wi4ZE323Klpe4uENdd9f0Yoz.MN06wz45GdyYY0gfzTfwqLq036utOhyu08QTbIuwnts8XhDSBNF2tiz74pnALW43LFAA09jeNJwAjwUSI8ayF7eMccNvulMwRSM61mvlwJ.p.bu1P7_c2aVC.SuNyIbj_m6H9P5pJg0xSeU_Ol6WNxIowmYd34tUzrrxthEMnqE5DdNjELPVZZ8Tl0hjoKHY7.fzvIjNRTPosp.x6s2pX8IzCDUjMfqbJAJmaSKfYaj0n9uSa8lUIdDse39hiMpzpFAENFuL9mTEE2MChOh0qhQHo8zoeSy.qp4b.XeeaNfogoYn9cw9QOhOsWuy.QsMrEz2JO0z2539bQbHrrTJrLYeUQp0LuJ.jbX9HzkKjpq68w7OPOJYf3mTN80tS2MjdJLI56lZnVSPXyt2PT6oZRn5s4zsomVI0SYR5AJhUcKwlUQwj7b7kIwgNoCfxyDCID8veXh9JtNAEKwcXsRFxVqEYrwo_rYAvloFVuysQXu4ilbcnzViV4j9.GxE4D85_bculnX9O9Wf.bnsL1HjiE2AyU1Fo3_vTYlpvcEzdAMWVZZS_vJtsEC_CcVFMxlHo7Bcl4ZPdTuZ0WlE3nl0oNS0JWzx5xH5QjPFeJwNtg12pgj2OleOFqgZJJnK5WbLwuhm.vobp6TdheTwHb7e43Zx2FeMm5hquib_LJ3ce2yoTJmdxFFc8psUHbtwjUSUPQB_vYuZdrYoo8Lg_ZnIVUzD3efY4HrtFBhg7egk2v5Ii43rLGSm7R0Ps.unTv4ET1cmkAOTvbhy94qU~A|C6221dc2c|UnQmArz.2SpSHqQNuaUh_kXjNNsDfK0WAPE8ajwQkQx6WvLBUXQTwkEdHDM5xDN4Zvrg14pVUdSOI07yl3UNCbkO2kslVk.Q76p8AMRdyGBg0uxVhawdEjqz6rQD6ySAossMILrxg_78jZVXMvA0.yhgM9Qcg7PqhlFHlIxBCxdfb9fcaHlEtQvpBVOBeaqZ_A7iKtQ_sX9dy4q9exKEavXL7tlgeqhG1XkowANzK.0BSpPHWh.IBen9lOJwAHVZz5D9ikXaf5vu5kYD.tpZSCVrlnyaddxxtGZL.Hfty7gguKgJ2z_7dvwX50zLrmTyPqne4nig0N5ZklVqiK1A8KQhETnTv3zu5tsd4xVcrh4m_nxyx94DWGPmxr.e.XTsqgXxOQ.GiB6TirpdJmi.9WdTN8LNqN7o3SPl8R2eU360ZUytOli63hDOVneTxxdU.xZbX05Uau79tPLzpqIZB.iC.ahavpkXWePnBlMxlFO5p2dxw_YHCtpWicgQZ7C1tCMYA2IxjSyZmq0c8Z8lbt2XM7fteslEaR48AVW0.sR1di6jhdnT5e79pf2LPrckXmVToHasNbm8KVOAWi4uYR_hVTcGzRGAkLpMRCXd0q99dLI33Y2Y4eJC_3nSqgKKIL6xf2.hV4RO89MnELKxR3Hmam3CMgVOHG1HKAnAFwHaOYJRXWPKmvujzYnFsbGsVvactzZu1H9UkWPTIAe4qtk3DOQpG2Kl_2gd.XDwPtoxH4m6d_0V9FrBqWe4gQe5P3ZdHBadQ70gflhgGk1gAoWTREJmR9zuntw4OKb4u9OKG9tejF9tdX0XOC.Omx.qYsLPCn7vgKYdFgmBZFWdWBw4ztjnDBlm5Wv_etdxwtyUV7GYOxYpPRtnnHfke7w677km7m0ULKqam7r1ax9YL18JdACrsTyBLl10AFY9LgLZQaCOTKabQa_irW4S_bcC4DZc8EbedlY-~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https://mail.yahoo.com/d',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?1',
    'Sec-Fetch-Dest': '"Android"',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'}
	data = {
    'browser-fp-data': '{"language":"ar-EG","colorDepth":24,"deviceMemory":4,"pixelRatio":2,"hardwareConcurrency":8,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Linux aarch64","doNotTrack":"unknown","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Qualcomm~Adreno (TM) 505","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":5,"event":1,"start":1},"fonts":{"count":11,"hash":"1b3c7bec80639c771f8258bd6a3bf2c6"},"audio":"124.08072766105033","resolution":{"w":"360","h":"760"},"availableResolution":{"w":"760","h":"360"},"ts":{"serve":1646300431603,"render":1646300408417}}',
    'specId': 'yidreg',
    'crumb': '7vik8idfuDk',
    'acrumb': 'Rrgflwg3',
    'done': 'https://www.yahoo.com',
    'attrSetIndex': '0',
    'tos0': 'oath_freereg|xa|ar-JO',
    'yid': email,
    'password': 'zaidkaream1',
    'shortCountryCode': 'AF',}
	response = requests.post(url,headers=headers,data=data).text
	if ('"yid"') in response:
		return jsonify(check=False, email= eml, Telegram="@JJJJzJJJ") 

	elif ('"birthDate"') in response:
		
		return jsonify(check=True, email= eml, Telegram="@JJJJzJJJ") 
		

	else:
		return jsonify(check=False, email= eml, Telegram="@JJJJzJJJ") 


if __name__=="__main__":
  app.run()
