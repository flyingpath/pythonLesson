from .util import query as q

def writePlayData(par):

    try:
        name = par['name']
        skill = par['skill']
        lv = par['lv']
    except:
        return {
            'status': False,
            'err': '缺少參數'
        }

    sql = """
        insert into test (NAME, SKILL, LV)
        values (:name, :skill, :lv) 
    """
    
    result = q.queryWrite(sql, [name, skill, lv])
    
    return result
