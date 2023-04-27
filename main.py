from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    # this line will rerun the webserver any time we update the code
    # you would turn this off or debug=false in production