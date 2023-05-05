from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=3000)
    # this line will rerun the webserver any time we update the code
    # you would turn this off or debug=false in production