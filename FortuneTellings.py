import random
from flask import Flask

App_FortuneTellings = Flask(__name__)


@App_FortuneTellings.route("/")
def FortuneTellings():
    # おみくじの結果リスト
    results = ["大吉 🌟 最高の一日になります！", "吉 👍 良いことあるかも。", "中吉 😊 穏やかに過ごせそう。", "凶 ☕ 暖かいコーヒーでも飲んでリラックス。"]

    # ランダムに1つ選ぶ
    fortune = random.choice(results)

    # 画面に表示するHTMLをPythonで作る
    html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>おみくじ</title></head>
    <body style="text-align: center; margin-top: 100px; font-family: sans-serif;">
        <h1>今日のおみくじ</h1>
        <h2 style="color: #ff4757; background: #f1f2f6; display: inline-block; padding: 200px; padding: 10px 20px; border-radius: 10px;">
            {fortune}
        </h2>
        <p><button onclick="location.reload()">もう一度引く</button></p>
    </body>
    </html>
    """
    return html


if __name__ == "__main__":
    App_FortuneTellings.run(host="0.0.0.0", port=8080)
