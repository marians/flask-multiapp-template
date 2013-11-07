import webapps.one

if 'app' in dir(webapps.one):
    print "There is something called 'app' inside webapps.one."

webapps.one.app.run(debug=True)
