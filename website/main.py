from __init__ import create_app, redirect
import quickstart

app = create_app()

@app.route("/")
def home():
    return redirect(quickstart.main())

if __name__ =='__main__':
    app.run(debug=False) #off in production