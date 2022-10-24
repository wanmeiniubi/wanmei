import time
from pymysql import connect


def get_result():
    try:
        conn = connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root123456',
            db='fabuzhan',
            charset='utf8')
        cursor = conn.cursor()
        time1 = int(time.time())
        # 置顶服sql语句
        sql = "select * from serverlist where endtime>%d and level=3;" % (time1)
        # 普通服sql语句
        sql2 = "select * from serverlist where endtime>%d and level=1;" % (time1)
        sql = sql.encode('utf-8')
        sql2 = sql2.encode('utf-8')
        try:
            cursor.execute(sql)
            zhiding_result = cursor.fetchall()
            cursor.execute(sql2)
            putong_result = cursor.fetchall()
            return zhiding_result,putong_result
            # print(zhiding_result)
            # print(putong_result)
        except Exception as e:
            print(e)
        finally:
            conn.close()
    except Exception as e:
        print(e)
    else:
        print('Connect Success:%s' % cursor)



def make_Tr(result):
    all_string = ""
    for i in result:
        ip = i[2]
        name = i[1]
        time = i[3]
        xianlu = i[4]
        qq = i[5]
        miaoshu = i[6]
        tuijian = i[7]
        content1 = u'''<tr bgcolor="#FFFF00" onmouseover="javascript:this.bgColor='#ffff99'" onmouseout="javascript:this.bgColor='#F8F8FF'">
                        <td height="22">&nbsp;<a href="{ip}" target="_blank">{name}</a></td>
                        <td align="center"><a href="{ip}" target="_blank">点击查看</a></td>
                        <td align="center"><font color="#FF359A"><b>{time}</b></font></td>
                        <td align="center">
                            {xianlu}</td><td align="center">{qq}</td>
                        <td>&nbsp;{miaoshu}<font color="#FF359A">-精品</font></td>
                        <td align="center"><a href="{ip}" target="_blank">点击查看</a></td>
                        <td align="center">{tuijian}</td>
                    </tr>\n'''.format(ip=ip,name=name,time=time,xianlu=xianlu,qq=qq,miaoshu=miaoshu,tuijian=tuijian)
        all_string = all_string + content1
    print(all_string)


def main():
    zhiding_result,putong_result = get_result()
    # print(zhiding_result)
    # print(putong_result)
    make_Tr(zhiding_result)

if __name__ == '__main__':
    main()