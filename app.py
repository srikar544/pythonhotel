from app import create_app

print("Starting app...")
app = create_app()

if __name__ == "__main__":
    print("Running Flask Server")
    app.run(debug=True)