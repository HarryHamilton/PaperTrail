if __name__ == '__main__':
    from src import create_app

    create_app().run(debug=True, host="0.0.0.0", port=9146)