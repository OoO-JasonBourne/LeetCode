def haveConflict(event1, event2):
    """
    思路： 当事件一的结束时间小于事件二的开始时间时事件不冲突
    同理，当事件二的结束时间小于时间一的开始时间时事件不冲突，
    反之时间冲突；
    不需要转成int，直接比较字符串即可
    """
    # 将时间转为分钟
    # def timeTrans(time):
    #     return int(time[:2]) * 60 + int(time[3:])
    # event1 = [timeTrans(event1[0]), timeTrans(event1[1])]
    # event2 = [timeTrans(event2[0]), timeTrans(event2[1])]
    if event1[0] > event2[1] or event1[1] < event2[0]: return False
    return Tru

