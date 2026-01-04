import streamlit as st
import random

# ページのタイトルと説明
st.title("🌟 りんたろす・開運おみくじ 🌟")
st.write("ボタンを押すと、あなたの今日の運勢を占います。")

# ボタンを配置
if st.button("おみくじを引く"):
    # おみくじの結果リスト
    fortunes = [
        "✨ 大吉：りんたろすがビッグな愛をぶつけます！",
        "😊 中吉：りんたろすが見つめています。",
        "🙂 小吉：りんたろすが照れています。",
        "🤔 吉：りんたろすが応援しています。",
        "🍃 末吉：りんたろすが頬を赤らめています。",
        "☔ 凶：りんたろすがそっと見守っています。",
    ]
    
    # ランダムに1つ選ぶ
    result = random.choice(fortunes)
    
    # 結果を表示
    st.balloons() # お祝いの風船を飛ばす
    st.header(result)