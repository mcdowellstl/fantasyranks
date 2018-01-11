"""
   test python application
"""
import cherrypy

rb = {
    '1': {'name': 'Bob', 'points': '500' },
    '2': {'name': 'Reggie', 'points': '400'},
    '3': {'name': 'Pete', 'points': '300'}
}
wr = {
    '1': {'name': 'Randy', 'points': '400' },
    '2': {'name': 'Alex', 'points': '350'},
    '3': {'name': 'Chris', 'points': '300'}
}
qb = {
    '1': {'name': 'Keenan', 'points': '800' },
    '2': {'name': 'Andrew', 'points': '700'},
    '3': {'name': 'Aaron', 'points': '600'}
}
te = {
    '1': {'name': 'Travis', 'points': '200' },
    '2': {'name': 'Rob', 'points': '150'},
    '3': {'name': 'Zach', 'points': '100'}
}



class RB(object):
    exposed = True

    def GET(self, rb_id=None):
        if rb_id is None:
            return('top rbs: %s' % rb)
        elif rb_id in rb:
            getrb = rb[rb_id]
            return('rb #%s is %s, with %s points' %
                   (rb_id, getrb['name'], getrb['points']))
        else:
            return('i dont know the #%s rb ' % rb_id)

class WR(object):
    exposed = True

    def GET(self, wr_id=None):
        if wr_id is None:
            return('top wrs: %s' % wr)
        elif wr_id in rb:
            getwr = wr[wr_id]
            return('wr #%s is %s, with %s points' %
                   (wr_id, getwr['name'], getwr['points']))
        else:
            return('i dont know the #%s wr ' % wr_id)

class QB(object):
    exposed = True

    def GET(self, qb_id=None):
        if qb_id is None:
            return('top qbs: %s' % qb)
        elif qb_id in qb:
            getqb = qb[qb_id]
            return('qb #%s is %s, with %s points' %
                   (qb_id, getqb['name'], getqb['points']))
        else:
            return('i dont know the #%s qb ' % qb_id)

class TE(object):
    exposed = True

    def GET(self, te_id=None):
        if te_id is None:
            return('top tes: %s' % te)
        elif te_id in te:
            gette = te[te_id]
            return('te #%s is %s, with %s points' %
                   (te_id, gette['name'], gette['points']))
        else:
            return('i dont know the #%s te ' % te_id)



if __name__ == '__main__':
    cherrypy.tree.mount(RB(), '/api/rb', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }),
    cherrypy.tree.mount(WR(), '/api/wr', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }),
    cherrypy.tree.mount(QB(), '/api/qb', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    }),
    cherrypy.tree.mount(TE(), '/api/te', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })

    cherrypy.engine.start()
    cherrypy.engine.block()