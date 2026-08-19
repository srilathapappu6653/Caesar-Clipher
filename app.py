from flask import Flask, render_template, request

app = Flask(__name__)


def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr(
                (ord(char) - base + shift) % 26 + base
            )
        else:
            result += char

    return result


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    text = ""
    shift = 3

    if request.method == "POST":
        text = request.form.get("text", "")
        shift = int(request.form.get("shift", 3))
        action = request.form.get("action")

        if action == "encrypt":
            result = caesar_cipher(text, shift)

        elif action == "decrypt":
            result = caesar_cipher(text, -shift)

    return render_template(
        "index.html",
        result=result,
        text=text,
        shift=shift
    )


if __name__ == "__main__":
    app.run(debug=True)