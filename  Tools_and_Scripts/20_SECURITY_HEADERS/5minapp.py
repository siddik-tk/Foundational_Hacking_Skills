from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, SIDDIK! Your security headers are working.</h1>'

@app.after_request
def set_headers(response: Response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


if __name__ == '__main__':
    app.run(debug=True)
