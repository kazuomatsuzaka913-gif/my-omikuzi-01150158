import streamlit as st
import random

# ページのタイトルと説明
st.title("🌟 令和・開運おみくじ 🌟")
st.write("ボタンを押すと、あなたの今日の運勢を占います。")

# ボタンを配置
if st.button("おみくじを引く"):
    # おみくじの結果リスト
    fortunes = [
        "✨ 大吉：最高の一日になります！",
        "😊 中吉：良いことがありそうです。",
        "🙂 小吉：穏やかな一日でしょう。",
        "🤔 吉：普通が一番です。",
        "🍃 末吉：一歩ずつ進みましょう。",
        "☔ 凶：忘れ物に注意してください。"
        "特別賞：りんたろう賞 りんたろうが全力で応援しています。"
    ]
    
    # ランダムに1つ選ぶ
    result = random.choice(fortunes)
    
    # 結果を表示
    st.balloons() # お祝いの風船を飛ばす
    st.header(result)