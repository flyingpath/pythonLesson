from .util import query as q

def playData(par):

    try:
        name = par['name'][0]
    except:
        return {
            'status': False,
            'err': '缺少參數: name '
        }

    sql = """select 
            * 
        from 
            test 
        where 
            name=:name
    """
    
    result = q.query(sql, [name], False)
    
    return {
        'status': True,
        'data': result
    }
