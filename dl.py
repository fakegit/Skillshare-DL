import sys, os
from skillshare import Skillshare

# or by class ID:
# dl.download_course_by_class_id(189505397)

cookie = """
__qca=P0-635299867-1571385528106; __ssid=cc3640f4e141f981692ba0ab4e5a97f; __utmc=99704988; __utmv=99704988.|1=visitor-type=user=1; __utmz=99704988.1571385527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1571385527921.1656880204; _gcl_au=1.1.1639240667.1571385527; device_session_id=2d456e00-7bef-4044-b78f-bc5f507b478f; IR_gbd=skillshare.com; __stripe_mid=b8b19c52-1c76-4ac0-b32d-312a98186974; G_ENABLED_IDPS=google; __pdst=d4adba231b7f4fc383668b99c7db6fe3; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; loc=%7B%22lat%22%3A%2260.1699%22%2C%22lng%22%3A%2224.9384%22%2C%22cid%22%3A%2266%22%2C%22city_name%22%3A%22Helsinki%22%2C%22city_district%22%3A%22%22%2C%22region%22%3Anull%2C%22region_code%22%3Anull%2C%22country_code%22%3A%22FI%22%2C%22country%22%3A%22Finland%22%7D; PHPSESSID=3238c17166588730ea6fd6580c0943b7; show-like-copy=1; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; YII_CSRF_TOKEN=QjBUVWdqWHBndnMxMm0zM0VraVFUMnRibm1hQVhNS0EJlnHHVZsbcE1orZT1PaDK5ocE-11CgpjYS4tBOavqJw%3D%3D; __utma=99704988.1959367213.1571385527.1571385527.1571390370.2; __utmt=1; __stripe_sid=9974a9b8-0748-409b-8e5c-307394584705; orientation-flow-data=%7B%22orientationPath%22%3A%7B%22orientation%5C%2Findex%22%3A%22orientation%5C%2Ffollowskills%22%2C%22orientation%5C%2Ffollowskills%22%3A%22orientation%5C%2Fclasses%22%2C%22orientation%5C%2Fclasses%22%3A%22orientation%5C%2Freferrals%22%2C%22orientation%5C%2Freferrals%22%3A%22orientation%5C%2Fcomplete%22%7D%2C%22viewedPages%22%3A%5B%5D%2C%22finalRedirect%22%3A%22https%3A%5C%2F%5C%2Fwww.skillshare.com%5C%2Fhome%3Fvia%3Dlogged-in-home%22%2C%22completesOrientation%22%3Atrue%2C%22force%22%3Atrue%7D; __utmb=99704988.2.10.1571390370; IRMS_la4650=1571390372965; mp_c0ffa2093d02e0d503db07fe142aab98_mixpanel=%7B%22distinct_id%22%3A%20%2216ddde04eb0614-0541abcf6a8899-b363e65-100200-16ddde04eb17c9%22%2C%22%24device_id%22%3A%20%2216ddde04eb0614-0541abcf6a8899-b363e65-100200-16ddde04eb17c9%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22%24user_id%22%3A%20%2216ddde04eb0614-0541abcf6a8899-b363e65-100200-16ddde04eb17c9%22%7D; pses={"id":"4ytwcer0s0h","start":1571390370123,"last":1571390373336}
"""

def main():
    dl = Skillshare(cookie=cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""	 
				 ____  _    _ _ _     _                          ____  _     
				/ ___|| | _(_) | |___| |__   __ _ _ __ ___      |  _ \| |    
				\___ \| |/ / | | / __| '_ \ / _` | '__/ _ \_____| | | | |    
				 ___) |   <| | | \__ \ | | | (_| | | |  __/_____| |_| | |___ 
				|____/|_|\_\_|_|_|___/_| |_|\__,_|_|  \___|     |____/|_____|  
					 _ __ ___  _ _  _ _ _  ___  _ _ 
					| / /| __>| \ || | | || . || | |
					|  \ | _> |   || | | ||   |\   /
					|_\_\|___>|_\_||__/_/ |_|_| |_| 

				Visit Us for more Cool Stuff: https://blackpearl.biz/

                """)


if __name__ == "__main__":
    info()
    main()

